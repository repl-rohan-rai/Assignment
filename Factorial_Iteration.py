def fact(number):
    if number==0:
        return 1
    elif number==1:
        return 1
    else:
        c=1
        for i in range(1,number+1):
            c=c*i
        return c
    
number=int(input())
print(fact(number))