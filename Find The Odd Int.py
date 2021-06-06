#Given an array of integers, find the one that appears an odd number of times.

#There will always be only one integer that appears an odd number of times.

#solution
def find_it(arr):
    for i in arr: 
        if arr.count(i) % 2 == 1:
            return i 
