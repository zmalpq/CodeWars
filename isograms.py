#An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
#Implement a function that determines whether a string that contains only letters is an isogram. 
#Assume the empty string is an isogram. Ignore letter case.

#is_isogram("Dermatoglyphics" ) == true
#is_isogram("aba" ) == false
#is_isogram("moOse" ) == false # -- ignore letter case

#solution
def is_isogram(string):
    #convert string to lower case in order to ignore letter case
    string = string.lower()
    #iterate over each character in the string
    for char in string:
        #if number of occurrences for the character being iterated over is greater than 1, return False as it is not an isogram
        if string.count(char) > 1:
            return False
    #do not indent return True - it should not fall under the block of code being executed by the for loop
    return True
