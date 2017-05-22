import random
import timeit
n=int(input("Enter the max size "))

def insertionSort(list):
        for index in range(1,len(list)):
            current = list[index]
            pos = index
            while pos>0 and list[pos-1]>current:
                list[pos]=number[pos-1]
                pos -=1
            number[pos]=current

number=[]
for j in (range(n)): 	
    number.append(random.randint(-n,n))
print("The unsorted list",number)	
start=timeit.default_timer()
insertionSort(number)
end=timeit.default_timer()
print("Sorted list",number)
c=end-start
print("Time",c)
