def record_sales():
    sales = []
    amount = int(input("¿How many sales are you going to make? "))
    count = 0
    while count < amount:
        product = input("Product: ").strip()
        while product == "":
            product = input("Product (not empty): ").strip()

        unit_price = float(input("unit price: "))
        while unit_price <= 0:
            unit_price = float(input("unit price (>0): "))

        units = int(input("Unit: "))
        while units <= 0:
            units = int(input("Unit (>0): "))

        total = unit_price * units
        sales.append({
            "product": product,
            "units": units,
            "unit_price": unit_price,
            "total": total
        })
        count += 1

    another = input("¿Register another sale? (s/n): ").lower()
    while another in ("s", "si"):
        product = input("Product: ").strip()
        while product == "":
            product = input("Product (not empty): ").strip()

        unit_price = float(input("unit price: "))
        while unit_price <= 0:
            unit_price = float(input("unit price (>0): "))

        units = int(input("Unit: "))
        while units <= 0:
            units = int(input("Unit (>0): "))

        total = unit_price * units
        sales.append({
            "product": product,
            "units": units,
            "unit_price": unit_price,
            "total": total
        })
        another = input("¿Register another sale? (s/n): ").lower()

    print("save sales information")
    return sales