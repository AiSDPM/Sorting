class Stacks:
    def __init__(self):
        self.tab = []

    def push(self, a, b):
        self.tab.append((a, b))

    def pop(self):
       pom = self.tab.pop(-1)
       return pom

    def empty(self):
        if len(self.tab) > 0:
            return False
        else:
            return True

def QuickSort(A):
    stack = Stacks()
    stack.push(0, len(A)-1)
    while not stack.empty():
        l, p = stack.pop()
        while l < p:
            x = A[(l+p)//2]
            i=l
            j=p
            while i < j:
                 while A[j] > x:
                    j -=1
                 while A[i] < x:
                    i +=1
                 if i <= j:
                     A[i], A[j] = A[j], A[i]
                     i +=1
                     j -=1
            if i<p:
                stack.push(i, p)
            p = j
    return A

Tablica = [1, 4, 6, 7, 36, 346, 3, 57, 34, -503, 37,3,1,4,6]
print(QuickSort(Tablica))