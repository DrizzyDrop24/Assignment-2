# experiment.py
# Run time trials of searching algorithms
# Starter Code from CSC 210
# Modified by: Sahara Bangura

from random import randint
from search import linear_search, binary_search
from time import perf_counter_ns


# Generate a random list of integers with
# every integer between min_value and max_value
# of length, length
def random_int_list(length, min_value, max_value):
    result = []

    for _ in range(length):
        result.append(randint(min_value, max_value))

    return result


# Conduct timing trials
def time_trial(num_trials, data_size, min_value, max_value):
    data = random_int_list(data_size, min_value, max_value)

    sort_start = perf_counter_ns()
    sorted_data = sorted(data)
    sort_end = perf_counter_ns()

    sort_time = sort_end - sort_start

    linear_total = 0
    binary_total = sort_time

    for _ in range(num_trials):
        key = randint(min_value, max_value)

        start = perf_counter_ns()
        linear_search(data, key)
        end = perf_counter_ns()
        linear_total += (end - start)

        start = perf_counter_ns()
        binary_search(sorted_data, key)
        end = perf_counter_ns()
        binary_total += (end - start)

    avg_linear = linear_total / num_trials
    avg_binary = binary_total / num_trials

    return float(avg_linear), float(avg_binary)
