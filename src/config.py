""" This file contains global constants that are parameters for the model.
Modify these to change how the data look (and how "big data" you feel) """

### Parameters ###

# total number of cells for the area of interest
num_cells = 1000

# total number of people call records are collected for
num_people = 1000

# time is in hours, starting from 0
# so, if end time is 48, the generated data spans two days
end_time = 30 * 24

# on average, people change numbers every... (in hours)
change_numbers_every = 365 * 24 * 3
