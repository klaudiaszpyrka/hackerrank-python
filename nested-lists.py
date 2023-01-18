# https://www.hackerrank.com/challenges/nested-list/problem 

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    #print(records)

    names, scores = zip(*records)
    #print(names)
    #print(scores)
    
    scores = list(set(scores))
    scores.sort()
    second_lowest = scores[1]
    #print(second_lowest)
    
    result_names = [record[0] for record in records if record[1] == second_lowest]
    #print(result_names)
    
    result_names.sort()
    for name in result_names:
        print(name)
        