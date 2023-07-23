"""
Generate a module containing a list of class instances based on the given inventory below.
Could be extended to take it like a cmd program but more than enough for now.

Alternatively, you could do this whole thing by reading the same way and then inserting into a database.

Just run ``python generate_inventory.py`` to regenerate.

"""
from textwrap import indent
from dataclasses import dataclass, field


INVENTORY = """
| A    | 50    | 3A for 130, 5A for 200          |
| B    | 30    | 2B for 45                       |
| C    | 20    |                                 |
| D    | 15    |                                 |
| E    | 40    | 2E get one B free               |
| F    | 10    | 2F get one F free               |
| G    | 20    |                                 |
| H    | 10    | 5H for 45, 10H for 80           |
| I    | 35    |                                 |
| J    | 60    |                                 |
| K    | 70    | 2K for 120                      |
| L    | 90    |                                 |
| M    | 15    |                                 |
| N    | 40    | 3N get one M free               |
| O    | 10    |                                 |
| P    | 50    | 5P for 200                      |
| Q    | 30    | 3Q for 80                       |
| R    | 50    | 3R get one Q free               |
| S    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| T    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| U    | 40    | 3U get one U free               |
| V    | 50    | 2V for 90, 3V for 130           |
| W    | 20    |                                 |
| X    | 17    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Y    | 20    | buy any 3 of (S,T,X,Y,Z) for 45 |
| Z    | 21    | buy any 3 of (S,T,X,Y,Z) for 45 |
"""


###################################################################


@dataclass
class SpecialOffer:
    """Represents a special offer for some product."""
    count: int
    price: int
    average_price: float = field(init=False)

    def __post_init__(self):
        """Calculate average price per item for sorting purposes to give customer the best deal."""
        self.average_price = self.price / self.count


@dataclass
class BOGOFOffer:
    """
    Buy `n X product`, get `m X another_product` free.
    Can be later extended if needed for more combinations but works for this spec.
    """
    count: int
    free_product: str
    free_count: int

    def process(self, base_product: str, remaining_order_count: int) -> tuple[int, int]:
        """
        Handle the counting, return the remaining count, and a count to extend the free_products with.

        Need to do a loop for each application since if the bogof refers to itself, it requires an extra count for it to actually work.

        For example, if it is "2A" giving free "1B", we need 4A-> 2B free,
        But if its 2A -> 1A:

            - 3A-> 1Afree, 2Apaid,
            - 4A -> 1Afree, 3Apaid
            - 5A -> 1Afree, 4Apaid  (next would be free)
            - 6A -> 2Afree, 4Apaid

        Can't actually only do a check once because of this edge case.
        """

        if base_product == self.free_product:
            num_required_to_apply = self.count + self.free_count
        else:
            num_required_to_apply = self.count

        num_free = 0
        while remaining_order_count >= num_required_to_apply:
            num_free += 1
            remaining_order_count -= num_required_to_apply

        return num_free, remaining_order_count


@dataclass
class SKU:
    """
    Represents one type of product
    For now it has a name and a price, plus optionally a special offer.
    We will assume that it could have multiple types of offer later,
    but simplify a little and do it for only one now until we know more.

    Takes 2 separate lists of offers/bogof_offers for now,
    but if there are more then they could always be combined and we
    could search through with an isinstance or something.
    """
    name: str
    price: int
    offers: list[SpecialOffer] = field(default_factory=list)
    bogof_offers: list[BOGOFOffer] = field(default_factory=list)


###################################################################

MODULE_TEMPLATE = """
from .generate_inventory import SKU, SpecialOffer, BOGOFOffer


GROUP_OFFERS = [
    {group_offers}
]

PRODUCTS_LIST = [
{templates}
]

"""

SKU_TEMPLATE = """
    SKU(
        name="{name}",
        price={price},
        offers=[
{offers}
        ],
        bogof_offers=[
{bogof_offers}
        ],
    ),
"""

