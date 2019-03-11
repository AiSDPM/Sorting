def MergeSortMain(A):
     B = [0] * len(A)
     A = MergeSort(A, 0, len(A) - 1, B)
     return A

def MergeSort(A, first, last, B):
    med = (first+last)//2
    if (med - first) >0:
        MergeSort(A, first, med, B)
    if (last - med) >1:
        MergeSort(A, med+1, last, B)
    i = first
    j = med + 1
    for k in range(first, last+1):
        if ((i <= med) and (j > last)) or (((i <= med) and (j <= last)) and (A[i] <=A[j])):
            B[k] = A[i]
            i +=1
        else:
            B[k] = A[j]
            j +=1
    for k in range(first, last+1):
        A[k]=B[k]
    return A

Tablica = [1, 4, 6, 4, 7, 36, 346, 3, 57, 34, -50, 37]
print(MergeSortMain(Tablica))