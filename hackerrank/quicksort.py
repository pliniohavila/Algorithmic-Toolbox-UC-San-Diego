
def quicksort(vetor, low=0, high=None):
    if high is None:
        high = len(vetor) - 1
    
    if low < high:
        pivotIndex = partition(vetor, low, high)
        quicksort(vetor, low, pivotIndex - 1)
        quicksort(vetor, pivotIndex + 1, high)
    
    return vetor

def partition(vetor, low, high):
    pivot = vetor[high]
    i = low - 1
    for j in range(low, high):
        if vetor[j] <= pivot:
            i += 1
            vetor[i], vetor[j] = vetor[j], vetor[i]
    
    vetor[i + 1], vetor[high] = vetor[high], vetor[i + 1]
    return i + 1


if __name__ == '__main__':
    unsorted = [2, 4, 6, 8, 3, 0, 0, 5, 10, 12, 20, 1, 1, 1]
    sorted = quicksort(unsorted) 

    print(sorted)