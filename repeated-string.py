# https://www.hackerrank.com/challenges/repeated-string


def repeatedString(s, n):
    # initialize current interation i = 0 & counter = 0
    # while i < n check value at index i%n%len(s)
    # e.g. for i==9, s=='aba', n==10 this should be s[9%10%3] == s[0]
    # visual mapping shown below
    # a[0]b[1]a[2] a[3]b[4]a[5] a[6]b[7]a[8] a[9]
    # a[0]b[1]a[2] a[0]b[1]a[2] a[0]b[1]a[2] a[0]
    # if element == a increase counter by 1
        
    i = 0 
    count_a = 0
    
    while i < n:
        if s[i % n % len(s)] == 'a':
            count_a += 1
        i += 1

    return count_a 


# Optimized for large numbers 
def repeatedString(s, n):
        
    i = 0 
    
    full_str_count = 0
    last_str_count = 0
    
    while i < len(s):
        if s[i] == 'a':
            if i < n % len(s): # this is the length of the last (incomplete) appended string
                last_str_count += 1
            full_str_count += 1
        i += 1

    # count of letter `a` in a full string * repetitions of the full string + 
    # + count of letter `a` in the last incomplete string
    return full_str_count * (n // len(s)) + last_str_count


# One-liner for geeks & faster than the above
def repeatedString(s, n):
    return s.count('a') * (n // len(s)) + s[:n%len(s)].count('a')