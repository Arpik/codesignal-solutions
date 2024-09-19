"""
Task_1 Array Intersection

Find all non-repeating elements in a list, which means identifying 
items that appear only once. This problem can arise in real-life scenarios, such as 
analyzing sales data to find products sold exactly once.

A naive approach would involve checking every item against the rest of the list, but 
this results in inefficient O(n²) time complexity. A more efficient solution uses a 
Python set, which allows for faster operations. The approach involves using two sets: 
one for elements seen and another for repeated elements.

Problem 1: Efficient Approach Explanation
Here, the unique functionality of Python's set data structure proves beneficial. 
A set in Python, as you may remember, is an unordered collection of unique objects, 
ensuring the absence of duplicate values. Furthermore, it allows us to perform several 
operations on such collections, such as:

        - intersection (identifying common elements), 
        - union (combining all unique elements), 
        - difference (detecting unique items in a set).

"""

def array_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))


"""
Task_2 Non-repeating elements

The problem involves finding elements in a list that appear only once. 
A real-world example could be identifying products sold only once in a 
company's transactions. 
A naive solution checks each item against the rest, 
resulting in O(n²) time complexity. 
A more efficient approach uses Python sets, which offer constant time operations. 
The solution involves creating two sets: 
one to track seen elements and another for repeated elements.

"""

def intersecting_elements(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    common_elements = sorted(set_1.intersection(set_2))  
    
    return common_elements[::-1]
     
print(intersecting_elements({1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, {5, 6, 7, 8, 9, 10, 11, 12, 13, 14}))
# Expected output: [10, 9, 8, 7, 6, 5]

print(intersecting_elements({-1, -2, -3, -4, -5}, {-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5}))
# Expected output: [-1, -2, -3, -4, -5]

print(intersecting_elements({1, 3, 5, 7, 9}, {2, 4, 6, 8, 10}))
# Expected output: []


"""
Task_3 Problem 3: Unique Elements
The third problem compels us to find elements unique to each of 
the two given lists, i.e. given two lists, list1 and list2, we 
need to find elements that exist only in list1 and elements that 
exist only in list2, respectively.

"""

def unique_elements(list_1, list_2):
     set1 = set(list_1)
     set2 = set(list_2)

     # Get unique to each set elements by using set difference
     unique_to_1 = sorted(list(set1 - set2))
     unique_to_2 = sorted(list(set2 - set1))

     return (unique_to_1, unique_to_2)

    


        
       



