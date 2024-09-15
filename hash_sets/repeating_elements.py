"""
    Given a list of integers. Return a list of repeating elements of that list.
"""


def repeating_elements(nums):
    # Set to keep track of elements seen once
    seen_elements = set() 
    # Set to store elements that appear more than once
    repeated_elements = set()

    for num in nums:
        if num in seen_elements:
            # If the item is already seen, add it to repeated_elements
            repeated_elements.add(num)
        else:
             # If not seen before, add it to seen_elements
            seen_elements.add(num)
    return list(repeated_elements) 
    
print(repeating_elements([9, 8, 7, 8, 7, 6, 5]))  # expected output : [8, 7]
print(repeating_elements([-1, 2, 3, -1, 2, 3]))   # expected output : [-1, 2, 3]
print(repeating_elements([1, 2, 3, 4, 5]))        # expected output : []