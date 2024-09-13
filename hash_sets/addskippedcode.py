# Imagine that you have a massive database, and you're tracking millions 
# of unique data entries. If you need to frequently check whether certain 
# items exist in your dataset, comparing the performance of lists versus 
# hash sets could play an instrumental role in your memory management process.
# We've prepared a starter code for a Python function, but part of it is missing. 
# 
# Could you complete the code? Your task is to check the existence of a test element in both a 
# list and a set 100 times, then print the time it took to process each case.

# WITH SOLUTION

# Importing the necessary libraries
import time

# Define a function to demonstrate the operation and time complexity of a hash set
def compare_operations():
  
    # Create a list and a set
    data_list = []
    data_set = set()

    # Adding elements to list and set
    for i in range(10**6):
        data_list.append(i)
        data_set.add(i)

    # Set and List are ready; now let's define a non-existing item to search for
    test_item = 10**6 + 1  # This item is not in our set or list

    # Timing the 100 consecutive operations for set
    start_time_set = time.time()
    for _ in range(100):
        test_item in data_set
    print("Hash Set took: ", time.time() - start_time_set)

    # Timing the 100 consecutive operations for list
    start_time_list = time.time()
    for _ in range(100):
        test_item in data_list
    print("List took: ", time.time() - start_time_list)

# Execute the function
compare_operations()