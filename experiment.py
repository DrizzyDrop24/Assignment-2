# experiment.py
# Run time trials of searching algorithms
# Starter Code from CSC 210
# Modified by: [Your Name]

from random import randint
from search import linear_search, binary_search
from time import perf_counter_ns

# Generate a random list of integers with
# every integer between *min_value* and *max_value*
# of length, *length*
def random_int_list(length, min_value, max_value):
    # YOUR CODE HERE
    pass
    
# Conduct *num_trials* number of trials of linear and
# binary search using a random list of *data_size* with
# *min_value* and *max_value* 
# Record the time that the average linear search or binary search
# takes
# Use the same list data for both searches but pre-sort it
# in a copied list for the binary searches
# Be sure to amortize the cost of sorting by dividing the time
# it takes to do the one sort across all binary searches
# Create a new search key between *min_value* and
# *max_value* for each search
# Return the average linear search time and average
# binary search time as a tuple in that respective order
# To measure the time something takes in nanoseconds
# you can use something like:
# start_time = perf_counter_ns()
# expensive_thing()
# end_time = perf_counter_ns()
# time_elapsed += (end_time - start_time)
def time_trial(num_trials, data_size, min_value, max_value):
    # YOUR CODE HERE
    pass