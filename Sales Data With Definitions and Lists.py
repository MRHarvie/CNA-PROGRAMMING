def get_amount():
    while True:
        amount = float(input("Amount:    "))
        if amount > 0:
            return amount
        else:
            print("Sales must be greater than 0.")
def get_day(month):
    if month == 2:
        max_days = 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        max_days = 30
    else:
        max_days = 31
    while True:
        day = int(input(f"Day (1 - {max_days}):  "))
        if day >= 1 and day <= max_days:
            return day
        else:
            print("Day Must Be Between 1 and {max_days}/  /n")

def get_month():
    while True:
        month = int(input("Month (1-12):   "))
        if month >= 1 and month <= 12:
            return month
        else:
            print("Month should be between 1-12.")
def get_year():
    while True:
            year = input("Year (1900-3000):    ")
            if year >= 1900 and year <= 3000:
                return year
            else:
                print("Please select a valid year (1900-3000). \n")
                
def title():
    print("SALES DATA IMPORTER")
    
def cmd_menu():
    print("view - View All Sales")
    print("add - Add Sales")
    print("menu - Show Menu")
    print("exit - Exit Program")
    print()
    
def get_qrtr(month):
    if month > 0 and month <= 3:
        quarter = 1
    elif month >= 4 and month <=6:
        quarter = 2
    elif month >= 7 and month <= 9:
        quarter = 3
    else:
        quarter = 4
    return quarter

def view_sales(sales):
    if len(sales) == 0:
        print("No Sales to report.")
    else:
        total_sales = 0
        print("\tDate\t\tQuarter\t\tAmount")
        print(40*"=")
        for num, data in enumerate(sales, start = 1):
            amount = data[0]
            year = data[1]
            month = data[2]
            day = data[3]
            quarter = data[4]
            total_sales += amount
            
            print(f"{num}.\t{year}-{month}-{day}\t{quarter}\t\t${amount}")
        print(40*"=") 
        print(f"TOTAL: \t\t\t\t\t${total_sales}")
        
def add_sales(sales):
    amount = sales.get_amount()
    year = sales.get_year()
    month = sales.get_month()
    day = sales.get_day(month)
    print()    
    quarter = get_qrtr(month)
    sales_data = [amount,year,month,day,quarter]
    sales.append(sales_data)
    print(f"Sales for {year}-{month}-{day} added. \n")
    
def main():
    title()
    cmd_menu()
    sales = []
    while True:
        command = input("Command:  ")
        if command == 'view':
             print("\t\t\tDay\t\tYear\t\t\tQuarter\t\t\tAmount")
             view_sales(sales)
        elif command == 'add':
            add_sales(sales)
        elif command == 'menu':
            cmd_menu()
        elif command == "exit":
            print()
            break
        else:
            print("Please select a valid command.")
            print()
            cmd_menu()
    print("Bye!")
    
if __name__ == '__main__':
        main()
