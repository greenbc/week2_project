from IPython.display import clear_output

class ParkingGarage():

    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket

    def takeTicket(self, ticketNum):
        self.currentTicket[ticketNum] = ''
        self.tickets.remove(ticketNum)
        self.parkingSpaces.remove(ticketNum)

    def payForParking(self, payTicket):
        self.payTicket = payTicket
        value = input("Please press any key to pay: ")
        if value is not None:
            self.currentTicket[payTicket] = "paid"
            self.tickets.append(int(payTicket)) 
            self.parkingSpaces.append(int(payTicket))
            self.tickets.sort()
            self.parkingSpaces.sort()
            print("ticket has been paid and you may leave")



tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
currentTicket = {}

garage = ParkingGarage(tickets, parkingSpaces, currentTicket)

def runGarage():
    while True:
        value = input("Would you like to park/pay or leave?: ")
        if value == "park":
            if tickets != []:
                ticketNum = tickets[0]
                garage.takeTicket(ticketNum)
                clear_output()
                print("Parking available:")
                print(tickets)
            else:
                clear_output()
                print("No parking available")
        elif value == "pay":
            clear_output ()
            pay = input("What parking space would you like to pay for?: ")
            garage.payForParking(pay)

runGarage()   