from record import record_sales
from summary import generate_summary

def main():
    sales = record_sales()
    generate_summary(sales)

if __name__=="__main__":
    main()