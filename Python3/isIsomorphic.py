'''
205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Here we are using the zip function. https://www.programiz.com/python-programming/methods/built-in/zip
        # with zip we are able to map the elements of the two strings without duplicates.
        # zip will only map the elements that have the same index and will ignore the rest if one string is bigger than the other.
        # We are also using set, to remove duplicates. https://www.programiz.com/python-programming/set
        # Then we compare the lenght of the sets and the zip, to see if they
        # as far as i comprehended the problem, the characters must follow the same order, so we also compare the lenght of the strings.
        # this because if we did not compare the lenght, this will pass as true:
        # s = "abc"
        # t = "12233"
        # set(zip(s, t))            {('b', '2'), ('c', '2'), ('a', '1')}
    	# set(s)                    {'a', 'c', 'b'}
    	# set(t)                    {'1', '2', '3'}
    	# len(set(zip(s, t)))       3
    	# len(set(s))               3
    	# len(set(t))               3
        # So its really about the interpretation of the problem. One might say that the strings are isomorphic, because they have the same characters and they follow some kind of order.
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)