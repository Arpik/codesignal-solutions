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

nums = []
seen, repeated = set(), set()
for num in nums:
    if num in seen:
        repeated.add(num)
    else: 
        seen.add(num)