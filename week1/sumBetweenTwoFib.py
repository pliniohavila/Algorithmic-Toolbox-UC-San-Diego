def lastDigitFib(n):
    result = [None] * (10 ** 7)
    result[0] = 0
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = (result[i - 1] + result[i - 2]) % 10
    return result[n]
    
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def sumBetweenTwoFib(m, n):
    result = [None] * (20)
    end = (n - m) 

    if (m == n):
        return lastDigitFib(m)
    
    result[0] = lastDigitFib(m)
    result[1] = lastDigitFib(m + 1)

    for i in range(2, end + 2):
        result[i] = (result[i - 1] + result[i - 2]) % 10

    # print(result)
    return result[end]


def main():
    # sumBetweenTwoFib(3, 7)
    # sumBetweenTwoFib(5, 5)
    # sumBetweenTwoFib(8, 15)
    print(f"[3 7] = {sumBetweenTwoFib(3, 7)} - Assert: {1}")
    print(f"[10 10] = {sumBetweenTwoFib(10, 10)} - Assert: {5}")
    print(f"[1 20] = {sumBetweenTwoFib(1, 20)} - Assert: {2}")

if __name__ == "__main__":
    main()