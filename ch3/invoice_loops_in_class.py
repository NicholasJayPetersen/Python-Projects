#!usr/bin/env python3

# display a welcome message
print(f"The Invoice Program")
print()

# get user entries
customer_type = input(f"Enter customer type (r/w):\t") #get customer type
invoice_total = float(input(f"Enter invoice total:\t\t")) #get invoice total
print()

# determine discounts for retail customers
if customer_type.lower() == "r":
    if invoice_total > 0 and invoice_total < 100: #set discount for 0-100
        discount_percent = 0
    elif invoice_total >= 100 and invoice_total < 250: #setdiscount for 100-249
        discount_percent = .1
    elif invoice_total>= 250 and invoice_total < 500: #setdiscount for 250-499
        discount_percent = .2
    elif invoice_total >= 500: #set discount for 500 or more
        discount_percent = .25

#determine discounts for wholesale customers
elif customer_type.lower() == "w":
    if invoice_total > 0 and invoice_total < 500: #set discount for 0-499
        discount_percent = .4
    elif invoice_total >= 500: #set discount for 500 or more
        discount_percent = .5

# set discount to zero if neither retail nor wholesale
else:
    discount_percent = 0

# calculate the new discount amount and invoice total
discount_amount = round(invoice_total * discount_percent, 2)
new_invoice_total = invoice_total - discount_amount

# display results
print(f"Invoice total:\t\t{invoice_total}")
print(f"Discount percent:\t{discount_percent}")
print(f"Discount amount:\t{discount_amount}")
print(f"New invoice total:\t{new_invoice_total}")
print()
print(f"Bye!")
