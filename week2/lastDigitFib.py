def lastDigitFib(n):
    result = [None] * (10 ** 7)
    result[0] = 0
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = (result[i - 1] + result[i - 2]) % 10
    return result[n]
    
def main():
    fibSeq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
    inputs = [0, 1, 4, 5, 10, 18]
    for n in inputs:
        print(f"LastFibDigit nth {n} = {lastDigitFib(n)} - Assert: {fibSeq[n]}")

if __name__ == "__main__":
    main()