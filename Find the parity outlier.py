#You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
#The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
#Write a method that takes the array as an argument and returns this "outlier" N.

#Examples
#[2, 4, 0, 100, 4, 11, 2602, 36]
#Should return: 11 (the only odd number)

#[160, 3, 1719, 19, 11, 13, -21]
#Should return: 160 (the only even number)

#solution
def find_outlier(integers):
    #create two empty lists to separate even and odd integers 
    evenLst = []
    oddLst = []
    #iterate over inputted integers
    for i in integers:
        #if integer is divisible by 2, it is an even number. Append it to the even list. 
        if i % 2 == 0:
            evenLst.append(i)
        #if not, it is an odd number. Append it to the odd list. 
        else:
            oddLst.append(i)
    #compare the lengths of the even list and the odd list. If the even list is longer, then the single outlier must be in the odd list, and vice versa. 
    if len(evenLst) > len(oddLst):
        return oddLst[0]
    else: 
        return evenLst[0]
