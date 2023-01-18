# https://www.hackerrank.com/challenges/counting-valleys

def countingValleys(steps, path):
    
    # idea: initialize a counter = 0 & number_of_valleys = 0
    # add to / subtract from the counter as you iterate over the path
    # if current iteration step == D and counter == 0
    # then number_of_valleys += 1
    
    counter = 0 
    number_of_valleys = 0
    
    for step in path:
        if step == 'D':
            if counter == 0:
                number_of_valleys += 1
            counter -= 1
        else:
            counter += 1

    return number_of_valleys