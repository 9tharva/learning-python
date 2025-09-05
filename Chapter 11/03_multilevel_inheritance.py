class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Maneger(Programmer):
    c = 3

o = Maneger()
print(o.a, o.b, o.c)