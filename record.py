def record_sales():
sales = []
    amount = int(input("¿How many sales are you going to make? "))
    count = 0
    while count < amount:
        product = input("Producto: ").strip()
        while product == "":
            product = input("Producto (no vacío): ").strip()

        unit_price = float(input("Precio unitario: "))
        while unit_price <= 0:
            unit_price = float(input("Precio unitario (>0): "))

        units = int(input("Unidades: "))
        while units <= 0:
            units = int(input("Unidades (>0): "))

        total = unit_price * units
        sales.append({
            "product": product,
            "units": units,
            "unit_price": unit_price,
            "total": total
        })
        count += 1

    another = input("¿Registrar otra venta? (s/n): ").lower()
    while another == "s":
        product = input("Producto: ").strip()
        while product == "":
            product = input("Producto (no vacío): ").strip()

        unit_price = float(input("Precio unitario: "))
        while unit_price <= 0:
            unit_price = float(input("Precio unitario (>0): "))

        units = int(input("Unidades: "))
        while units <= 0:
            units = int(input("Unidades (>0): "))

        total = unit_price * units
        sales.append({
            "product": product,
            "units": units,
            "unit_price": unit_price,
            "total": total
        })
        another = input("¿Registrar otra venta? (s/n): ").lower()

    print("Saldrán guardando ventas")
    return sales