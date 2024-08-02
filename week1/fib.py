def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    fibSeq = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584]
    inputs = [0, 1, 4, 5, 10, 18]
    for n in inputs:
        print(f"Fib nth {n} = {fib(n)} - Assert: {fibSeq[n]}")

if __name__ == "__main__":
    main()