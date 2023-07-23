

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

