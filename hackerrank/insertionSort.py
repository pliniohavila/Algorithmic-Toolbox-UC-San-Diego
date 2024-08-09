
def insertionSort1(n, vetor):
    for i in range(1, n):
        index = i
        currentValue = vetor.pop(i)
        for j in range(i - 1, -1, -1):
            if vetor[j] > currentValue:
                index = j
        vetor.insert(index, currentValue)
        
    return vetor

def insertionSort(vetor):
    n = len(vetor)
    if n <= 1:
        return vetor
    
    for i in range(1, n):
        index = i
        currentValue = vetor[i]
        for j in range(i - 1, -1, -1):
            if vetor[j] > currentValue:
                vetor[j + 1] = vetor[j]
                index = j
            else: 
                break
        vetor[index] = currentValue

    return vetor
        

if __name__ == '__main__':
    unsorted1 = [314159, 1, 3, 10, 3, 5]
    unsorted2 = [1, 2, 100, 12, 3084193741082937, 30, 111, 200]
    unsorted3 = [2, 4, 6, 8, 3, 0]
    
    print(insertionSort(unsorted1))
    print(insertionSort(unsorted2))
    print(insertionSort(unsorted3))