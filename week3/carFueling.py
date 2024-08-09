#!/bin/python3

def carFueling(case):
    distance = case[0]
    tank = case[1]
    stops = case[2]
    stops.append(distance)
    traveled = 0
    ans = 0

    for i in range(len(stops) - 1):
        if (stops[i+1] - stops[i]) > tank and (distance - traveled > tank):
            return 1
        elif ((stops[i+1] - stops[i])) <= (tank - stops[i]):
            tank = tank - stops[i]
        else:
            tank = 400
            ans += 1
        traveled += (stops[i] - traveled)
    print(ans)

def main():
    case1 = [950, 400, [200, 375, 550, 750]]
    case2 = [10, 3, [1, 2, 5, 9]]
    case3 = [200, 250, [100, 150]]
    carFueling(case1)
    carFueling(case2)
    carFueling(case3)
    

if __name__ == "__main__":
    main()