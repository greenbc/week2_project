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
            print("ticket has been paid and you may leave")

    def leaveGarage(self, ticketNum):
        if self.currentTicket[int(ticketNum)] == 'paid':
            print("Thank you, have a nice day")
            self.tickets.append(int(ticketNum)) 
            self.parkingSpaces.append(int(ticketNum))
            self.tickets.sort()
            self.parkingSpaces.sort()
        else:
            print("Must pay first")

tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parkingSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
currentTicket = {}

garage = ParkingGarage(tickets, parkingSpaces, currentTicket)

def runGarage():
    while True:
        value = input("Would you like to park/pay or leave?: ")
        if value.lower() == "park":
            if tickets != []:
                ticketNum = tickets[0]
                garage.takeTicket(ticketNum)
                clear_output()
                print("Parking available:")
                print(tickets)
            else:
                clear_output()
                print("No parking available")
        elif value.lower() == "pay":
            clear_output ()
            pay = input("What parking space would you like to pay for?: ")
            garage.payForParking(pay)
        elif value.lower() == "leave":
            clear_output()
            ticketNum = input("What is your ticket number?: ")
            garage.leaveGarage(ticketNum)
            print("Parking available:")
            print(tickets)
        else:
            clear_output()
            print("Command not recognized")

runGarage()   