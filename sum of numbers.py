# link: https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python

# Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. 
# If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# Examples
# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

# solution 
def get_sum(a,b):
    # create a variable to track sum of numbers in the given range and assign it an initial value of zero
    sum = 0
    # if the two numbers are equal return a or b
    if a == b:
        return a 
    # remember a and b are not ordered, if a is less than b then it should come first in the range and vice versa
    elif a < b:
        #iterate over range in between integer a and integer b (+ 1 to include integer b)
        for i in range(a, b + 1):
            #for each iteration, add the current value (i) being iterated over to the variable sum and update its value
            sum += i
        return sum
    # if integer a is greater than integer b, then it should be ordered second in the range provided
    elif a > b:
        for i in range(b, a + 1):
            sum += i 
        return sum
