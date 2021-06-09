#link: https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python

#solution 
def longest(a1, a2):
    a3 = a1 + a2
    a3_sorted = sorted(a3)
    lst = []
    for i in a3_sorted:
        if i not in lst: 
            lst.append(i)
    return ''.join(lst)
