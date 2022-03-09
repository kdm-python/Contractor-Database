import datetime as dt

###########################
### CONTRACTOR DATABASE ###
###########################

# JOB MODULE

# a Job is composed of a client, property and start/end dates

class Job:
    """Represents a job to be done or already done.
    PROBLEM: THIS NEEDS TO BE LINKED TO A HOME PROPERTY OR AN OTHER PROPERTY
    FROM CLIENT - HOW TO DIFFERENTIATE?
    TO BEGIN WITH, ASSUME PROPERTY ADDRESS IS CLIENT'S HOME ADDRESS"""
    jobID = 201

    def __init__(self, client, dateStart, dateEnd, quote, notes):
        """Subtract dates to get number of days to complete.."""
        self.client = client  # Client object
        # self.property = prop  # str for test, Property object later
        self.notes = notes  # str
        self.quote = quote
        self.dateStart = dateStart  # date object
        self.dateEnd = dateEnd  # date object
        # self.timeToFinish = dateEnd - dateStart  # store number of days
        self.finished = False  # is job finished or not, default to False
        self.hasInvoice = False
        self.invoice = None  # Invoice objects
        self.id = Job.jobID  # this will need to examine existing data for current ID count
        Job.jobID += 1
        # add pictures

    def getID(self):
        return self.id

    def getClient(self):
        """Return a Client object."""
        return self.client

    def displayClient(self):
        """NOT SURE IF THIS IS NEEDED? RETURN STRING INSTEAD OF CLIENT OBJECT?"""
        print(f'*** Client for job {self.id} ***\n{self.client.getFullName}')
        # not sure whether need this return statement?
        # since Client object can be accessed directly using getClient()
        return f'*** Client for job {self.id} ***\n{self.client.getFullName}'

    def getJobAddress(self):
        return self.client.getHomeAddress()

    def getQuote(self):
        """Return list of past and present quotes."""
        return self.quote

    def changeQuote(self, newQuote):
        """Assign float value charge and datetime date to a newly created Quote object.
        Add Quote object to self's quotes list."""
        self.quote = newQuote

    def makeInvoice(self, dateIssued, dateDue):
        """Generate Invoice object. Assign to self, change hasInvoice to True. """
        # automatically generate one-month due date
        newInvoice = Invoice(self.client, self, self.quote, dateIssued, dateDue)
        self.invoice = newInvoice
        self.hasInvoice = True
        return newInvoice

    def getInvoice(self):
        """Return each invoice connected to this job."""
        if not self.invoice:
            print(f"Job {self.id} hasn't been invoiced yet.")
        else:
            return self.invoice

    def finishJob(self):
        """Set the job as completed. Other functionality added soon."""
        self.finished = True

    def __str__(self):
        """Property object name later, just a string placeholder for now.
        Need to represent the Job in plain english using jobName class attributes below, if possible."""
        if not self.hasInvoice:
            invoiced = 'NO'
        else:
            invoiced = 'YES'

        return f'ID: {self.id} Job type: {type(self).__name__}\nClient: {self.client.getFullName()}\n' \
               f'* PROPERTY *\n{self.client.getHomeAddress}\nStart date: {self.dateStart} End date: {self.dateEnd}\n' \
               f'Quote: £{self.getQuote()} Invoiced?: {invoiced}'
        # WILL ADD FUNCTIONALITY TO RETRIEVE QUOTES AND JOB/CLIENT FURTHER DETAILS

### HOME JOB NAD LANDLORD JOB CLASSES???
# e.g.

class HomeJob(Job):
    pass

class LandlordJob(Job):
    pass

class BoilerRepair(Job):
    """How do I pass jobName into the __str__ method above, without
    having to override __str__ here?"""
    jobName = 'Boiler Repair'
    # boiler model, what problem is, etc

class GasCert(Job):
    jobName = 'Gas Certificate'
    # last certificate date

class Service(Job):
    pass

class CookerInstall(Job):
    pass

class BoilerChange(Job):
    pass

class EmergencyJob(Job):
    pass

class Invoice:
    invoiceID = 301
    csv_keys = ['Invoice ID', 'Job ID', 'Client ID', 'Job Type', 'paid?', 'Total', 'Balance']

    def __init__(self, client, job, amount, dateIssued, dateDue):
        self.client = client  # associated client object
        self.job = job  # associated job object
        self.amount = amount
        self.balance = amount
        self.dateIssued = dateIssued
        self.dateDue = dateDue
        self.isPaid = False
        self.csv_keys = Invoice.csv_keys
        self.id = Invoice.invoiceID
        Invoice.invoiceID += 1

    def invoicePaid(self):
        """Mark this invoice as paid."""
        self.isPaid = True
        self.balance = 0

    def lowerBalance(self, payment):
        """If part payment is made."""
        self.balance -= payment

    def getKeys(self):
        return self.csv_keys

    def getCSV(self):
        """Create a row of values to insert into a CSV file."""
        if not self.isPaid:
            paid = 'NOT PAID'
        else:
            paid = 'PAID'
        newRow = [self.id, self.job.getID(), self.client.getID(), type(self.job).__name__, paid,
                  f'£{self.amount}', f'£{self.balance}']
        return newRow
        # ADD TO EXISTING CSV HERE OR ELSEWHERE?

    def __str__(self):
        return f'JOB ID: {self.job.getID()}\nCLIENT: {self.client.getFullName()}\n{self.client.getHomeAddress()}\n' \
               f'DATE ISSUED: {self.dateIssued}\nAMOUNT DUE: £{self.amount}\nBALANCE REMAINING: {self.balance}'

def getClientJob(job):
    print(f'Client for Job {job.getID()}: {job.getClient().getFullName()}')

# class Quote:
#     """A job could have multiple quotes attached."""
#     quoteID = 501
#
#     def __init__(self, job, charge, dateQuoted):
#         self.job = job  # Job object
#         self.charge = charge  # float
#         self.dateQuoted = dateQuoted  # str to test, datetime module later
#
#     def __lt__(self, other):
#         """Return True if this quote is lower than another."""
#         return self.charge < other.charge
#
#     def __gt__(self, other):
#         """Return True if this quote is greater than another."""
#         return self.charge > other.charge
#
#     def getCharge(self):
#         return self.charge
#
#     def __str__(self):
#         return f'Job ID: {self.job.getID()}\nQuote: {self.charge}\nDate: {self.dateQuoted}'

