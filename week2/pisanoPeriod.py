def pisanoPeriod(m):
    f0 = 0
    f1 = 1
    for i in range(0, (m*m)):
        fi =  (f0 + f1) % m
        f0 = f1
        f1 = fi
        if (f0 == 0 and f1 == 1):
            return i + 1
        

print(pisanoPeriod(2))
print(pisanoPeriod(3))
print(pisanoPeriod(4))
print(pisanoPeriod(10))