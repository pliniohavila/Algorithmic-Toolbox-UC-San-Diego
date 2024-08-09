
def selectionSort(vetor):
    n = len(vetor)

    if n <= 1:
        return vetor
    
    for i in range(n-1):
        min = 1
        for j in range(n+1, n):
            if vetor[j] < vetor[min]:
                min = j
        if vetor[i] != vetor[min]:
            aux = vetor[i]
            vetor[i] = vetor[min]
            vetor[min] = aux
    
    return vetor


def insertionSort(vetor):
    n = len(vetor)
    if n <= 1:
        return vetor
    for i in range(1, n):
        index = i
        currentValue = vetor[i]
        for j in range(i-1, -1, -1):
            if vetor[j] > currentValue:
                vetor[j+1] = vetor[j]
                index = j
            else:
                break
        vetor[index] = currentValue
    
    return vetor

# def mergeSort(vetor):


# def merge(left, right):


# def quickSort(vetor, low=0, high=None):


# def partition(vetor, low, high):



def sortTests(vetor):
    return selectionSort(vetor)


def swap(vetor):
    vetor[0], vetor[1] = vetor[1], vetor[0]

if __name__ == '__main__':
    unsorted1 = [314159, 1, 3, 10, 3, 5]
    unsorted2 = [1, 2, 100, 12, 108, 29, 29, 37, 30, 111, 200]
    unsorted3 = [2, 4, 6, 8, 3, 0]
    unsorted4 = [4, 2]

    print(sortTests(unsorted1))
    print(sortTests(unsorted2))
    print(sortTests(unsorted3))
    print(sortTests(unsorted4))