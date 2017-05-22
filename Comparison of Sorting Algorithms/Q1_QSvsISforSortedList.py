import sys
import random
import timeit
import matplotlib.pyplot as plt
n=int(input("Enter the max size "))

def insertionSort(list):
        for index in range(1,len(list)):
            current = list[index]
            pos = index
            while pos>0 and list[pos-1]>current:
                list[pos]=number[pos-1]
                pos -=1
            number[pos]=current

		
def Partition(A,low,high):
    pivot_initial=A[high]
    i=low-1	
    for j in range(low,high):
        if A[j]<=pivot_initial:
            i+=1
            temp1=A[i]
            A[i]=A[j]
            A[j]=temp1
    i+=1
    temp=A[i]
    A[i]=A[high]
    A[high]=temp			
    return i
def Quicksort(A,low,high):
    if high>low:
        pivot=Partition(A,low,high)
        Quicksort(A,low,pivot-1)
        Quicksort(A,pivot+1,high)	
		



size=[]
time=[]
time1=[]
for i in range(0,n+1,10):
    if(i == 0):
        continue
    size.append(i)
    number=[]
    number1=[]
    for j in (range(len(size)*10)): 	
        number.append(random.randint(-n,n))
        Quicksort(number,0,len(number1)-1)	
        number1.append(number[j])
        Quicksort(number1,0,len(number1)-1) 
    start= timeit.default_timer()
    insertionSort(number)
    end= timeit.default_timer()
    c=end-start
    time.append(c)
    start= timeit.default_timer()
    sys.setrecursionlimit(11000)	
    Quicksort(number1,0,len(number1)-1)
    end= timeit.default_timer() 
    d=end-start
    time1.append(d)	

print("Size",size,"Time",time)
print("Size",size,"Time",time1)     
plt.plot(size,time)
plt.plot(size,time1)
plt.xlabel('Size')
plt.ylabel('Time')
plt.title("Insertion Sort(Blue) Vs Quicksort(Green) For SortedList")
plt.show()

