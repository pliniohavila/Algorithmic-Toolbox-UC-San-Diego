#!/bin/python3

def sort(arr):
    n = len(arr)
    if n == 1:
        return arr
    for i in range(n):
        for j in range (0, n - 1):
            if arr[j] < arr[j + 1]:
                tmp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = tmp
    return arr


def maxAdv(arr):
    arrA = sort(arr[0])
    arrB = sort(arr[1])
    n = len(arrA)
    r = 0
    for i in range(n):
        r += arrA[i] * arrB[i]
    return r

def main():
    case1 = [[23], [39]]
    case2 = [[1, 3, -5], [-2, 4, 1]]
    print(maxAdv(case1))
    print(maxAdv(case2))
    
if __name__ == "__main__":
    main()