#!usr/bin/env python3

def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Plese try again")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Total Calculator Program\n")

    price = get_price()
    quantity = get_quantity()

    total = price * quantity

    print()
    print("price:        ", price)
    print("quantity:     ", quantity)
    print("total:        ", total)

if __name__ == "__main__":
    main()
