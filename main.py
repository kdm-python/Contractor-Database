import csv
import datetime as dt
from os.path import exists
import pickle

import client
import job

###########################
### CONTRACTOR DATABASE ###
###########################

# MAIN MODULE

# TO START WITH:
# ASSUME ALL CLIENTS ARE INDIVIDUAL TENANTS OR HOMEOWNERS WITH A SINGLE PROPERTY
# ASSUME EACH JOB HAS ONE PROPERTY AND VICE VERSA. LATER JOB/INVOICE/CLIENT CAN HAVE MULTIPLE PROPS

# NOT USING INHERITED CLASSES FOR PROPERTIES AND CLIENTS YET
# GET WORKING WITH SINGLE CLASSES, THEN EXPAND

### DATA IMPORTING/EXPORTING TO FILES

def readCSV(filePath):
    try:
        with open(filePath, 'r') as r:
            csv_reader = csv.reader(r)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        f'{filePath} not found.'

def exportNewCSV(filePath, keys, *objects):
    """*objects = 1 or more objects. keys = list of keys, filePath = chosen file name.
    Check if file exists first. All object types should have a toCSV() method so this function
    can be used on any object collection.
    PROBLEM: NEED TO EXTRACT CLASS ATTR FROM TYPE OF THE OBJECT"""
    if len(objects) == 0:
        raise Exception('You have not supplied any objects to extract.')

    print(f'csv keys: {keys}')
    print(f'writing {len(objects)} to file...')
    if exists(filePath):
        print(f'{filePath} already exists.')
    else:
        with open(filePath, 'w', newline='') as w:
            csvWriter = csv.writer(w)
            csvWriter.writerow(keys)
            for i in objects:
                csvWriter.writerow(i.getCSV())
        print(f'{filePath} successfully written.')

def amendExistingCSV(filePath, *objects):
    """Check file exists, then write each row"""
    if len(objects) == 0:
        raise Exception('You have not supplied any objects to extract.')

    if not exists(filePath):
        print(f'{filePath} not found.')
    else:
        with open(filePath, 'a', newline='') as a:
            csvWriter = csv.writer(a)
            for i in objects:
                csvWriter.writerow(i.getCSV())

def unpickleObject(file_name):
    """Read file, return list of unpickled objects"""
    with open(file_name, 'rb') as r:
        while True:
            try:
                yield pickle.load(r)
            except EOFError:
                break

def pickleNewFile(file_name, *objects):
    """Create one or more pickle objects, write to file.
    ALTERNATIVE: CREATE LIST ELSEWHERE AND PICKLE JUST THAT.
    THEN CAN FEED BACK IN AS LIST."""
    # exists? try-except
    with open(file_name, 'wb') as p:
        pick = map(pickle.dumps, objects)
        for x in pick:
            p.write(x)

### TESTING ###

clients = []

jobs = []
# use later:
current_jobs = []
past_jobs = []

invoices = []
# use later:
current_invoices = []
past_invoices = []

properties = []

def clientTest():
    """The main creation function needs to create addresses, properties and clients at the same time. """
    clients.extend(unpickleObject('Clients.pickle'))
    for i in clients:
        print(i)
    # client1 = client.Client('Kyle', 'Marden', '07930 548077', '12 George Close', 'Coventry', 'County',
    #                         'CV2 X3Y', 'Lawyer', 'Nice dude, hot wife.')
    #
    # client2 = client.Client('John', 'Smith', '07755 548997', '19 George Street', 'Kingston', 'Surrey',
    #                         'KT12 4HY', 'Lawyer', 'Total prick but lots of business here.')
    #
    # client3 = client.Client('George', 'Harris', '07643 599786', '12 George Close', 'Coventry', 'County',
    #                         'CV2 X3Y', 'Accountant', 'Might have more properties')
    #
    # clients.extend([client1, client2, client3])
    #
    # for i in clients:
    #     print(f'{i}\n')
    # print()

    # pickleNewFile('clients.pickle', client1, client2, client3)

    ### pickle the objects
    ### create some new properties using functions from client module

clientTest()

def jobTest():
    print('### GENERATING JOBS ###')
    print(clients)
    job1 = job.BoilerChange(clients[0], dt.date(2022, 2, 26), dt.date(2022, 2, 28),
                            5000, 'Model C: Broken')

    job2 = job.BoilerChange(clients[1], dt.date(2022, 3, 1), dt.date(2022, 3, 2),
                            2500, 'Old model, totally gone')

    job3 = job.GasCert(clients[2], dt.date(2022, 3, 1), dt.date(2022, 3, 2),
                       2500, 'Model C: Broken')

    # job4 = job.GasCert(clients[3], 'home property', dt.date(2022, 3, 1), dt.date(2022, 3, 2),
    #                    2500, 'Model C: Broken')

    jobs.extend([job1, job2, job3])

    for j in jobs:
        print(j)

    print('\n### GENERATING INVOICES ###')
    job1_inv = job1.makeInvoice(dt.date(2022, 1, 5), dt.date(2022, 3, 10))
    job2_inv = job2.makeInvoice(dt.date(2022, 1, 5), dt.date(2022, 3, 10))
    job3_inv = job3.makeInvoice(dt.date(2022, 3, 8), dt.date(2022, 4, 8))
    invoices.extend([job1_inv, job2_inv, job3_inv])

    print('Current invoices: ')
    for i in invoices:
        print(i, '\n')
    print()

    print('\n# Make a new CSV file of invoices #')
    inv_keys = job.Invoice.csv_keys
    exportNewCSV('invoices.csv', inv_keys, job1_inv, job2_inv)
    print('# Amend existing file #')
    amendExistingCSV('invoices.csv', job3_inv)
    print(f'# read back in existing file #')
    readCSV('invoices2.csv')
    readCSV('invoices.csv')

# jobTest()

def invoiceTest():
    """Would want functionality to work with the invoices alone."""
    pass

def clientMenu():
    """List the functions that need to be performed on clients."""
    def loadExisting():
        pass

    def exportNew():
        pass

    def addClient():
        pass

    def delClient():
        pass

    def searchClients(category, search_term):
        """Search for name, phone, anything."""
        pass

    def displayAll():
        pass

    def amendDetails(cl, attribute):
        """Change details of chosen client."""
        pass