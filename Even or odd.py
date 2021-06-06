#Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

#solution
def even_or_odd(number):
    if int(number) % 2 == 0:
        return "Even"
    else:
        return "Odd"
