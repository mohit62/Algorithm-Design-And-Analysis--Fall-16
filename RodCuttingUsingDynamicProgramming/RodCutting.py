import sys
def cut_rod(price, length, cost):
    revenue = [0 for x in range(length+1)]
    size = [0 for x in range(length+1)]
    revenue[0] = 0
    for j in range(1, length+1):
        q = -sys.maxint
        for i in range(1, j+1):
            if i == j and q < (price[i][1] + revenue[j-i]):#No Cuts Scenario
                q = (price[i][1] + revenue[j-i])
                size[j] = i
            elif i != j and q < (price[i][1] + revenue[j-i] - cost):#Rod with Cuts Scenario
                q = (price[i][1] + revenue[j-i] - cost)
                size[j] = i
        revenue[j] = q
    return revenue,size

def Cut_Rod_Solution(price, length, cost):
    revenue,size = cut_rod(price, length, cost)
    print "Maximum Revenue is:", revenue[length]
    print "The size of piece(s) cut is as follows:"
    while (length > 0):
        print (size[length])
        length = length - size[length]		

price = [int(price) for price in raw_input().strip().split(" ")]#input price for each length 
price.insert(0, 0)#Add 0 as price for length 0
price = [[i, price[i]] for i in range(len(price))]
print "The price entered is ",price
length = int(raw_input("Enter the Length of Rod "))
cost = int(raw_input("Enter the cost of each cut "))
Cut_Rod_Solution(price, length, cost)    

