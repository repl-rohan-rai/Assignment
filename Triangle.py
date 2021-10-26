l=[]
ll=[]
while(True):
    ll=[int(n) for n in input().split()]
    if ll==[]:
        break
    l.append(ll)
x=len(l)
s=l[0][0]
j=0
for i in range(1,x):
   s+=min(l[i][j],l[i][j+1])
   j=l[i].index(min(l[i][j],l[i][j+1]))
print(s)