#File for test cases: Test_Cases.py
#importing the classes from the file Museum_Code.py
from Museum_Code import Artwork, Exhibition, Visitor, Ticket, TourTicket, SpecialEventsTicket
from Museum_Code import Gender, ExhibitLocation, Purpose, TicketPurchase

#Creating Objects
#Adding an artwork
print("New Artwork Added:")
newArtwork = Artwork("Self-portrait", "Vincent Van Gogh", "1889", "Significant, showcasing his unique artwork style", ExhibitLocation.PermanentGallery)
newArtwork.displayArtwork()
print(" ") #Adding an empty line for spacing between objects

#Opening a new exhibition
print("New Exhibition Opening")
newExhibition = Exhibition("Nature Art Exhibition", "Nature", "1 Month")
newExhibition.dispalyExhibition()
print(" ") #Adding an empty line for spacing between objects

#Creating visitor 1 as an object, creating the student ticket, and displaying its details
visitor1 = Visitor("Fatma", 20, Gender.Female, "Student", TicketPurchase.Online)
individualTicketPrice = Ticket.purchaseTicket(visitor1, "Student")  # Purchase regular ticket
individualTicket = Ticket(individualTicketPrice, "B5322", "30/03/2024", "09:00", visitor1)
individualTicket.displayTicket()
print(" ") #Adding an empty line for spacing between objects

#Creating visitor 2 as an object, creating the group ticket, and displaying its details
visitor2 = Visitor("Aisha", 30, Gender.Female, "Group", TicketPurchase.Online)
groupTicketPrice = Ticket.purchaseTicket(visitor2, "Group")  # Purchase regular ticket
groupTicketPrice = Ticket(groupTicketPrice, "E5786", "11/04/2024", "11:00", visitor2)
groupTicketPrice.displayTicket()
print(" ") #Adding an empty line for spacing between objects

#Creating visitor 3 as an object, creating the regular ticket, and displaying its details
visitor3 = Visitor("Zayed", 26, Gender.Male, "Regular", TicketPurchase.InPerson)
regularTicketPrice = Ticket.purchaseTicket(visitor3, "Regular")  # Purchase regular ticket
regularTicketPrice = Ticket(regularTicketPrice, "A9857", "06/07/2024", "14:00", visitor3)
regularTicketPrice.displayTicket()
print("") #Adding an empty line for spacing between objects

#Creating Tour Ticket as an object for visitor 4 and displaying its details
visitor4 = Visitor("Omar", 23, Gender.Male, "Regular", TicketPurchase.InPerson)
tourTicket = TourTicket(70, "G3960", "02/06/2024", "16:00", visitor4, 20, "Amna", "3 hours")
tourTicket.displayTourTicket()

print("") #Adding an empty line for spacing between objects
#Creating Special Events Ticket Ticket as an object for visitor 4 and displaying its details
specialEvTicket = SpecialEventsTicket("85", "C4652", "03/07/2024", "12:00", visitor4, Purpose.LightShow, "2 hours", "Classic Art Exhibition")
specialEvTicket.displaySpecialEvents()
