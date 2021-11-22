maximum_number = 10000
def Min_Cost(cost, weight):
    if all(isinstance(x, int) for x in cost)!=True:
        return "Invalid Cost value"
    for value in cost:
        if value<=0:
            return "Cost value cannot be less than oe equal to zero"
    if weight<=0:
        return "Weight cannot be zero or less than zero"
    else: 
       list_value = [0 for i in range(weight + 1)]
       for i in range(1, weight + 1):
           for j in range(i):
               if j<len(cost) and cost[j]!=-1:
                   maximum_number= min(maximum_number,cost[j] + list_value[i - j - 1])
           list_value[i] = maximum_number
       if maximum_number==10000:
           return -1
       else:
           return list_value[weight]
weight=5
cost = [20,10,4,50,100]

print(Min_Cost(cost,weight))
