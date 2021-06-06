#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.


#solution - list comprehension
def find_short(s):
    #s.split() - split string into a list of individual words
    #len(l) for l in s.split() -> get lengths of each word
    #min() -> get length of shortest word
    shortest_word = min(len(l) for l in s.split())
    return shortest_word
