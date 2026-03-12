def record_sales():
    sales = []
    amount = int(input("¿how many sales are you going to make? "))
    for _ in range(amount):
        product = input("Product: ")
        price = float(input("unit price: "))
        units = int(input("Units: "))
        total = price * units
        ventas.append({"product": product, "units": units, "total": total})
    return ventas