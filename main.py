from record import record_sales
from summary import generate_summary

def main():
    sales = record_sales()
    generate_summary(sales)

if _name_ == "_main_":
    main()