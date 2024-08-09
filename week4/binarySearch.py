
def binarySearch(vetor, target, min, max):
    if max < min:
        return -1
    guess = (max + min) // 2
    if vetor[guess] == target:
        return guess
    elif vetor[guess] < target:
        return binarySearch(vetor, target, guess + 1, max)
    else:
        return binarySearch(vetor, target, min, guess - 1)
    

def selectionSort(vetor):
    n = len(vetor)
    if n <= 1:
        return vetor
    
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if vetor[j] < vetor[min]:
                min = j
        if vetor[i] != vetor[min]:
            aux = vetor[i]
            vetor[i] = vetor[min]
            vetor[min] = aux
    
    return vetor

if __name__ == '__main__':
    vetor = selectionSort([5, 1, 5, 8, 12, 13])
    toSearch = [5, 8, 1, 23, 1, 11]
    n = len(vetor)
    for i in toSearch:
        isFound = binarySearch(vetor, i, 0, n - 1)
        print(i, isFound, vetor[isFound])