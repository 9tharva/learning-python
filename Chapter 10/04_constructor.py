class Employee:
    language = "py"
    salary = 1200000

    def __init__(self):      #dunder method
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Goodmorning")

harry = Employee()
harry.name = "Harry"
harry.language = "java"

harry.greet()
harry.getInfo()   #Employee.getInfo(harry)