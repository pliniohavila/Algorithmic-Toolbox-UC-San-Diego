def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, (a % b))

def lcm(a, b):
    a = abs(a)
    b = abs(b)

    r = a * (b / gcd(a, b))
    return r

def main():
    print(f"LCM (21, 6) = {lcm(21, 6)} - Assert: {42}")
    print(f"LCM (6, 8) = {lcm(6, 8)} - Assert: {24}")
    print(f"LCM (761457, 614573) = {lcm(761457, 614573)} - Assert: {467970912861}")

    
if __name__ == "__main__":
    main()