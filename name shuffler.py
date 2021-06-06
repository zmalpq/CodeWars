#Write a function that returns a string in which firstname is swapped with last name.

#e.g. name_shuffler('john McClane'); => "McClane john"

def name_shuffler(str_):
    str_ = str_.split()
    reverse_str = " ".join(reversed(str_))
    return reverse_str
