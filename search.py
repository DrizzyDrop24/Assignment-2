# search.py
# Implementations of simple searching algorithms
# Starter Code from CSC 210
# Modified by: [Sahara Bangura]

# This version of linear search looks for
# *key* in *lst* and returns a boolean (True or False)
# depending on if it found it
def linear_search(lst, key):
    for item in 1st:
        if item == key:
            return True
    return False
    pass

# This version of binary search looks for
# *key* in *lst* and returns a boolean (True or False)
# depending on if it found it
def binary_search(data, key):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == key: 
            return True
        elif data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return False
    pass
