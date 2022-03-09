###########################
### CONTRACTOR DATABASE ###
###########################

# CLIENT MODULE

# laying foundations: use string placeholder for jobs and properties: expand to classes later
# first store client details in database on their own

### put property and address classes here. Or link only this module to properties module
### a property and address link only to a client
### these will then be accessed from job <-> client <- property

### COULD ALSO IMPORT THE PROPERTY MODULE, LINK TO CLIENT AND MAIN??? OR JUST CLIENT
class Address:
    def __init__(self, street, city, county, postcode, street2=''):
        self.street = street
        self.street2 = street2  # optional
        self.city = city
        self.county = county
        self.postcode = postcode

    def getPostcode(self):
        return self.postcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f'{self.city}, {self.county} {self.postcode}')
        return '\n'.join(lines)

class Property:
    """Represents a property connected to a Client.
    HAVE INHERITED CLASSES FOR HOME PROPERTY AND OTHER PROPERTIES?"""

    def __init__(self, address, isHome):
        self.address = address  # Address object
        # isHome will be False if this property is different than client's home address.
        # most clients will have this as true
        # could be landlords default to False, home clients to True, etc
        self.isHome = isHome  # boolean

    def getAddress(self):
        return self.address

    def toCSV(self):
        pass

    def __str__(self):
        return f'{self.address}'

class HomeProperty(Property):
    pass

class OtherProperty(Property):
    pass

class Client:
    """Abstract class representing a client.
    Look for a module to represent dates"""
    clientID = 101  # will need to check stored client list later

    def __init__(self, firstName, lastName, phoneNo, street, city, county, postcode,
                 occupation, notes='No notes yet.'):
        """Optional notes added during client initialisation.
        Use strings in the lists to test functionality."""
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = f'{firstName} {lastName}'
        # assigning address object to client as their home address
        self.homeAddress = Address(street, city, county, postcode)
        self.homeProperty = Property(self.homeAddress, True)
        self.phoneNo = phoneNo  # str now, phone number module or object later
        self.occupation = occupation

        self.jobs = []  # one or many Job objects
        # THIS ONLY APPLIES TO LANDLORDS, NOT NEEDED IN ABSTRACT CLIENT CLASS:
        # self.otherProperties = []  # not including homeProperty
        self.invoices = []  # one or many Invoice objects
        self.notes = notes  # optional to add notes when creating client
        self.id = Client.clientID
        Client.clientID += 1
    # would i print text of invoices/props/jobs here or elsewhere?

    def getID(self):
        return self.id

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getFullName(self):
        return self.fullName

    def getHomeProperty(self):
        return self.homeProperty

    def getHomeAddress(self):
        return self.homeAddress

    def getPhoneNo(self):
        return self.phoneNo

    def getJobs(self):
        """Returns the list of Job objects."""
        return self.jobs

    def displayJobs(self):
        """Return string representation of all jobs for this client."""
        if len(self.jobs) == 0:
            return 'No jobs found for this client.'
        else:
            jobStr = ''
            for i in self.getJobs():
                jobStr += f'{str(i)}\n\n'
            return jobStr

    def addJob(self, *jobs):
        """Assumes job is Job object."""
        self.jobs.extend(jobs)

    ### THESE WILL BE IN LANDLORD CLASS:
    # def getProperties(self):
    #     """Return list of Property objects."""
    #     return self.otherProperties

    # def addProperty(self, street, city, county, postcode):
    #     """Assumes prop is Property object. Add other non-home property. Just address for now,
    #     more attributes like bedrooms and value later."""
    #     newAddress = Address(street, city, county, postcode)
    #     newProp = Property(newAddress, False)
    #     self.otherProperties.append(newProp)

    def setAddress(self, address):
        self.homeAddress = address

    def getInvoices(self):
        """Return list of Invoice objects."""
        return self.invoices

    def addInvoice(self, invoice):
        """Assumes invoice is Invoice object."""
        self.invoices.append(invoice)

    def __str__(self):
        """Perhaps a way to simplify the below."""
        return f'{self.id}: {self.fullName}\n* HOME ADDRESS *\n{self.homeAddress}\n{self.phoneNo}\n' \
               f'{type(self).__name__}\n{self.notes}\n* JOBS * \n{self.displayJobs()}'

class Tenant(Client):
    """Store info about tenant who rents a property. Default property creation
    to a Tenant property object."""
    pass

class Homeowner(Client):
    """Store info about client who owns their home to be worked on.
    Default property creation to a"""
    pass

class Landlord(Client):
    """CAN HAVE MULTIPLE PROPERTIES/ADDRESSES"""
    pass

### FUNCTIONS ###

def createClient(fName, lName, phone, occ, ownsHome, notes):
    """Return Client object based on above parameters."""
    if ownsHome:
        newClient = Homeowner(fName, lName, phone, occ, notes)
    else:
        newClient = Tenant(fName, lName, phone, occ, notes)

    return newClient

def searchPostcode(postcode, clients):
    """Can use any number of letters above. Use generator b/c could be big list.
    If no results, display message - how to?"""
    return (x for x in clients if postcode in x.getHomeAddress().getPostcode())

def searchFirstName(name, clients):
    """Assumes name is str and clients is a list of Client objects."""
    return (x for x in clients if name in x.getFirstName())

def searchLastName(name, clients):
    """Assumes name is str and clients is a list of Client objects."""
    return (x for x in clients if name in x.getLastName())

def searchPostcodeMore(postcode, clients):
    """Trying to figure out a way to display a message if no results using a generator."""
    gen = (x for x in clients if postcode in x.getAddress())
    if not list(gen):
        print(f'no results for {postcode}.')
    else:
        for i in gen:
            print(i)

def displayJobs(client):
    """Display all the jobs for specified client. Unsure if this
    should be within the Client class or not."""
    print(f'*** Jobs for {client.getFullName()} ***')
    for i, j in enumerate(client.getJobs(), start=1):
        print(f'{i}:\n{j}\n')