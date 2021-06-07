#Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

#For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

#Note: The function accepts an integer and returns an integer

#revise - inefficient solution
def square_digits(num):
    numLst = [int(d) for d in str(num)]
    finalLst = [(i**2) for i in numLst]
    result = "".join(str(i) for i in finalLst)
    result = int(result)
    return result
