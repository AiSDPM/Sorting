import math
import random
import copy
import time

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

logfile = open('quickIter.txt', 'w')

n = 1
quickList = []
greater = [-5000]
lower = [-5000]
for j in range(15):
    quickList = []
    greater = [-5000]
    lower = [-5000]
    for i in range(1000 * n):
        lower.append(lower[-1] + random.randint(1,10))
        greater.append(greater[-1] + random.randint(1, 10))

    lower.sort()
    lower.reverse()
    greater.sort()
    quickList = copy.copy(greater)
    quickList += lower
    startTime = time.time()
    QuickSort(quickList)
    endTime = time.time()
    Time = endTime - startTime
    logfile.write("QuickSort " + str(Time) + "\n")
    print(str(
        n) + ".    ----------------------------------------------------------------------------------------------------------")
    n += 1
logfile.close()
