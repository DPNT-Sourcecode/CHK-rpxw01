from .generate_inventory import SKU, SpecialOffer, BOGOFOffer

PRODUCTS_LIST = [

    SKU(
        name="A",
        price=50,
        offers=[
            SpecialOffer(count=3, price=130),
            SpecialOffer(count=5, price=200),
        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="B",
        price=30,
        offers=[
            SpecialOffer(count=2, price=45),
        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="C",
        price=20,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="D",
        price=15,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="E",
        price=40,
        offers=[

        ],
        bogof_offers=[
            BOGOFOffer(count=2, free_product="B", free_count=1),
        ],
    ),


    SKU(
        name="F",
        price=10,
        offers=[

        ],
        bogof_offers=[
            BOGOFOffer(count=2, free_product="F", free_count=1),
        ],
    ),


    SKU(
        name="G",
        price=20,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="H",
        price=10,
        offers=[
            SpecialOffer(count=5, price=45),
            SpecialOffer(count=10, price=80),
        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="I",
        price=35,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="J",
        price=60,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="K",
        price=80,
        offers=[
            SpecialOffer(count=2, price=150),
        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="L",
        price=90,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="M",
        price=15,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="N",
        price=40,
        offers=[

        ],
        bogof_offers=[
            BOGOFOffer(count=3, free_product="M", free_count=1),
        ],
    ),


    SKU(
        name="O",
        price=10,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="P",
        price=50,
        offers=[
            SpecialOffer(count=5, price=200),
        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="Q",
        price=30,
        offers=[
            SpecialOffer(count=3, price=80),
        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="R",
        price=50,
        offers=[

        ],
        bogof_offers=[
            BOGOFOffer(count=3, free_product="Q", free_count=1),
        ],
    ),


    SKU(
        name="S",
        price=30,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="T",
        price=20,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="U",
        price=40,
        offers=[

        ],
        bogof_offers=[
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
        bogof_offers=[

        ],
    ),


    SKU(
        name="W",
        price=20,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="X",
        price=90,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="Y",
        price=10,
        offers=[

        ],
        bogof_offers=[

        ],
    ),


    SKU(
        name="Z",
        price=50,
        offers=[

        ],
        bogof_offers=[

        ],
    ),

]
