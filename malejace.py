import math
import random
import copy
import time


def HeapSort(A):
    BuildHeap(A)
    heapsize = len(A)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapsize -= 1
        Heapify(A, 0, heapsize)
    return A


def BuildHeap(A):
    heapsize = len(A)
    for i in range((len(A) // 2), -1, -1):
        Heapify(A, i, heapsize)


def Heapify(A, i, heapsize):
    l = 2 * i + 1
    r = 2 * i + 2
    if (l < heapsize) and (A[l] > A[i]):
        largest = l
    else:
        largest = i
    if (r < heapsize) and (A[r] > A[largest]):
        largest = r
    if largest != i:
        A[largest], A[i] = A[i], A[largest]
        Heapify(A, largest, heapsize)


def InsertSort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def MergeSortMain(A):
    B = [0] * len(A)
    A = MergeSort(A, 0, len(A) - 1, B)
    return A


def MergeSort(A, first, last, B):
    med = (first + last) // 2
    if (med - first) > 0:
        MergeSort(A, first, med, B)
    if (last - med) > 1:
        MergeSort(A, med + 1, last, B)
    i = first
    j = med + 1
    for k in range(first, last + 1):
        if ((i <= med) and (j > last)) or (((i <= med) and (j <= last)) and (A[i] <= A[j])):
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
    for k in range(first, last + 1):
        A[k] = B[k]
    return A


def SelectionSort(A):
    for i in range(len(A) - 1, 0, -1):
        maks = i
        for j in range(i, -1, -1):
            if A[j] > A[maks]:
                maks = j
        A[maks], A[i] = A[i], A[maks]
    return A




lowerList = []
heaList = []
merList = []
selList = []
logfile = open('malejace.txt', 'w')

n = 1
for j in range(15):
    greaterList = [10000]

    for i in range(1000 * n):
        greaterList.append(greaterList[-1] + random.randint(0, 10))

    lowerList = copy.copy(greaterList)
    lowerList.reverse()

    insList = copy.copy(lowerList)
    heaList = copy.copy(insList)
    merList = copy.copy(insList)
    selList = copy.copy(insList)

    startTime = time.time()
    InsertSort(insList)
    endTime = time.time()
    Time = endTime - startTime
    logfile.write("InsertSort " + str(Time)+ "\n")

    startTime = time.time()
    HeapSort(heaList)
    endTime = time.time()
    Time = endTime - startTime
    logfile.write("HeapSort " + str(Time)+ "\n")

    startTime = time.time()
    MergeSortMain(merList)
    endTime = time.time()
    Time = endTime - startTime
    logfile.write("MergeSort " + str(Time)+ "\n")

    startTime = time.time()
    SelectionSort(selList)
    endTime = time.time()
    Time = endTime - startTime
    logfile.write("SelectionSort " + str(Time) + "\n")
    print(str(
        n) + ".    ----------------------------------------------------------------------------------------------------------")
    n += 1
logfile.close()
