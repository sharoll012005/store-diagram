from registro import register_sales
from resumen import trigger_summary_summary

def main():
    sales = register_sales()
    trigger_summary(sales)

if _name_ == "_main_":
    main()