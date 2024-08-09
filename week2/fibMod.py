def pisanoPeriod(m):
    f0 = 0
    f1 = 1
    for i in range(0, (m*m)):
        fi =  (f0 + f1) % m
        f0 = f1
        f1 = fi
        if (f0 == 0 and f1 == 1):
            return i + 1
        
def fibMod(n, m):
    pisanoNumber = pisanoPeriod(m)
    n = n % pisanoNumber
    prev = 0
    curr = 1

    if (n <= 1):
        return n
    
    for i in range(n-1):
        temp = curr
        curr = (prev + curr) % m
        prev = temp

    return curr % m

def main():
    print(f"LCM (239, 1000) = {fibMod(239, 1000)} - Assert: {161}")
    print(f"LCM (2816213588, 239) = {fibMod(2816213588, 239)} - Assert: {151}")
    # print(f"LCM (6, 8) = {fibMod(6, 8)} - Assert: {24}")
    # print(f"LCM (761457, 614573) = {fibMod(761457, 614573)} - Assert: {467970912861}")

    
if __name__ == "__main__":
    main()