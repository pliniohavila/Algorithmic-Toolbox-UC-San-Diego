


def majorityElement1(vetor, target, min, max):
    if max < min:
        return -1
    guess = (max + min) // 2
    if vetor[guess] == target:
        count  = 0
        i = guess
        while vetor[i - 1] == target:
            i -= 1
        i += 1
        print(i)
        while vetor[i] == target:
            count += 1
            i += 1
        if count > len(vetor)//2:
            return count
    elif vetor[guess] < target:
        return majorityElement1(vetor, target, guess + 1, max)
    else:
        return majorityElement1(vetor, target, min, guess - 1)
    

def majorityElement(vetor):
    n = len(vetor)
    for i in range(0, n):
        currentElement = vetor[i]
        count = 0
        for j in range(i, n):
            if vetor[j] == currentElement:
                count += 1
        if count > n//2:
            return vetor[i]
    return 0



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
    sample1 = selectionSort([2, 3, 9, 2, 2])
    sample2 = selectionSort([1, 2, 3, 4])
    sample3 = selectionSort([1, 2, 3, 1])
    print(majorityElement(sample1))
    print(majorityElement(sample2))
    print(majorityElement(sample2))