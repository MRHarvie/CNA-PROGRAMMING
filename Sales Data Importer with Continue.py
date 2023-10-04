print("SALES DATA IMPORTER")
print("\nEnter Sales Data")
total_sales = 0
xxy = "y"
index_r = 1
while xxy.lower() == 'y':
    amount_1 = float(input("\nAmount:\t\t\t\t"))
    year = int(input("Year:\t\t\t\t"))
    month = int(input("Month (1-12):\t\t"))
    day = int(input("Day (1-31):\t\t\t"))
    if month == 1 or month == 2 or month == 3:
        quarter = "Q1"
    elif month == 3 or month == 4 or month == 5:
        quarter = "Q2"
    elif month == 6 or month == 7 or month == 8:
        quarter = "Q3"
    else:
        quarter = "Q4" 
    print("\n",index_r,"\t\t\t",year,"-",month,"-",day,"\t\t",quarter,"\t\t","$",amount_1)
    index_r += 1
    total_sales += amount_1
    if input("\nContinue? (y/n)     ") != 'y' and 'Y':
        break
print("\nTotal Sales")
print(20*"=")
print("$",total_sales)

print("\nBye!")







