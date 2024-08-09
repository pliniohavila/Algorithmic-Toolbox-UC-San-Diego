
def selectionSort(vetor):
    n = len(vetor)

    if n == 1:
        return vetor
    
    for i in range(n-1):
        min = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[min]:
                min = j
        if vetor[i] != vetor[min]:
            aux = vetor[i]
            vetor[i] = vetor[min]
            vetor[min] = aux

    return vetor

def mergeSort(vetor):
    n = len(vetor)

    if n <= 1:
        return vetor
    
    mid = n // 2
    left = vetor[:mid]
    right = vetor[mid:]

    sortedLeft = mergeSort(left)
    sortedRight = mergeSort(right)

    return merge(sortedLeft, sortedRight)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

def bigSorting(unsorted):
    return selectionSort(unsorted)


if __name__ == '__main__':
    unsorted1 = [31415926535897932384626433832795, 1, 3, 10, 3, 5]
    unsorted2 = [1, 2, 100, 12303479849857341718340192371, 3084193741082937, 3084193741082938, 111, 200]
    
    print(bigSorting(unsorted1))
    print(bigSorting(unsorted2))