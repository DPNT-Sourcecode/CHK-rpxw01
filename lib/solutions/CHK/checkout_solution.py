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

    # TODO: add average price for sorting to give customer best deal


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
    offers: list[SpecialOffer] | None = None
    bogof_offers: list[BOGOFOffer] | None = None


products_list = [
    SKU(
        name="A",
        price=50,
        offer=[SpecialOffer(count=3, price=130)],
    ),
    SKU(
        name="B",
        price=30,
        offer=[SpecialOffer(count=2, price=45)],
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
        if product.bogof_offers:
            for bogof_offer in product.bogof_offers:





    for product_name, product_order_count in orders_counter.items():
        base_price = products_map[product_name].price
        offer = products_map[product_name].offer
        #  handle the special offer
        product_order_price = 0
        if offer is not None:
            number_offer_multiples = math.floor(product_order_count / offer.count)
            remaining_orders = product_order_count % offer.count

            product_order_price += number_offer_multiples * offer.price
            product_order_price += remaining_orders * base_price
        else:
            product_order_price += product_order_count * base_price
        total_price += product_order_price

    return total_price
