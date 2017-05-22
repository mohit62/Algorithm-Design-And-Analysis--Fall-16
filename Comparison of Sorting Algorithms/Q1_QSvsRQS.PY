import sys
import random
import timeit
import matplotlib.pyplot as plt
n=int(input("Enter the max size "))


def RandQuicksort(A,low,high):
    if high>low:
        pivot=RandomPartition(A,low,high)
        RandQuicksort(A,low,pivot-1)
        RandQuicksort(A,pivot+1,high)	
def RandomPartition(A,low,high):
    pivot=random.randrange(low,high+1)
    temp=A[pivot]
    A[pivot]=A[high]
    A[high]=temp
    return RandPartition(A,low,high)
		
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
def RandPartition(A,low,high):
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
time1=[]
time2=[]
for i in range(0,n+1,100):
    if(i == 0):
        continue
    size.append(i)
    number1=[]
    number2=[]
    for j in (range(len(size)*100)): 	
        number1.append(random.randint(-n,n))		
        number2.append(number1[j])

    start= timeit.default_timer()
    sys.setrecursionlimit(11000)	
    Quicksort(number1,0,len(number1)-1)
    end= timeit.default_timer() 
    d=end-start
    time1.append(d)	
    print("Time",d)
    start= timeit.default_timer()
    RandQuicksort(number2,0,len(number2)-1)
    end= timeit.default_timer()
    timeit.default_timer()
    e=end-start
    time2.append(e)		
    print("Time",e)
print("Size",size,"Time",time1) 
print("Size",size,"Time",time2)     
plt.plot(size,time1)
plt.plot(size,time2)
plt.xlabel('Size')
plt.ylabel('Time')
plt.title("Quicksort(Blue) Vs RandomQuicksort(Green)")
plt.show()

