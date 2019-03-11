def SelectionSort(A):
    for i in range(len(A)-1, 0, -1):
        maks = i
        for j in range(i, -1, -1):
            if A[j] > A[maks]:
                maks = j
        A[maks], A[i] = A[i], A[maks]
    return A


Tablica = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -501, 37]
print(SelectionSort(Tablica))
