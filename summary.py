def generate_summary(sales):
    summary = {}
    general = 0
    for v in sales:
        summary.setdefault(v["product"], 0)
        summary[v["product"]] += v["units"]
        general += v["total"]
    print("\nDAILY SALES SUMMARY\n")
    for prod, cant in summary.items():
        print(f"Product: {prod}\ntotal quantity sold: {cant}\n")
    print(f"TOTAL RAISED: ${general:,.3f}")
    