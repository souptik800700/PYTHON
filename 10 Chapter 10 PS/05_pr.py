from random import randint

class Train:
    def book(self, trainNo, fro, to):

        print(f"Ticket is booked in train no: { trainNo}  {fro} {to}")
    def getstatus(self, trainNo):
        print(f"Ticket is booked in train no: { trainNo} on time")
    def getFare(self, trainNo, fro, to):
        print(f"Ticket fare in train no: {trainNo} from {fro} to {to} is {randint(222,5555)}")

t = Train()
t.book(13399, "rampur", "Delhi")
t.getFare("rampur", "dj", "dj")