from dataclasses import dataclass, field
from collections import Counter, defaultdict
import math


# 2 different types of offer for now.
# Could be worth subclassing them off something common later, but not obviously worthwhile now.


@ dataclass
class SpecialOffer:
    """Represents a special offer for some product."""
    count: int
    price: int
    average_price: float = field(init=False)

    def __post_init__(self):
        """Calculate average price per item for sorting purposes to give customer the best deal."""
        self.average_price = self.price / self.count

@ dataclass
class BOGOFOffer:
    """
    Buy `n X product`, get `m X another_product` free.
    Can be later extended if needed for more combinations but works for this spec.
    """
    count: int
    free_product: str
    free_count: int

    def process(self, remaining_order_count: int) -> tuple[int, int]:
        """Handle the counting, return the remaining count, and a count to extend the free_products with."""

        num_free = math.floor(remaining_order_count / self.count)
        num_remaining = remaining_order_count % self.count
        return num_free, num_remaining


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


products_list = [
    SKU(
        name="A",
        price=50,
        offers=[
            SpecialOffer(count=3, price=130),
            SpecialOffer(count=5, price=200),
        ],
    ),
    SKU(
        name="B",
        price=30,
        offers=[SpecialOffer(count=2, price=45)],
    ),
    SKU(
        name="C",
        price=20,
    ),
    SKU(
        name="D",
        price=15,
    ),
    SKU(
        name="E",
        price=40,
        bogof_offers=[
            BOGOFOffer(
                count=2,
                free_product="B",
                free_count=1,
            )
        ]
    ),
]

products_map: dict[str, SKU] = {p.name: p for p in products_list}
allowed_products: set[str] = {p.name for p in products_list}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    """
    Calculate the total price of a list of items.
    Round 2.

    The argument is a string containing the SKUs of all products in the basket.
    Eg ``AABBCCC`` to mean, eg, [2xA, 2xB, 3xC].

    If the input is invalid (implements as the string containing any character that is not one of the product names)
    then return a ``-1`` response.
    """
    separate_orders = list(skus)

    if set(separate_orders) | allowed_products != allowed_products:
        return -1

    total_price = 0
    orders_counter = Counter(list(skus))

    # 1. handle the bogofs by looking for those and either constructing a second string without the free products,
    # or by building a dict listing the number free of each product.

    free_products = defaultdict(int)

    for product_name, product_order_count in orders_counter.items():
        product = products_map[product_name]
        # For each bogof (in case there could be multiple)
        # default is empty list so fine to just iterate.
        remaining_order_count = product_order_count
        # for each bogof for that product
        # sort by number required for free (asc)
        for bogof_offer in sorted(product.bogof_offers, key=lambda x: x.count):
            # get the number the offer gives free of the other thing
            num_free, remaining_order_count = bogof_offer.process(remaining_order_count)
            # and add that number to the list. use defaultdict to simplify stuff.
            free_products[bogof_offer.free_product] += num_free

    # 2. now do the normal offers and price summing.
    for product_name, product_order_count in orders_counter.items():
        product = products_map[product_name]

        # initialise price to zero
        product_order_price = 0
        remaining_order_count = product_order_count

        # remove any free items based on the bogofs, but capped at zero
        remaining_order_count = max(0, remaining_order_count - free_products[product_name])
        if remaining_order_count == 0:
            continue

        #  handle the special offers
        # sort by average price desc to get the best offer for the customer
        for offer in sorted(product.offers, key=lambda x: x.average_price):
            # get number of times the offer applies, calculate price
            number_offer_multiples = math.floor(remaining_order_count / offer.count)
            product_order_price += number_offer_multiples * offer.price

            # update the remaining_order_count
            remaining_order_count = remaining_order_count % offer.count

        # add price for any remaining ones.
        product_order_price += remaining_order_count * product.price
        total_price += product_order_price

    return total_price
