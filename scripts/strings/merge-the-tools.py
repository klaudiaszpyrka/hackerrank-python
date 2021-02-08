# HackerRank https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    splits = []
    for i in range(0, len(string), k):
        splits.append(string[i:(i+k)])
        
    #print(splits)
    
    splits_clean = []
    for split in splits:
        splits_clean.append("")
        for i in range(len(split)):
            if split[i] in splits_clean[-1]:
                pass
            else:
                splits_clean[-1] += split[i]
                
    for split in splits_clean:
        print(split)

merge_the_tools('AGADCCGBA', 3)