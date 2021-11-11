def Contiguos_subarray(initial_array,size):
    if size==0:
        return "List cannot be empty"
    else:
        sum_a=initial_array[0]
        sum_b=initial_array[0]
        for i in range(1,size):
            sum_b = max(initial_array[i], sum_b + initial_array[i])
            sum_a = max(sum_a,sum_b)
         
        return sum_a
number = [-2,-3,4,-1,-2,1,5,-3]
print(Contiguos_subarray(number,len(number)))