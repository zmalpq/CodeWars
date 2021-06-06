#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
#The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#Example
#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice


#solution
def duplicate_count(text):
    #make text case-insensitive
    text = text.lower()
    #create empty list to add characters with duplicates
    lst = []
    #iterate over characters in input string
    for char in text:
    #if character count > 1 (character has duplicates) and character is not in list:
        if (text.count(char) > 1 and not(char in lst)):
            #add character to list 
            lst.append(char)
    #return length of list (number of duplicates)       
    return len(lst)
