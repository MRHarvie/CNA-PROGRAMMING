print("SALES DATA IMPORTER")
print("\nEnter Sales Data")
total_sales = 0
for i in range(1,4):
    amount_1 = float(input("\nAmount:\t\t\t\t"))
    year = int(input("Year:\t\t\t\t"))
    month = int(input("Month (1-12):\t\t"))
    day = int(input("Day (1-31):\t\t\t"))
    print("\n",i,"\t\t\t",year,"-",month,"-",day,"\t\t","$",amount_1)
    total_sales += amount_1
print("\nTotal Sales")
print(20*"=")
print("$",total_sales)

print("\nBye!")
