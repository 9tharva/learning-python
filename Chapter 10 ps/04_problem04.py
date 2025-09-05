class Calculator:
    def __init__(self, n):
        self.n = n
        print("hello there!")

    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello there")

a = Calculator(4)
a.hello()  # we can print it in init
a.square()
a.cube()
a.squareroot()