def QuickSortMain(A):
    QuickSort(A,0,len(A)-1)
    return A

def QuickSort(A, p, r):
    if p < r:
        q = Partition(A, p, r)
        print(A)
        QuickSort(A, p, q)
        QuickSort(A, q+1, r)

def Partition (A, p, r):
    x = A[(p+r)//2]
    i = p
    j = r
    while True:
        while A[j] > x:
            j -=1
        while A[i] < x:
            i +=1
        if i < j:
            print(i,j)
            A[i], A[j] = A[j], A[i]
        else:
            return j

Tablica = [1, 4, 6, 7, 36, 346, 3, 57, 34, -503, 37,1] #poprawić by działao dla rownych
print(QuickSortMain(Tablica))