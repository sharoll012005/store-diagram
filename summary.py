def generate_summary(sales):
    summary = {}
    general = 0
    for v in record_sales:
        summary.setdefault(v["product"], 0)
        summary[v["product"]] += v["units"]
        general += v["total"]
    print("\nsummary:")
    for prod, cant in summary.items():
        print(f"{prod}: {cant} units")
    print(f"Total raised: {general}"