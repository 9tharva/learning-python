class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer("Atharva", 200000, 38665)
print(a.name, a.salary, a.pin, a.company)
v = Programmer("Vaishnavi", 3900000, 34083)
print(v.name, v.salary, v.pin, v.company )