def my_sum(**args):
    product = args.copy()
    for key in product:
        print(f"{key}: --> {product[key]}")
    print("*" * 50)


#! kwargs is used when you don't know the exact number of parameters for your function but you need to specify the name of each parameter
my_sum(id="1654", name="Poco X4 Pro", brand="Xiaomi")
my_sum(id="1154", name="Master Mx S3", brand="Logitech", dpis="3600ms")
