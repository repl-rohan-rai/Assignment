def num(c, w):
     
    l = [0 for i in range(w + 1)]
    for i in range(1, w + 1):
        m = 10000
        for j in range(i):
            if j<len(c) and c[j]!=-1:
                m= min(m,c[j] + l[i - j - 1])
        l[i] = m
    if m==10000:
        return -1
    else:
        return l[w]
w=int(input())
c = [int(n) for n in input().split()]

print(num(c,w))