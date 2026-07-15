# 🏦 Banking Management System

## About the Project

This is a simple Banking Management System that I built while learning Object-Oriented Programming (OOP) in Python.

The main goal of this project was to understand how **Hybrid Inheritance** works in a real-world scenario. Instead of using basic examples like animals or vehicles, I wanted to create something that models an actual banking system.

The project contains four classes:

- User
- Customer
- Employee
- BankManager

The `BankManager` class inherits from both `Customer` and `Employee`, making this a good example of **Hybrid Inheritance** in Python.

---

## Concepts Practiced

During this project, I practiced:

- Classes and Objects
- Constructors (`__init__`)
- Single Inheritance
- Multiple Inheritance
- Hybrid Inheritance
- Method Reuse
- Constructor Chaining
- Object-Oriented Design

---

## Project Structure

```text
                 User
               /      \
              /        \
        Customer      Employee
              \        /
               \      /
            BankManager
```

---

## Features

- Display user, customer, and employee information
- Deposit money into an account
- Withdraw money from an account
- Approve loans
- Display complete bank manager details
- Demonstrates Hybrid Inheritance using a practical example

---

## Sample Output

```text
Name: Basil
Email: basil@123gmail.com
Phone: 03352606613

Account Number: 2335
Account Type: Saving
Balance: 10000

Employee ID: 22
Department: HR
Salary: 5000

Branch: Defence
Experience: 15
```

---

## What I Learned

While building this project, I gained a much better understanding of:

- How multiple inheritance works in Python.
- How a child class can access methods from different parent classes.
- Constructor chaining between parent and child classes.
- Common mistakes such as forgetting `self` while calling parent constructors.
- Updating object data using methods like `deposit()` and `withdraw()`.

This project also helped me understand Python's inheritance hierarchy much better through hands-on practice.

---

## Future Improvements

Some features I plan to add in the future are:

- Transaction history
- Money transfer between accounts
- PIN authentication
- File or database storage
- Exception handling for invalid input
- Graphical User Interface (GUI)

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## Author

**Basil Khan**

This project is part of my Python learning journey as I continue building practical projects and improving my software development skills.
