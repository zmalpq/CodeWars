# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

# For example:

 # persistence(39) # returns 3, because 3*9=27, 2*7=14, 1*4=4
                 # and 4 has only one digit
                  
 # persistence(999) # returns 4, because 9*9*9=729, 7*2*9=126,
                  # 1*2*6=12, and finally 1*2=2

 # persistence(4) # returns 0, because 4 is already a one-digit numb

#solution
def persistence(n):
    # if n is a single digit, return 0.
    if n < 10:
        return 0
    else:
        # create variable to store result of multiplication
        res = 1
        # convert integer n into a string so that each individual digit can be iterated over
        string_n = str(n)
        # iterate over each digit of integer using for loop
        for i in string_n: 
            # for each digit iterated over, convert digit back to integer and multiply by res variabl
            res *= int(i) 
    # recursion - function calling itself
    return 1 + persistence(res)
