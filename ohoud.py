class Artwork:
    def __init__(self, title="", artist="", date_created=None, significance=""):
        self.title = title
        self.artist = artist
        self.date_created = date_created
        self.significance = significance

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setArtist(self, artist):
        self.artist = artist

    def getArtist(self):
        return self.artist

    def setDateCreated(self, date_created):
        self.date_created = date_created

    def getDateCreated(self):
        return self.date_created

    def setSignificance(self, significance):
        self.significance = significance

    def getSignificance(self):
        return self.significance

class Ticket:
    def __init__(self, ticketID=0, price=0.0, ticket_type="", availability=False):
        self.ticketID = ticketID
        self.price = price
        self.ticket_type = ticket_type
        self.availability = availability

    def setTicketID(self, ticketID):
        self.ticketID = ticketID

    def getTicketID(self):
        return self.ticketID

    def setTicketType(self, ticket_type):
        self.ticket_type = ticket_type

    def getTicketType(self):
        return self.ticket_type

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setAvailability(self, availability):
        self.availability = availability

    def getAvailability(self):
        return self.availability

class Exhibition:
    def __init__(self, name="", start_date=None, end_date=None, location=""):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setStartDate(self, start_date):
        self.start_date = start_date

    def getStartDate(self):
        return self.start_date

    def setEndDate(self, end_date):
        self.end_date = end_date

    def getEndDate(self):
        return self.end_date

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

class Visitor:
    def __init__(self, visitorID=0, name="", age=0, nationality=""):
        self.visitorID = visitorID
        self.name = name
        self.age = age
        self.nationality = nationality

    def setVisitorID(self, visitorID):
        self.visitorID = visitorID

    def getVisitorID(self):
        return self.visitorID

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def setNationality(self, nationality):
        self.nationality = nationality

    def getNationality(self):
        return self.nationality

class ExhibitionLocation:
    def __init__(self, locationID=0, name="", type=""):
        self.locationID = locationID
        self.name = name
        self.type = type

    def setLocationID(self, locationID):
        self.locationID = locationID

    def getLocationID(self):
        return self.locationID

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

class Tour:
    def __init__(self, tourID=0, date=None, group_size=0, guide=""):
        self.tourID = tourID
        self.date = date
        self.group_size = group_size
        self.guide = guide

    def setTourID(self, tourID):
        self.tourID = tourID

    def getTourID(self):
        return self.tourID

    def setDate(self, date):
        self.date = date

    def getDate(self):
        return self.date

    def setGroupSize(self, group_size):
        self.group_size = group_size

    def getGroupSize(self):
        return self.group_size

    def setGuide(self, guide):
        self.guide = guide

    def getGuide(self):
        return self.guide

# Create instances of classes
artwork = Artwork()
ticket = Ticket()
exhibition = Exhibition()
visitor = Visitor()
exhibition_location = ExhibitionLocation()
tour = Tour()

# Set values for each object
artwork.setTitle("The Starry Night")
artwork.setArtist("Vincent van Gogh")
artwork.setDateCreated("1889-06-01")
artwork.setSignificance("One of van Gogh's most famous paintings.")

ticket.setTicketID(12345)
ticket.setPrice(25.99)
ticket.setTicketType("General Admission")
ticket.setAvailability(True)

exhibition.setName("Impressionist Art Exhibit")
exhibition.setStartDate("2024-05-15")
exhibition.setEndDate("2024-08-15")
exhibition.setLocation("Metropolitan Museum of Art")

visitor.setVisitorID(9876)
visitor.setName("Ohoud")
visitor.setAge(18)
visitor.setNationality("Emarati")

exhibition_location.setLocationID(54321)
exhibition_location.setName("Gallery Hall")
exhibition_location.setType("Gallery")

tour.setTourID(6745)
tour.setDate("2024-07-21")
tour.setGroupSize(15)
tour.setGuide("Medeya")

# Displaying details of the objects
print("Artwork Details:")
print("Title:", artwork.getTitle())
print("Artist:", artwork.getArtist())
print("Date Created:", artwork.getDateCreated())
print("Significance:", artwork.getSignificance())

print("\nTicket Details:")
print("Ticket ID:", ticket.getTicketID())
print("Price:", ticket.getPrice())
print("Type:", ticket.getTicketType())
print("Availability:", ticket.getAvailability())

print("\nExhibition Details:")
print("Name:", exhibition.getName())
print("Start Date:", exhibition.getStartDate())
print("End Date:", exhibition.getEndDate())
print("Location:", exhibition.getLocation())

print("\nVisitor Details:")
print("Visitor ID:", visitor.getVisitorID())
print("Name:", visitor.getName())
print("Age:", visitor.getAge())
print("Nationality:", visitor.getNationality())

print("\nExhibition Location Details:")
print("Location ID:", exhibition_location.getLocationID())
print("Name:", exhibition_location.getName())
print("Type:", exhibition_location.getType())

print("\nTour Details:")
print("Tour ID:", tour.getTourID())
print("Date:", tour.getDate())
print("Group Size:", tour.getGroupSize())
print("Guide:", tour.getGuide())

