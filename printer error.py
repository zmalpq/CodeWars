#link: https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

#solution 
def printer_error(s):
    lst = []
    for i in s:
        if i not in "abcdefghijklm":
            lst.append(i)
    error_rate = str(len(lst)) + "/" + str(len(s))
    return error_rate
