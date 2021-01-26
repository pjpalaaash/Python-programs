class Train:
    #trainNo = 11464
    seats = 500
    def __init__(self,name):
        print(f"**************{name}*****************")

    def tickets(self):
        print("Ticket booked successfully........")
        self.seats = self.seats - 1
        #print(f"Seats left {self.seats} " )


a = input("Enter train name bc....: ")

t = Train(a)
ex = None
while ex != "e":
    choose = int(input("press 1 for ticket booking and 0 for Checking seats left: "))

    if choose == 1:
        t.tickets()
        ex = (input('''press "e" for exit and "m" for menu....: '''))
    elif choose == 0:
        print(t.seats)
        ex = (input('''press "e" for exit and "m" for menu....: '''))
    else:
        print("Wrong entry....!!")        
        ex = (input('''press "e" for exit and "m" for menu....: '''))

print("Thankyou for visiting bruhhh..............!!!!!!!!!!!")
    