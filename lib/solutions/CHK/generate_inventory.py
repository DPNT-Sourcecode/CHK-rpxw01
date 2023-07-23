

INVENTORY = """
| A    | 50    | 3A for 130, 5A for 200 |
| B    | 30    | 2B for 45              |
| C    | 20    |                        |
| D    | 15    |                        |
| E    | 40    | 2E get one B free      |
| F    | 10    | 2F get one F free      |
| G    | 20    |                        |
| H    | 10    | 5H for 45, 10H for 80  |
| I    | 35    |                        |
| J    | 60    |                        |
| K    | 80    | 2K for 150             |
| L    | 90    |                        |
| M    | 15    |                        |
| N    | 40    | 3N get one M free      |
| O    | 10    |                        |
| P    | 50    | 5P for 200             |
| Q    | 30    | 3Q for 80              |
| R    | 50    | 3R get one Q free      |
| S    | 30    |                        |
| T    | 20    |                        |
| U    | 40    | 3U get one U free      |
| V    | 50    | 2V for 90, 3V for 130  |
| W    | 20    |                        |
| X    | 90    |                        |
| Y    | 10    |                        |
| Z    | 50    |                        |
"""

SKU_TEMPLATE = """
    SKU(
        name="{name}",
        price={price},
        offers=[
            {offers}
        ],
    ),
"""

SPECIAL_OFFER_TEMPLATE = "SpecialOffer(count={count}, price={price})"
BOGOF_OFFER_TEMPLATE = "BOGOFOffer(count={count}, free_product={free_product}, free_count={free_count})"




def get_special_offer(offer_str):
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


def get_bogof_offer(offer_str):
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
        free_product=free_product,
        free_count=free_count,
    )

def generate_inventory():
    """
    Generate the inventory page based on the input as given in the problem spec.
    (you could copy/paste/string format, but this seems more reasonable to just make it repeatable.)

    Creates a module with a big list of nested classes, but could also do the same to go
    into a database, for a more realistic scenario.
    """
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
        if offers:
            for offer in offers.split(","):
                if "for" in offer_str:
                    offer_templates.append(get_special_offer(offer_str.))








if __name__ == "__main__":
    generate_inventory()





