from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
        
    def getStatus(self, traiNo, fro, to):
        print(f"Train no: {self.trainNo} from {fro} to {to} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

t = Train(12374)
t.book("Rampur", "Delhi")
t.getStatus((),"Rampur", "Delhi")
t.getFare("Rampur", "Delhi")


