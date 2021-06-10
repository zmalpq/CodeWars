#link: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

# solution 
def filter_list(l):
    filtered_list = list(filter(lambda x: isinstance(x, int) ,l))
    return filtered_list
