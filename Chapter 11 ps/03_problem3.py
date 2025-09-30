class Employee:
    salary = 234
    increment = 28

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # Calculate increment percentage based on new salary
        self.increment = ((new_salary / self.salary) - 1) * 100


e = Employee()
e.salaryAfterIncrement = 280.8
print(e.increment)

