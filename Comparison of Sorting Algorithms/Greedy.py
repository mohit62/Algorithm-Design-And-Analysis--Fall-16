number=[]
n =int(input("enter number of categories:"))
for i in range(n):
    num = int(input())
    number.append(num)

print (number)


for GQ in range(n,-1,-1):
    count,m = 0,0
    for j in number:
        if GQ<=j:
            count+=1
        else:
            m+=1
    if (GQ <= count and (n - count) == m):
        print("The GQ is : %d" % GQ)	
        break      	  			

	   
    