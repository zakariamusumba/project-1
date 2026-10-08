products = ("1. Bread @sh 65\n  2. Milk @sh 60\n 3. Eggs @sh 20\n 4. Grapes @sh 200\n 5. soda @sh 80\n")
choice = input("Enter your choice: ")
if choice == "1":
        amount = int(input("Enter the amount: "))
        discount = 15
        subtotal = amount * 65 - discount
        print(subtotal)

elif choice == "2":
        amount = int(input("Enter the amount: "))
        discount = 20
        subtotal = amount  * 60 - discount
        print(subtotal)

elif choice == "3":
        amount = int(input("Enter the amount: "))
        discount = 12
        subtotal = amount  * 20 - discount
        print(subtotal)

elif choice == "4":
        amount = int(input("Enter the amount: "))
        discount = 75
        subtotal = amount  * 200 - discount
        print(subtotal)

elif choice == "5":
        amount = int(input("Enter the amount: "))
        discount = 15
        subtotal = amount  * 60 - discount
        print(subtotal)

else:
        print("products have finished")

payment_amount = input("Enter your payment: ")
if payment_amount == 100:
        print ("Payment successful")
elif payment_amount != 100:
        print ("Insufficient funds")

def available_products (items):
        print("YOUR ITEMS")
        items ["bread :65\n" "milk: 60\n" "eggs: 20\n" "grapes: 200\n" "soda: 80\n"]
        print(f"these {items} are available")

def add_products(items):
        items ["bread :65\n" "milk: 60\n" "eggs: 20\n" "grapes: 200\n" "soda: 80\n"]
        basket += items.add("cheese: 700\n")
        print(f"{items} have been stored in your basket")

def remove_item(items):
        items ["bread :65\n" "milk: 60\n" "eggs: 20\n" "grapes: 200\n" "soda: 80\n"]
        basket = items.remove(0)
        print(basket)

def calculate_total(items):
        items ["bread :65\n" "milk: 60\n" "eggs: 20\n" "grapes: 200\n" "soda: 80\n"]
        total += items
        print(total)

def process_payment(items):
        items ["bread :65\n" "milk: 60\n" "eggs: 20\n" "grapes: 200\n" "soda: 80\n"]
        total_payment = items % 100
        print(total_payment)

def reciept_structure(items):
        items ["bread :65\n" "milk: 60\n" "eggs: 20\n" "grapes: 200\n" "soda: 80\n"]
        basket = items
        print(basket)