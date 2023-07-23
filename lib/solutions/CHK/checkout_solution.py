import dataclasses, field
from collections import Counter


dataclass
class SpecialOffer:
    """Represents a special offer for some product."""
    count: int
    price: int


@dataclass
class SKU:
    """
    Represents one type of product
    For now it has a name and a price, plus optionally a special offer.
    We will assume that it could have multiple types of offer later,
    but simplify a little and do it for only one now until we know more.
    """
    name: str
    price: int
    offer: SpecialOffer | None


products_list = [
    SKU(
        name="A",
        price=50,
        offer=SpecialOffer(count=3, price=130),
    ),
    SKU(
        name="B",
        price=30,
        offer=SpecialOffer(count=2, price=45),
    ),
    SKU(
        name="C",
        price=20,
    ),
    SKU(
        name="D",
        price=15,
    ),
]

products_map: dict[str, SKU] = {p.name: p for p in products_list}
allowed_products: set[str] = {p.name for p in products_list}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    """
    Calculate the total price of a list of items.

    The argument is a string containing the SKUs of all products in the basket.
    The input is not well defined for now, so we will assume (lol) that it is like
    ``AABBCCC`` to mean, eg, [2xA, 2xB, 3xC] for now,
    and correct it later on if needed depending on how the tests go.
    Maybe I take a time penalty but in reality you just go back and ask for a more precise spec...

    If the input is invalid (implements as the string containing any character that is not one of the product names)
    then return a ``-1`` response.
    """
    separate_orders = list(skus)

    if set(separate_orders) | allowed_products != allowed_products:
        return -1

    total_price = 0
    orders_counter = Counter(list(skus))
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







