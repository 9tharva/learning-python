class Employee:
    language = "py"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Goodmorning")

harry = Employee()
harry.name = "Harry hirapav"
harry.language = "java"

harry.greet()
harry.getInfo()   #Employee.getInfo(harry)
