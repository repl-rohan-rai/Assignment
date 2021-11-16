def jumps(initial_array,length):
    x=0
    y=0
    jump=0
    if all(isinstance(x, int) for x in initial_array)!=True:
        return "Elements in the array only need to be integer values"
    if length==0:
        return "List cannot be empty"
    else:
        for i in range(length):
            if initial_array[i]<=0:
                    return "Jump length cannot be less than or equal to zero"
            if i>x:
                jump+=1
                x=y
            y=max(y,i+initial_array[i])
        return jump
initial_array=[0]
length=len(initial_array)
print(jumps(initial_array,length))
