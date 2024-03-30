#Code File Name: Museum_Code.py
#Importing Enum class from the enum python module
from enum import Enum
#Using an enumerator class for purpose (Fundraising, Musical, Concert, Light Show)
class Purpose(Enum):
    Fundraising = "Fundraising"
    Musical = "Musical"
    Concert = "Concert"
    LightShow = "Light Show"

#Using an enumerator class for gender (Male, Female)
class Gender(Enum):
    Male = "Male"
    Female = "Female"

#Using an enumerator class for exhibit location (permanent gallery,exhibition hall, outdoor spaces)
class ExhibitLocation(Enum):
    PermanentGallery = "Permanent Gallery"
    ExhibitionHall = "Exhibition Hall"
    OutdoorSpaces = "Outdoor Spaces"

#Using an enumerator class for ticket purchase method (Online, In Person)
class TicketPurchase(Enum):
    Online = "Online Purchase"
    InPerson = "In Person Purchase"

class Artwork:
    """Class to represent an Artwork"""
    # Using initializing constructor to initialize attributes of Artwork class
    def __init__(self, title, artist, creationDate, histSignificance, exhibitLoc):
        #Initializing attributes
        self.__title = title
        self.__artist = artist
        self.__creationDate = creationDate
        self.__histSignificance = histSignificance
        self.__exhibitLoc = exhibitLoc

    # Implementing setter and getter functions for Artwork class attributes
    def set_title(self, title):
        self.__title = title
    def get_title(self):
        return self.__title

    def set_artist(self, artist):
        self.__artist = artist
    def get_artist(self):
        return self.__artist

    def set_creationDate(self, creationDate):
        self.__creationDate = creationDate
    def get_creationDate(self):
        return self.__creationDate

    def set_histSignificance(self, histSignificance):
        self.__histSignificance = histSignificance
    def get_histSignificance(self):
        return self.__histSignificance

    def set_exhibitLoc(self, exhibitLoc):
        self.__exhibit_loc = exhibitLoc
    def get_exhibitLoc(self):
        return self.__exhibitLoc

    #Display Artwork Details
    def displayArtwork(self):
        print("Title:", self.__title)
        print("Artist:", self.__artist, " - Creation Date:", self.__creationDate)
        print("Historical Significance:", self.__histSignificance)
        print("Exhibit Location:", self.__exhibitLoc.value)

class Exhibition:
    """Class to represent an Exhibition"""
    # Using initializing constructor to initialize attributes of Exhibition class
    def __init__(self, exhibitName, theme, duration):
        #Initializing attributes
        self.__exhibitName = exhibitName
        self.__theme = theme
        self.__duration = duration
        #This represents aggregation between Artwork and Exhibition classes
        self.artworks = [] #aggregation

    #Adding artwork to the exhibition
    def add_artwork(self, artwork):
        self.artworks.append(artwork)

    # Implementing setter and getter functions for Exhibition class attributes
    def set_exhibitName(self, exhibitName):
        self.__exhibitName = exhibitName
    def get_exhibitName(self):
        return self.__exhibitName

    def set_theme(self, theme):
        self.__theme = theme
    def get_theme(self):
        return self.__theme

    def set_duration(self, duration):
        self.__duration = duration
    def get_duration(self):
        return self.__duration

    #Display Exhibition Details
    def dispalyExhibition(self):
        print("Exhibition Name:", self.__exhibitName)
        print("Theme:", self.__theme)
        print("Duration:", self.__duration)

class Visitor:
    """Class to represent a Visitor"""
    # Using initializing constructor to initialize attributes of Visitor class
    def __init__(self, name, age, gender, ticketType, ticketPurchase):
        #Initializing attributes
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__ticketPurchase = ticketPurchase
        self.__ticketType = ticketType

    # Implementing setter and getter functions for Visitor class attributes
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age
    def get_age(self):
        return self.__age

    def set_gender(self, gender):
        self.__gender = gender
    def get_gender(self):
        return self.__gender

    def set_ticketPurchase(self, ticketPurchase):
        self.__ticketPurchase = ticketPurchase
    def get_ticketPurchase(self):
        return self.__ticketPurchase

    def set_ticketType(self, ticketType):
        self.__ticketType = ticketType
    def get_ticketType(self):
        return self.__ticketType

    #Display Visitor Information
    def displayVisitor(self):
        print("Visitor Name:", self.__name, "Age:", self.__age)
        print("Gender:", self.__gender.value)
        print("Ticket Purchase", self.__ticketPurchase.value)
        print("Ticket Type:", self.__ticketType)

