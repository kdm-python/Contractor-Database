###########################
### CONTRACTOR DATABASE ###
###########################

# PROPERTY MODULE

class Address:
    def __init__(self, street, city, county, postcode, street2=''):
        self.street = street
        self.street2 = street2  # optional
        self.city = city
        self.county = county
        self.postcode = postcode

    def getCity(self):
        return self.city

    def getCounty(self):
        return self.county

    def getPostcode(self):
        return self.postcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.county} {self.postcode}')
        return '\n'.join(lines)

class Property:
    """Represents a property connected to a Client and optionally
    connected to a Job. WILL I NEED A CLIENT ATTRIBUTE HERE TO LINK TO OBJECT?"""

    def __init__(self, address, bedrooms, value):
        self.address = address  # Address object
        self.bedrooms = bedrooms  # int
        self.value = value  # int

    def getAddress(self):
        return self.address

    def toCSV(self):
        pass

    def __str__(self):
        return f'{self.address}\nValue: {self.value}'

# expand into these later:

class Home(Property):
    """Represents property the Client lives in."""
    def __init__(self, address, bedrooms, value):
        super().__init__(address, bedrooms, value)

class Homeowner(Home):
    """A Home owned by the client."""
    def __init__(self, address, bedrooms, value):
        super().__init__(address, bedrooms, value)

class Tenant(Home):
    """A Home rented by the client."""
    def __init__(self, address, bedrooms, value):
        super().__init__(address, bedrooms, value)

class Letting(Property):
    """Represents a property that a Landlord is renting out."""
    def __init__(self, address, bedrooms, value):
        super().__init__(address, bedrooms, value)

### FUNCTIONS ###

def createAddress(street1, city, county, postcode):
    """Create new Address object to use in property creation."""
    newAddress = Address(street1, city, county, postcode)
    return newAddress

def createProperty(address, bedrooms, value):
    """Create new Property object repr client's home property."""
    newProperty = Home(address, bedrooms, value)
    return newProperty