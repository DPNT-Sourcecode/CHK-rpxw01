import dataclasses, field


dataclass
class SpecialOffer:
    """Represents a special offer for some product."""
    count: int
    price: int


@dataclass
class SKU:
    """Represents one type of product"""
    name: str
    price: int
    offers: list[SpecialOffer()]
    special_offer_count: int | None = field(init=False)

    def __post_init__(self):
        self.c = self.a + self.b







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


