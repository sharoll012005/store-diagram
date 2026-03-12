def record_sales():
    sales = []
    amount = int(input("¿Cuántas ventas vas a hacer? "))
    for _ in range(amount):
        product = input("Product: ")
        price = float(input("unit price: "))
        units = int(input("Units: "))
        total = price * units
        sales.append({"product": product, "units": units, "total": total})
    return sales