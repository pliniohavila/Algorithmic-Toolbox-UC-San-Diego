#!/bin/python3

def sortThings(things):
    n = len(things)
    if n == 1:
        return things
    for i in range(n):
        for j in range (0, n - 1):
            if (things[j]['value'] / things[j]['weight']) < things[j + 1]['value'] / things[j + 1]['weight']:
                tmp = things[j + 1]
                things[j + 1] = things[j]
                things[j] = tmp
    return things

def maxValueLoot(bagWeight, things):
    things = sortThings(things)
    n = len(things)
    load = 0
    val = 0
    i = 0
    while (i < n) and (load < bagWeight):
        if things[i]['weight'] <= (bagWeight - load):
            val += things[i]['value']
            load += things[i]['weight']
        else:
            r = (bagWeight - load) / things[i]['weight']
            val += r * things[i]['value']
            load += things[i]['weight']
        i += 1
    print(val)
    return val 
        

def main():
    # 0=v and 1=w
    case1 = [{"value": 60, "weight": 20}, {"value": 100, "weight": 50}, {"value": 120, "weight": 30}]
    case2 = [{"value": 3, "weight": 2}, {"value": 4, "weight": 3}, {"value": 5, "weight": 4}]
    case3 = [{"value": 500, "weight": 30}]
    maxValueLoot(50, case1)
    maxValueLoot(5, case2)
    maxValueLoot(10, case3)
    
if __name__ == "__main__":
    main()