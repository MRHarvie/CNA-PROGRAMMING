#Inputing Customer Type and Invocie Total
print("The Invoice Program")
customer_type = input("Enter customer type (R or W):   ")
invoice_total = int(input("What is the total amount of invoice?  "))
print("\nInvoice Total: {}".format(invoice_total))
# Conditional Invoice Parameters
if customer_type.lower() == "r":
    if invoice_total < 250:
        discount_percent = 0
    elif invoice_total >= 250:
        discount_percent = .02
elif customer_type.lower() == "w":
    discount_percent = .04
else:
    print ("Customer Type Must Be R or W")
print("Invoice Total: {}".format(discount_percent))
# Final Calculation on Discount
invoice_final = (invoice_total)-(invoice_total*discount_percent)
print("\nYour Invoice Price With/Without Discount is: {} ".format(invoice_final))
