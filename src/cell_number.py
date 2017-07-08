""" the CellNumber class represents one phone (or, SIM card) with a unique
number that can be used by a person """

import random

from utils import phone_number_generator
from config import end_time, num_cells

random_phone_number = phone_number_generator()

class CellNumber():
    """ Describes a single cell number, which (usually) has a number of call
    records associated with it. A person could have one number, or more """

    def __init__(self, person):
        self.uuid = next(random_phone_number)
        self.person = person
        self.call_records = []

    def generateRecords(self, cell_numbers):
        for hour in range(end_time):
            if random.random() < 1/self.person.cell_usage:
                # they made a call/texted/etc. in this hour
                self.generateRecord(hour, cell_numbers)

    def generateRecord(self, time, cell_numbers):
        """ generates a call record from a random location to a random contact
        at a specified time """

        # choose a location
        if random.random() < self.person.cell_regularity:
            # in one of their cells
            location = random.choice(self.person.cells)
        else:
            # outside of one of their usual cells
            location = random.randrange(num_cells)

        # choose a contact
        if random.random() < self.person.contact_regularity:
            # calling a regular contact
            contact = random.choice(self.person.contacts)
        else:
            # venturing to call someone totally new
            contact = random.choice(cell_numbers)

        # assemble call record, store in self.call_records
        self.call_records.append({
            'cell':location,
            'from': self.uuid,
            'to': contact.uuid,
            'time': time
            })

