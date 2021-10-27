def num(a,n):
    x=0
    y=0
    j=0
    for i in range(n):
        if i>x:
            j+=1
            x=y
        y=max(y,i+a[i])
    return j
a=[int(i) for i in input().split()]
n=len(a)
print(num(a,n))