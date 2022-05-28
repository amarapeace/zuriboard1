# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True
from collections import Counter

def find_anagram(word, anagram):
    # [assignment] Add your code here
    if Counter(word) == Counter(anagram):
        print(True)
        return True
    else:
        print(False)
        return False

find_anagram('silent','listen')