#Parent Class
class Ticket:
    """Class to represent a Ticket"""
    # Using initializing constructor to initialize attributes of Ticket class
    def __init__(self, price, ticketID, date, time, visitor):
        # Initializing attributes
        self._price = price
        self._ticketID = ticketID
        self._date = date
        self._time = time
        #This represents composition between Visitor and Ticket classes
        self._visitor = visitor #composition

    # Implementing setter and getter functions for Ticket class attributes
    def set_price(self, price):
        self._price = price
    def get_price(self):
        return self._price

    def set_ticketID(self, ticketID):
        self._ticketID = ticketID
    def get_ticketID(self):
        return self._ticketID

    def set_date(self, date):
        self._date = date
    def get_date(self):
        return self._date

    def set_time(self, time):
        self._time = time
    def get_time(self):
        return self._time

    def set_visitor(self, visitor):
        self._visitor = visitor
    def get_visitor(self):
        return self._visitor

    #Calculate ticket price based on age and ticket type
    def purchaseTicket(visitor, event):
        #Setting initial price to 0
        price = 0
        #if the age is less than 18 or greater than 60 or they are a student or teacher
        if visitor.get_age() <= 18 or visitor.get_age() >= 60 or visitor.get_ticketType() == "Student" or visitor.get_ticketType() == "Teacher":
            # Price will be 0
            price = 0
        #else if the ticket type is group the price is 63 and then implements a 50% discount on it
        elif visitor.get_ticketType() == "Group":
            price = 63
            price *= 0.5
        #else if the age is between 18-60 or the ticket type is regular, then the price is 63 and implements 5% VAT on it
        elif 18 <= visitor.get_age() <= 60 or visitor.get_ticketType() == "Regular":
            price = 63
            price *= 1.05
        #returning the final ticket price
        return price

    #Display Ticket Information
    def displayTicket(self):
        print("Ticket Receipt:")
        print("Price:", self._price)
        print("Ticket ID:", self._ticketID)
        print("Date:", self._date, " - Time:", self._time)
        print("Visitor:", self._visitor.get_name(), " - Age:", self._visitor.get_age())

#Child Class
class TourTicket(Ticket):
    """Class to represent TourTicket as a child of Ticket class"""
    # Using constructor to initialize attributes of Tour Ticket class
    def __init__(self, price, ticketID, date, time, visitor, groupSize, guide, tourDuration):
        # Calling the constructor of the parent class
        Ticket.__init__(self, price, ticketID, date, time, visitor)
        # Initializing attributes
        self.__groupSize = groupSize
        self.__guide = guide
        self.__tourDuration = tourDuration

    # Implementing setter and getter functions for Tour Ticket class attributes
    def set_groupSize(self, groupSize):
        self.__groupSize = groupSize
    def get_groupSize(self):
        return self.__groupSize

    def set_guide(self, guide):
        self.__guide = guide
    def get_guide(self):
        return self.__guide

    def set_tourDuration(self, tourDuration):
        self.__tourDuration = tourDuration
    def get_tourDuration(self):
        return self.__tourDuration

    #Display Tour Ticket Details
    def displayTourTicket(self):
        print("Tour Ticket:")
        # Calling the display function from parent class to display its attributes
        Ticket.displayTicket(self)
        print("Group Size:", self.__groupSize)
        print("Guide Name:", self.__guide)
        print("Tour Duration:", self.__tourDuration)

#Child Class
class SpecialEventsTicket(Ticket):
    # Using constructor to initialize attributes of Special Events Ticket class
    def __init__(self, price, ticketID, date, time, visitor, purpose, duration, eventLocation):
        # Calling the constructor of the parent class
        Ticket.__init__(self, price, ticketID, date, time, visitor)
        self.__purpose = purpose
        self.__duration = duration
        self.__eventLocation = eventLocation

    # Implementing setter and getter functions for Special Events Ticket class attributes
    def set_purpose(self, purpose):
        self.__purpose = purpose
    def get_purpose(self):
        return self.__purpose

    def set_duration(self, duration):
        self.__duration = duration
    def get_duration(self):
        return self.__duration

    def set_eventLocation(self, eventLocation):
        self.__eventLocation = eventLocation
    def get_eventLocation(self):
        return self.__eventLocation

    #Display Special Events Ticket Details
    def displaySpecialEvents(self):
        print("Special Events Ticket:")
        # Calling the constructor of the parent class
        Ticket.displayTicket(self)
        print("Purpose:", self.__purpose.value)
        print("Event Duration:", self.__duration)
        print("Event Location:", self.__eventLocation)
