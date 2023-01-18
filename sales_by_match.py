# https://www.hackerrank.com/challenges/sock-merchant

def sockMerchant(n, ar):
    pairs = {}
    
    for a in ar:
        if a in pairs.keys():
            pairs[a] += 1
        else:
            pairs[a] = 1

    number_of_pairs = 0
    
    return sum(list(map(lambda x: int(x/2), pairs.values()))) 

ar = [10,20,20,10,10,30,50,10,20]
sockMerchant(9,ar)