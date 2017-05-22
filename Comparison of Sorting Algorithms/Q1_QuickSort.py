import random
import timeit

n=int(input("Enter the max size "))

def Quicksort(A,low,high):
    if high>low:
        pivot=Partition(A,low,high)
        Quicksort(A,low,pivot-1)
        Quicksort(A,pivot+1,high)	
		
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
number=[]
for j in (range(n)): 	
    number.append(random.randint(-n,n))	
print("The unsorted list",number)	
start=timeit.default_timer()
Quicksort(number,0,len(number)-1)
end=timeit.default_timer()
print("Sorted list",number)
c=end-start
print("Time",c)

    
