def Min_Cost(cost, weight):

    if weight<=0:
        return "Weight cannot be zero or less than zero"
    else: 
       l = [0 for i in range(weight + 1)]
       for i in range(1, weight + 1):
           maximum_number = 10000
           for j in range(i):
               if j<len(cost) and cost[j]!=-1:
                   maximum_number= min(maximum_number,cost[j] + l[i - j - 1])
           l[i] = maximum_number
       if maximum_number==10000:
           return -1
       else:
           return l[weight]
weight=5
cost = [20,10,4,50,100]

print(Min_Cost(cost,weight))