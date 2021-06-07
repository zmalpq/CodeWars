#You live in the city of Cartesia where all roads are laid out in a perfect grid. 
#You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
#The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 
#You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, 
#so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

#Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
#It will never give you an empty array (that's not a walk, that's standing still!).

#solution
def is_valid_walk(walk):
    # two conditions to meet:
    # 1. walk must take exactly 10 minutes. This means that the length of the directions provided must be equal to 10 (1 minute for each direction).
    # 2. walk must bring you back to original position. This means that number of north values must be equal to number of south values (sum equal to zero) and number of east values must be equal to number of west values.
    # First: create dictionary with "x" key to track sum of north/south values and "y" key to track sum of east/west values
    dict = {"x": 0, "y": 0}
    # first condition: walk must take exactly 10 minutes. if length of directions is less than or greater than 10, return False.
    if len(walk) < int(10):
        return False
    elif len(walk) > int(10):
        return False
    # if length of directions is equal to 10, we can now take a look at the second condition (walk must bring you back to original position).
    elif len(walk) == int(10):
        # use a for loop to iterate over the elements 'n', 's', 'e', 'w' in the list:
        for i in walk:
            # if i is equal to 'n' (north), add a count of +1 to the value of the key 'x' in the dictionary previously created. if equal to 's' (south), subtract 1.
            if i == "n":
                dict["x"] += 1
            if i == "s":
                dict["x"] -= 1
            # if i is equal to 'e' (east), add a count of +1 to the value of the key 'y' in the dictionary. if equal to 'w' (west), subtract 1.
            if i == "e":
                dict["y"] += 1
            if i == "w":
                dict["y"] -= 1
        # if north and south balance out to 0, and east and west balance out to 0, this means that the walk has brought you back to your original position.
        if dict == {"x": 0, "y": 0}:
            return True
        else:
            return False
