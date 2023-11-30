print("The Total Calculator Program")
def get_price():
    while True:
        try:
            price = float(input("Enter Price:   "))
            return price        
        except ValueError:
            print("Invalid Decimal number. Please try again.")
    
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter Quantity:    "))   
            return quantity
        except ValueError:
            print("Invalid Integer. Please Try Again.")
        

    
program = True
while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity
            
           
        print(f"Price:     {price}")
        print(f"Quantity:   {quantity}")
        print(f"Total:    {total}")