class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # Initial email assignment (not dynamic, just stored once)
        self._email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

 
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter
    def email(self, string):
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

basil = Employee("basil", "ahmed")
ali = Employee("ali", "khan")

print(basil.explain())       # "This employee is basil ahmed"
print(basil.email)           # Uses @property → "basil.ahmed@gmail.com"

basil.fname = "basu"
print(basil.email)           # Property reflects updated fname → "basu.ahmed@gmail.com"

basil.email = "new.name@gmail.com"  # Calls @setter → updates fname & lname
print(basil.email)           # "new.name@gmail.com"

del basil.email              # Calls @deleter → resets fname & lname
print(basil.explain())       # "This employee is None None"
