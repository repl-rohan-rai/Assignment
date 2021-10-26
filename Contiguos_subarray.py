def num(a,size):
    b=a[0]
    c=a[0]
    for i in range(1,size):
        c = max(a[i], c + a[i])
        b = max(b,c)
         
    return b
a = [int(n) for n in input().split()]
print(num(a,len(a)))