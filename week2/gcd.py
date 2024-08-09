def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, (a % b))

def main():
    # inputs = [[206, 40, 2], [18, 35, 1]]
    print(f"GCD (206, 40) = {gcd(206, 40)} - Assert: {2}")
    print(f"GCD (18, 35) = {gcd(18, 35)} - Assert: {1}")

    
if __name__ == "__main__":
    main()