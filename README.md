# 🛒 Shopping Basket and Payment System

## 📌 Project Description

This project is a simple **Python shopping basket and payment system**. It allows a user to select a product, enter the quantity they want to purchase, calculate the subtotal after a discount, and enter a payment amount.

The project also contains several functions intended to manage products and a shopping basket, including adding products, removing items, calculating the total, processing payments, and generating a receipt.

---

## 🧾 Available Products

The program currently contains the following products:

| No. | Product | Price |
|---|---|---:|
| 1 | Bread | KSh 65 |
| 2 | Milk | KSh 60 |
| 3 | Eggs | KSh 20 |
| 4 | Grapes | KSh 200 |
| 5 | Soda | KSh 80 |

---

## ✨ Features

The project is designed to provide the following features:

- Display available products.
- Allow the user to select a product.
- Ask the user for the quantity required.
- Calculate the product subtotal.
- Apply a discount to the purchase.
- Accept payment from the customer.
- Check whether payment is sufficient.
- Display available products.
- Add products to a shopping basket.
- Remove products from the basket.
- Calculate the total cost.
- Process payments.
- Display a receipt.

---

## 🛠️ Functions

The project contains several functions:

### `available_products(items)`

Displays the products that are available for purchase.

### `add_products(items)`

Intended to add products to the customer's shopping basket.

### `remove_item(items)`

Intended to remove an item from the shopping basket.

### `calculate_total(items)`

Intended to calculate the total price of the products in the basket.

### `process_payment(items)`

Intended to process the customer's payment.

### `reciept_structure(items)`

Intended to display the customer's receipt.

> **Note:** The function name `reciept_structure` could be renamed to `receipt_structure` because "receipt" is the correct spelling.

---

## ▶️ How to Run the Project

### 1. Install Python

Make sure Python is installed on your computer.

You can check by running:

```bash
python --version
```

### 2. Save the program

Save the Python code in a file, for example:

```text
shopping.py
```

### 3. Run the program

Open a terminal in the project folder and run:

```bash
python shopping.py
```

### 4. Select a product

When prompted:

```text
Enter your choice:
```

Enter a number from `1` to `5`.

For example:

```text
Enter your choice: 1
```

The program will then ask:

```text
Enter the amount:
```

Enter the quantity you want.

---

## 💰 Example

If the user selects bread and wants 2 loaves:

```text
Enter your choice: 1
Enter the amount: 2
95
```

The calculation is:

```text
2 × KSh 65 = KSh 130
KSh 130 - KSh 15 discount = KSh 115
```

---

## ⚠️ Current Limitations

The current version of the project still needs some improvements.

### Payment Input

The program uses:

```python
payment_amount = input("Enter your payment: ")
```

`input()` returns a string, so comparing it directly with:

```python
if payment_amount == 100:
```

will not work as expected.

It should be converted to an integer or float first:

```python
payment_amount = int(input("Enter your payment: "))
```

### Soda Price

The product list says soda costs **KSh 80**, but the calculation currently uses:

```python
subtotal = amount * 60 - discount
```

The soda calculation should use `80`.

### Basket Variables

Some functions use variables such as:

```python
basket
total
```

without defining them first. These variables need to be created before they are used.

### List Operations

Some statements such as:

```python
items ["bread :65\n"]
```

are not valid Python list operations.

The project should use a list or dictionary to store products.

For example:

```python
products = {
    "bread": 65,
    "milk": 60,
    "eggs": 20,
    "grapes": 200,
    "soda": 80
}
```

### Adding Items

The current code uses:

```python
items.add()
```

Python lists use:

```python
items.append()
```

while sets use `.add()`.

### Payment Calculation

The payment-processing function currently uses:

```python
total_payment = items % 100
```

The payment should instead be compared against the total amount that the customer owes.

---

## 🚀 Future Improvements

The project can be improved by adding:

- A proper shopping cart.
- Multiple products in one order.
- Product quantities.
- Automatic total calculation.
- Proper discount calculations.
- Change calculation after payment.
- Input validation.
- A printable receipt.
- Product stock management.
- A menu that allows users to continue shopping.
- A function to remove specific products from the basket.
- Error handling for invalid input.

---

## 📂 Suggested Project Structure

```text
shopping-project/
│
├── shopping.py
└── README.md
```

---

## 🎯 Project Goal

The main goal of this project is to practice **Python programming concepts**, including:

- Variables
- Strings
- Integers
- User input
- Conditional statements
- Functions
- Lists and dictionaries
- Arithmetic operations
- Shopping basket management
- Basic payment processing

---

## 👨‍💻 Author

**Zakkariya Hassan**

---

## 📄 License

This project was created for **educational and learning purposes**.#
