#!/bin/python3

def moneyChange(m):
    coins = 0
    while m > 0:
        if m >= 10:
            m -=10
        elif m >= 5:
            m -= 5
        else:
            m -= 1
        coins += 1
    return coins

def main():
    print(moneyChange(2))
    print(moneyChange(28))
    
if __name__ == "__main__":
    main()