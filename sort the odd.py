# link: https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# solution 
def sort_array(source_array):
    # list comprehension to create a separate list of odd integers from the original input
    # sorted in ascending order
    oddLst = sorted([i for i in source_array if i % 2 != 0])
    # create a variable that tracks the indices of the odd numbers in oddLst 
    oddLst_index = 0
    # iterate over the range of integers from the input array: 
    for j in range(len(source_array)):
        # if the integer being iterated over is an odd number:
        if source_array[j] % 2 != 0:
            # replace that integer with the first indexed number from the oddLst (oddLst[0])
            source_array[j] = oddLst[oddLst_index]
            # add 1 to value of int to update index from 0 to 1 
            oddLst_index += 1
    return source_array 
