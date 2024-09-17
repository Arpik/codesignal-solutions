"""
Problem 1: 
Unique String in the List

Our first problem revolves around identifying the first unique 
string from a list. Imagine you're working on a text analyzing 
tool that needs to identify the first unique word in a piece of text. 
This problem simulates such a real-world scenario.

Efficient Approach Explanation

Our strategy consists of two parts, each tailored to leverage the capabilities of sets:
We scan through the words, keeping track of the previously encountered words in a set called seen. 
A crucial aspect of our solution comes from an inherent feature of sets: if a word is already 
in seen, adding it again does not change the set. Keeping this in mind, we create a second set, 
duplicates, consisting only of words that we have previously seen.

Once we know which words are duplicates, it becomes elementary to find the first word in our original 
list that isn't a duplicate. We make another pass over the list, checking each word to see if it's in 
the duplicates set. The first word we find that isn't a duplicate is our answer.

"""
def find_unique_string(words):
    seen = set()
    duplicates = set()
    
    for word in words:
        if word in seen:
            duplicates.add(word)
        seen.add(word)
    
    for word in words:
        if word not in duplicates:
            return word

    return ""
