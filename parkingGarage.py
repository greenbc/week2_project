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

runGarage()   