SPECIAL_OFFER_TEMPLATE = """SpecialOffer(count={count}, price={price}),"""
BOGOF_OFFER_TEMPLATE = """BOGOFOffer(count={count}, free_product="{free_product}", free_count={free_count}),"""
GROUP_OFFER_TEMPLATE = """GroupOffer(count={count}, price={price}, products=[{products}]),"""


def get_special_offer(offer_str: str) -> str:
    """Takes a string like ``3Q for 80`` and formats a ``SpecialOffer`` init.
    """
    pieces = offer_str.strip().split()
    price = pieces[2]
    subset = pieces[0]
    count = int(subset[:-1])

    return SPECIAL_OFFER_TEMPLATE.format(
        count=count,
        price=price,
    )


def get_bogof_offer(offer_str: str) -> str:
    """
    Takes a string like ``2F get one F free`` and formats a BOGOFOffer init.
    """
    pieces = offer_str.strip().split()
    product = pieces[3]

    # If this isn't only for "one" then it needs more logic...
    assert " one " in offer_str

    subset = pieces[0]
    count = int(subset[:-1])

    return BOGOF_OFFER_TEMPLATE.format(
        count=count,
        free_product=product,
        free_count=1,
    )


def get_group_offer(offer_str: str) -> str:
    """
    Takes a string like ``buy any 3 of (S,T,X,Y,Z) for 45 and formats a GroupOffer init``.

    could use regex to find the pieces between the brackets, but can extend to that later if needed.
    """
    pieces = offer_str.split()
    count = int(pieces[2])
    price = int(pieces[-1])
    products_base_str = pieces[4].strip("()")
    products = ", ".join(sorted([f'"{p}"' for p in products_base_str.split(",")]))

    return GROUP_OFFER_TEMPLATE.format(
        count=count,
        price=price,
        products=products,
    )


def generate_inventory():
    """
    Generate the inventory page based on the input as given in the problem spec.
    (you could copy/paste/string format, but this seems more reasonable to just make it repeatable.)

    Creates a module with a big list of nested classes, but could also do the same to go
    into a database, for a more realistic scenario.
    """
    product_templates = []
    group_offer_templates = []
    for inventory_line in INVENTORY.strip().splitlines():

        # don't strip the bars off the ends, else the rows without offers will have fewer items after splitting.
        # => eg: ``['', ' C    ', ' 20    ', '                        ', '']``
        pieces = inventory_line.split("|")

        # => eg ``['', 'C', '20', '', '']``
        pieces = [p.strip() for p in pieces]

        product = pieces[1]
        price = int(pieces[2])
        offers = pieces[3]

        offer_templates = []
        bogof_offer_templates = []
        group_offer_templates = []
        if offers:
            for offer_str in offers.split(", "):    # ", " **including the space** to avoid splitting on group offers.
                if "any" in offer_str:
                    group_offer_templates.append(get_group_offer(offer_str))
                elif "for" in offer_str:
                    offer_templates.append(get_special_offer(offer_str))
                elif "get one" in offer_str:
                    bogof_offer_templates.append(get_bogof_offer(offer_str))
                else:
                    raise ValueError(f"Some unsupported offer str: {offer_str=}")
        if offer_templates:
            offer_template = indent("\n".join(offer_templates), "            ")
        else:
            offer_template = ""
        if bogof_offer_templates:
            bogof_offer_template = indent("\n".join(bogof_offer_templates), "            ")
        else:
            bogof_offer_template = ""

        product_templates.append(SKU_TEMPLATE.format(
            name=product,
            price=price,
            offers=offer_template,
            bogof_offers=bogof_offer_template,
        ))

        full_products_template = indent("\n".join(product_templates), "")
        full_group_offer_template = indent("\n".join(set(group_offer_templates)), "")   # go via a set to deduplicate.

        full_module_template = MODULE_TEMPLATE.format(
            templates=full_products_template,
            group_offers=full_group_offer_template,
        ).strip("\n")

        with open("inventory.py", "w") as f:
            f.write(full_module_template)


if __name__ == "__main__":
    generate_inventory()
