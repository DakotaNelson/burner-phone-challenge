import uuid
import math
import random

from utils import clamp
from cell_number import CellNumber
""" the person class implements one cell-phone-using human, and attempts to
simulate their behavior - at least, a little. They can have one or more
phone numbers. """

from config import num_cells, num_people, end_time, change_numbers_every

class Person():
    """ a single person, who has one or more cell phones, each with a unique
    cell phone number """
    def __init__(self):
        # how can we uniquely identify them?
        self._uuid = uuid.uuid4()
        # NOTE using this would be cheating :)

        # number of contacts they usually call
        self.num_contacts = math.ceil(random.normalvariate(10, 3))
        self.num_contacts = clamp(self.num_contacts, 1, 200)

        # who do they usually call?
        self.contacts = []

        # how habitual are they in their contacts?
        # 1 = always contacts the same set of contacts
        # 0 = completely uniform random contact for each call
        self.contact_regularity = random.normalvariate(.95, .01)

        # how often do they call people?
        # mean of 3 = 1/3 chance for average person to make call any given hour
        self.cell_usage = random.normalvariate(3,.30)
        if self.cell_usage < 0:
            self.cell_usage = .001

        # number of locations they usually call from
        self.num_cells = math.ceil(random.normalvariate(10, 3))
        self.num_cells = clamp(self.num_cells, 1, 200)

        # what cells (locations) do they commonly call from?
        self.cells = random.sample(range(num_cells), self.num_cells)

        # how habitual are they in their locations?
        # 1 = always uses the same set of locations
        # 0 = completely uniform random cell for each call
        self.cell_regularity = random.normalvariate(.8, .05)

        # how frequently (on average) does someone change phones?
        self.number_switch_frequency = 0
        while self.number_switch_frequency < 24:
            # stipulate that nobody change numbers more than once per day
            frequency = 1.0/change_numbers_every
            self.number_switch_frequency = random.expovariate(frequency)

        prob_per_hour = 1/self.number_switch_frequency
        # everybody "switches" at t=0
        self.switch_times = [0]
        for hour in range(end_time):
            if random.random() < prob_per_hour:
                self.switch_times.append(hour)

        self.numbers = []
        for time in self.switch_times:
            self.numbers.append(CellNumber(self))

        assert len(self.switch_times) == len(self.numbers)

    def pick_contacts(self, cell_numbers):
        """ given a full list of cell numbers, pick which numbers this person
        usually calls """
        self.contacts = random.sample(cell_numbers, self.num_contacts)

    def __repr__(self):
        return "<Person contacts:{} cells:{} switch_frequency:{}" \
               "switch_times:{}>".format(
                  len(self.contacts),
                  len(self.cells),
                  self.number_switch_frequency,
                  len(self.switch_times)
                  )


