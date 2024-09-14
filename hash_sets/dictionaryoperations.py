"""
Problem 1: Array Intersection
Our journey begins with the challenge of identifying the intersection of two arrays. 
In other words, we aim to pinpoint the elements that appear in both of the given lists. 
It's important to note that we're interested in locating unique common elements - even if 
an element appears more than once in both lists, it should only feature once in our output.

Problem 1: Problem Actualisation
To elucidate how this problem might emerge in a real-world scenario, 
presume that you're managing a database for a marketing company. 
You have two customer lists, each obtained through various marketing strategies. 
Your task is to determine the customers that both strategies successfully targeted. 
Essentially, these are the common elements in your two lists.

# Problem 1: Naive Approach

Suppose you decide to resolve this problem in the most uncomplicated way possible: 
for each customer (or element) on the first list, you verify if they’re also present 
on the second list. Once you identify a match, you must confirm that this customer 
hasn't previously been added to your output. Though this solution would, in the end, 
yield the correct list of shared customers, it would demand a lot of computational 
resources, as you would be operating at a time complexity of O(n**2) due to the 
nested lookups – far from ideal! 

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
Problem 2: Non-Repeating Elements
Our next issue is slightly more complex. We must determine all elements in a given 
list that appear only once, meaning they don't have any duplicates in the same list.

Problem 2: Problem Actualisation
To illustrate how this problem might arise in real life, consider analyzing a company's
sales transactions. Your aim is to identify the products sold exactly once over a specific 
period. These could potentially be underperforming products that need investigation.

Problem 2: Naive Approach
A naive method to resolve this pitfall would involve iterating over the list and, for every item,
checking if it occurs anywhere else in the list. This method is not efficient as it results in a 
time complexity of O(n**2)

Problem 2: Efficient Approach Explanation
A more efficient approach would employ a Python set, a built-in data structure that holds an 
unordered collection of unique elements. Sets provide constant time complexity for the add, 
remove, and search operations, making this data structure suitable for our problem.

Problem 2: Solution Building
Here's how you would tackle this predicament:
First, we create two sets, one for keeping track of the elements we've seen and 
another for the elements that have repeated.

"""
nums = []
seen, repeated = set(), set()
for num in nums:
    if num in seen:
        repeated.add(num)
    else: 
        seen.add(num)