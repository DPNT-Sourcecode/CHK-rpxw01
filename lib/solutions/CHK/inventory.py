from .generate_inventory import SKU, SpecialOffer, BOGOFOffer

PRODUCTS_LIST = [

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
        offers=[
            SpecialOffer(count=2, price=45),
        ],
    ),


    SKU(
        name="C",
        price=20,
        offers=[

        ],
    ),


    SKU(
        name="D",
        price=15,
        offers=[

        ],
    ),


    SKU(
        name="E",
        price=40,
        offers=[
            BOGOFOffer(count=2, free_product="B", free_count=1),
        ],
    ),


    SKU(
        name="F",
        price=10,
        offers=[
            BOGOFOffer(count=2, free_product="F", free_count=1),
        ],
    ),


    SKU(
        name="G",
        price=20,
        offers=[

        ],
    ),


    SKU(
        name="H",
        price=10,
        offers=[
            SpecialOffer(count=5, price=45),
            SpecialOffer(count=10, price=80),
        ],
    ),


    SKU(
        name="I",
        price=35,
        offers=[

        ],
    ),


    SKU(
        name="J",
        price=60,
        offers=[

        ],
    ),


    SKU(
        name="K",
        price=80,
        offers=[
            SpecialOffer(count=2, price=150),
        ],
    ),


    SKU(
        name="L",
        price=90,
        offers=[

        ],
    ),


    SKU(
        name="M",
        price=15,
        offers=[

        ],
    ),


    SKU(
        name="N",
        price=40,
        offers=[
            BOGOFOffer(count=3, free_product="M", free_count=1),
        ],
    ),


    SKU(
        name="O",
        price=10,
        offers=[

        ],
    ),


    SKU(
        name="P",
        price=50,
        offers=[
            SpecialOffer(count=5, price=200),
        ],
    ),


    SKU(
        name="Q",
        price=30,
        offers=[
            SpecialOffer(count=3, price=80),
        ],
    ),


    SKU(
        name="R",
        price=50,
        offers=[
            BOGOFOffer(count=3, free_product="Q", free_count=1),
        ],
    ),


    SKU(
        name="S",
        price=30,
        offers=[

        ],
    ),


    SKU(
        name="T",
        price=20,
        offers=[

        ],
    ),


    SKU(
        name="U",
        price=40,
        offers=[
            BOGOFOffer(count=3, free_product="U", free_count=1),
        ],
    ),


    SKU(
        name="V",
        price=50,
        offers=[
            SpecialOffer(count=2, price=90),
            SpecialOffer(count=3, price=130),
        ],
    ),


    SKU(
        name="W",
        price=20,
        offers=[

        ],
    ),


    SKU(
        name="X",
        price=90,
        offers=[

        ],
    ),


    SKU(
        name="Y",
        price=10,
        offers=[

        ],
    ),


    SKU(
        name="Z",
        price=50,
        offers=[

        ],
    ),

]
