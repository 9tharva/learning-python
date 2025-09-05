class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Employee")
    b = 2

class Maneger(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Employee")
    c = 3

o = Maneger()
print(o.a, o.b, o.c)