"""
See ``generate_offers.py`` for how to create the inventory.
"""
from collections import Counter, defaultdict
import math

from .generate_inventory import SKU
from .inventory import PRODUCTS_LIST, GROUP_OFFERS


# 2 different types of offer for now.
# Could be worth subclassing them off something common later, but not obviously worthwhile now.


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
    products_map: dict[str, SKU] = {p.name: p for p in PRODUCTS_LIST}
    allowed_products: set[str] = {p.name for p in PRODUCTS_LIST}

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
            # If the bogof refers to itself, check that there are enough in the basket to allow it.
            # get the number the offer gives free of the other thing
            # If it is a self-referential bogof, it checks that there are enough.
            num_free, remaining_order_count = bogof_offer.process(product.name, remaining_order_count)
            # and add that number to the list. use defaultdict to simplify stuff.
            free_products[bogof_offer.free_product] += num_free

    # 2. Now handle the ``Buy any n of A,B,C,D,E for m``
    # we handle this by selecting out all of them per group offer, and adding used ones to the "free" list,
    # then manually adding the full price on.
    for group_offer in GROUP_OFFERS

    # 3. now do the normal offers and price summing.
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

