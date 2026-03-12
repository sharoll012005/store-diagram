def generate_summary(sales):
    summary = {}
    general = 0
    for v in sales:
        summary.setdefault(v["product"], 0)
        summary[v["product"]] += v["units"]
        general += v["total"]
    print("\nRESUMEN DE VENTAS DEL DÍA\n")
    for prod, cant in summary.items():
        print(f"Producto: {prod}\nCantidad total vendida: {cant}\n")
    print(f"Total recaudado: ${general:,.3f}")
    