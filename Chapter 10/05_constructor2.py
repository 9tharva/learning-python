class Employee:
    language = "py"
    salary = 1200000

    def __init__(self, name, salary, language):#dunder method
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Goodmorning")

harry = Employee("Harry", 1300000, "java")
# harry.name = "Harry"
# harry.language = "java"

harry.greet()
print(harry.name, harry.salary)
harry.getInfo()   #Employee.getInfo(harry)