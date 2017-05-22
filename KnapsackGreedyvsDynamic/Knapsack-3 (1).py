def Knapsack_0_1(Value,Weight,Cap):
    load1=0
    i=0
    total1=0
    while (load1<Cap) and i<=len(Weight)-1:
        if Weight[i]<=(Cap-load1):
            load1+=Weight[i]
            total1+=Value[i]
        else:
            break
        i+=1
    return load1,total1
def KnapSack_DP(Value,Weight,Cap,n):
    K = [[0 for x in range(Cap+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(Cap+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif Weight[i-1] <= w:
                K[i][w] = max(Value[i-1] + K[i-1][w-Weight[i-1]],K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][Cap]
def Fractinal_Knapsack(Value,Weight,Cap):
    load=0
    i=0
    total=0
    while (load<Cap) and i<=len(Weight)-1:
        if Weight[i]<=(Cap-load):
            load+=Weight[i]
            total+=Value[i]
        else:
            fract=float(Cap-load)/Weight[i]
            load+=Weight[i]*fract 
            total+=Value[i]*fract
           
        i+=1
    return load,total

#Value=[int(temp) for temp in raw_input("Enter the values").strip().split()]
#Weight=[int(t) for t in raw_input("Enter the weights").strip().split()]
#Capacity=raw_input("Enter the capacity")
Value=[60,100,120]
Weight=[10,20,30]
Capacity=50
#Capacity=int(Capacity)
Ratio=[]
NewW=[]
NewV=[]
NewR=[]
for i in range(len(Value)):
    Ratio.insert(i,Value[i]/Weight[i])
SortR=list(Ratio)
SortR.sort(reverse=True)
for i in range(len(Value)):
    NewR.insert(i,Ratio.index(SortR[i]))   
for i in range(len(Value)):
    NewW.insert(i,Weight[NewR[i]])
    NewV.insert(i,Value[NewR[i]])
n=len(Value)
TotalSize,TotalValue=Fractinal_Knapsack(NewV,NewW,Capacity)
print "For Fractional Knapsack"+"Total Size "+str(TotalSize)+" Total Value "+str(TotalValue)
TotalSize1,TotalValue1=Knapsack_0_1(NewV,NewW,Capacity)
print "For 0/1 Knapsack"+"Total Size "+str(TotalSize1)+" Total Value "+str(TotalValue1)
TotalValue2=KnapSack_DP(NewV,NewW,Capacity,n)
print "For  Knapsack Using DP"+" Total Value "+str(TotalValue2)
