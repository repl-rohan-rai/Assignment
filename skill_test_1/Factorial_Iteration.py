def fact(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        c=1
        for i in range(1,n+1):
            c=c*i
        return c
    
n=int(input())
print(fact(n))