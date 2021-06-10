# link: https://www.codewars.com/kata/52761ee4cffbc69732000738/train/python

# solution 
def goodVsEvil(good, evil):
    # create two different lists for good and evil containing the associated worths for each race
    good_values = [1, 2, 3, 3, 4, 10]
    evil_values = [1, 2, 2, 2, 3, 5, 10]
    
    # create two variables for good and evil that contain the sum of worth values for each side, assign initially to 0 
    good_total = 0 
    evil_total = 0
    
    good = good.split()
    evil = evil.split()
    for num1, num2 in zip(good_values, good):
            good_total += num1 * int(num2)

    for num1, num2 in zip(evil_values, evil):
            evil_total += num1 * int(num2)
    
    if good_total > evil_total: 
        return 'Battle Result: Good triumphs over Evil'
    elif evil_total > good_total:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'
