# https://www.hackerrank.com/challenges/jumping-on-the-clouds

def jumpingOnClouds(c):

    # 0 --> good clouds, cumulus
    # 1 --> bad clouds, thunderheads
    
    # idea: initialize leaps = 0 
    # always try to leap by 2 => check index at i+2
    # where i is the current index in the iteration
    # if i+2 == 0 then leaps += 1
    # and jump to i+2
    # if i+2 == 1 then leaps += 1
    # and jump to i+1
    
    # make sure to only leap by 1
    # if the current iteration is at c[-2]
    # to avoid IndexError list index out of range
        
    i = 0
    leaps = 0
    
    while i < len(c)-1:  
        leaps += 1

        if (i == len(c)-2) or (c[i+2] == 1):
            i += 1
        else: 
            i += 2
            
    return leaps