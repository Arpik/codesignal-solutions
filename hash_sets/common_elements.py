"""
    Given 2 lists of integers. Write a function to return
    a list of common for two lists elements in ascending order
"""


def intersecting_elements(list_1, list_2):
    # Convert lists into sets 
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    # Separate common elements
    common_elements = sorted(list(set_1.intersection(set_2)))  
    
    # Reverse the sorted list and return
    return common_elements[::-1]
     
print(intersecting_elements({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}))
# Expected output: [10, 9, 8, 7, 6, 5]

print(intersecting_elements({-1, -2, -3, -4, -5}, {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}))
# Expected output: [-1, -2, -3, -4, -5]

print(intersecting_elements({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}))
# Expected output: []