import dataclasses, field


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







# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    """
    Calculate the total price of a list of items.

    The argument is a string containing the SKUs of all products in the basket.
    The input is not well defined for now, so we will assume (lol) that it is like
    ``AABBCCC`` to mean, eg, [2xA, 2xB, 3xC] for now,
    and correct it later on if needed depending on how the tests go.
    """



