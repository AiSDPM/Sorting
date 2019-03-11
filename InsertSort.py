
def InsertSort (A):
     for i in range(1,len(A)):
        key = A[i]
        j=i-1
        while j >= 0 and  A[j] > key:
            A[j+1] = A[j]
            j -=1
        A[j+1]=key
     return A

Tablica = [1,4,6,4,7,36,346,3,57,34,-50,37]
print(InsertSort(Tablica))

