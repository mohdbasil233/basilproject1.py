class User:
    def __init__(self,name,email,phone):
        self.name=name
        self.email=email
        self.phone=phone
    def show_user(self):
        print(f"Name:{self.name}\nEmail:{self.email}\nPhone:{self.phone}\n")

class Customer (User):
    def __init__(self,name,email,phone,account_number,account_type,balance):
        User.__init__(self,name,email,phone)
        self.account_number=account_number
        self.account_type=account_type
        self.balance=balance
    def deposit(self,amount):
        if amount>0:  
          self.balance+=amount
          print(f"Rs{amount} deposited in account\n ")
        else:
            print("invalid deposit amount\n")

    def withdraw(self,amount):
        if (amount<=0):
         print("invalid amount enetered\n")
        elif amount>self.balance:
             print("Insufficient Balance\n")
     
        else:
             self.balance-=amount
             print(f"Rs{amount} withdrawal from account\n")
    def show_customer(self):
        # super().show_user()
        print(f"AccountNumber:{self.account_number}\nAccountType:{self.account_type}\nBalance:{self.balance}\n")
  
class Employee(User):
    def __init__(self, name, email, phone,employee_id,department,salary):
        super().__init__(name, email, phone)
        self.employee_id=employee_id
        self.department=department
        self.salary=salary
    def approve_loan(self):
        print("Loan is approved sucessfully--")
    def show_employee(self):
        # super().show_user()
        print(f"Employeed ID:{self.employee_id}\nDepartment:{self.department}\nSalary:{self.salary}\n")
class BankManager(Customer,Employee):
    def __init__(self, name, email, phone, account_number, account_type, balance,employee_id,department,salary,branch_name,year_of_exp):
        Customer.__init__(self,name, email, phone, account_number, account_type, balance)
        Employee.__init__(self,name,email,phone,employee_id,department,salary)
        self.branch_name=branch_name
        self.year_of_exp=year_of_exp
    def display(self):
        self.show_user()
        self.show_customer()
        self.show_employee()
        print(f"Branch:{self.branch_name}\nExperience:{self.year_of_exp}\n")
bm=BankManager(
    "basil",
    "basil@123gmail.com",
    "123456789",
    2335,
    "saving",
    10000,
    22,
    "HR",
    5000,
    "Defence",
    15)
print("="*40)
print("        BANK MANAGER DEATILS")
print("="*40)
bm.display()


print("--Depositing--")
bm.deposit(5000)
print("--Withdrwing--")
bm.withdraw(1000)
print("Updated Sucessfully\n")

bm.display()
