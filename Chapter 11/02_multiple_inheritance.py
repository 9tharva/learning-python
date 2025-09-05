class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    languages = "python"
    def printlanguages(self):
        print(f"Out of all the languages here is your language: {self.languages}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"the name is {self.company} and he is good with {self.languages} language")
    
a = Employee()
b = Programmer()

b.show()
b.printlanguages()
b.showLanguage()