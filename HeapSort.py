def HeapSort (A):
    BuildHeap(A)
    heapsize = len(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -=1
        Heapify(A, 0, heapsize)
    return A

def BuildHeap(A):
    heapsize = len(A)
    for i in range (len(A)//2),-1,-1):
        Heapify(A, i, heapsize)

def Heapify(A, i, heapsize):
    l = 2*i+1
    r = 2*i+2
    if( l < heapsize) and (A[l]> A[i]):
        largest = l
    else:
        largest = i
    if (r < heapsize) and (A[r] > A[largest]):
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Heapify(A, largest, heapsize)

Tablica = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -503, 37]
print(HeapSort(Tablica))