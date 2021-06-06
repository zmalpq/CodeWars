#You are going to be given a word. Your job is to return the middle character of the word. 

#If the word's length is odd, return the middle character. 

#If the word's length is even, return the middle 2 characters.

#Examples:

#Kata.getMiddle("test") should return "es"

#Kata.getMiddle("testing") should return "t"

#Kata.getMiddle("middle") should return "dd"

#Kata.getMiddle("A") should return "A"

#solution
def get_middle(s):
    if len(s) % 2 == 0:
        left_middle = s[(len(s) - 1) // 2]
        right_middle = s[len(s) // 2]
        return f'{left_middle}{right_middle}'
    else:
        middle = s[len(s) // 2]
        return middle
