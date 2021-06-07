#Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

#move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

#solution
def move_zeros(array):
    zeroLst = []
    numLst = []
    for i in array:
        if int(i) == 0:
            zeroLst.append(i)
        else:
            numLst.append(i)
    return numLst + zeroLst
