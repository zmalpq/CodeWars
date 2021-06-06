#Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

#For example:

#unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
#unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
#unique_in_order([1,2,2,3,3])       == [1,2,3]

#solution
def unique_in_order(iterable):
    #create empty list to append letters
    lst = []
    #create variable to track current letter being iterated. Set initial value to None
    current_letter = None
    for letter in iterable:
        #if letter being iterated over does not match current_letter, append that letter to list.
        if letter != current_letter:
            lst.append(letter)
            #update current_letter to the letter being iterated over.
            current_letter = letter
            #i.e. (AAAABBBCCDAABB') 
            #1. first letter iterated over is 'A'. 
            #2. As 'A' does not match current_letter (value set to None), 'A' is appended to empty list.
            #3. The variable current_letter is then assigned 'A' as a value.
            #4. Loop iterates over next letter in iterable, which is another 'A'.
            #5. As 'A' is equal to current_letter, loop does not execute body of if/else statement.
            #6. Once loop iterates over a different letter ('B'), steps 2-4 repeat.
    return lst 
