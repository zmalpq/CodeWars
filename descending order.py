#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

#Examples:
#Input: 42145 Output: 54421

#Input: 145263 Output: 654321

#Input: 123456789 Output: 987654321


#inefficient solution
def descending_order(num):
    #split number into list using list comprehension
    numList = [int(n) for n in str(num)]
    #sort list in descending order
    numList.sort(reverse=True)
    #join list to return integer
    res = "".join(str(i) for i in numList)
    #convert result from string back to integer
    return int(res)
