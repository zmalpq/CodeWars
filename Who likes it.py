#You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. 

#We want to create the text that should be displayed next to such an item.

#Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item. 
    
#It must return the display text as shown in the examples:


#solution
def likes(names):
    display_text = ""
    if len(names) == 0:
        display_text = "no one likes this"
    elif len(names) == 1:
        display_text = f"{names[0]} likes this"
    elif len(names) == 2:
        display_text = f"{names[0]} and {names[1]} like this"
    elif len(names) == 3:
        display_text = f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        remainder = len(names) - 2
        display_text = f"{names[0]}, {names[1]} and {str(remainder)} others like this"
    return display_text
