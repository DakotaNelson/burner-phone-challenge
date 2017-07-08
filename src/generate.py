import random
import csv

from person import Person
from config import num_people

### ASSUMPTIONS (which should change, TODO) ###
# 1. Everyone only has one phone at a time
# 2. Highest resolution is an hour, only one "call" can happen per hour
# 3. No day/night cycle

people = []

if __name__ == "__main__":
    for x in range(num_people):
        people.append(Person())

    # build a list of all cell numbers
    cell_numbers = []
    for person in people:
        for cell_number in person.numbers:
            cell_numbers.append(cell_number)

    # pick each person's favored contacts from the numbers
    for person in people:
        person.pick_contacts(cell_numbers)

    # generate call records for each number
    for cell_number in cell_numbers:
        cell_number.generateRecords(cell_numbers)

    # put all of the call records in one place
    all_records = []
    for person in people:
        for number in person.numbers:
            all_records.extend(number.call_records)

    # sort the call records by time
    all_records = sorted(all_records, key=lambda k: k['time'])

    # write out all of the call records
    with open('call_records.csv', 'w') as csvfile:
        fieldnames = ['time', 'cell', 'from', 'to']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in all_records:
            writer.writerow(row)

    print("[*] Call record data written to call_records.csv")

    # build a dict mapping numbers to people (the solutions!)
    solutions = []
    for person in people:
        for number,time in zip(person.numbers, person.switch_times):
            solutions.append({
                'person': person._uuid,
                'number': number.uuid,
                'switch_time': time
                })


    # write out the "who has a number when" solutions
    with open('solutions.csv', 'w') as csvfile:
        fieldnames = ['person', 'number', 'switch_time']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in solutions:
            writer.writerow(row)

    print("[*] Solutions written to solutions.csv")

    try:
        import networkx as nx

        G=nx.DiGraph()

        for record in all_records:
            G.add_edge(str(record['from']), str(record['to']), time=record['time'], cell=record['cell'])

        nx.write_gexf(G, 'call_records.gexf')
        print("[*] Call record data written to call_records.gexf")
    except ImportError:
        print("[!] NetworkX library not found, skipping graph export.")
