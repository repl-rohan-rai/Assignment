n=input()
l=list(n)
ln=len(l)
f=0
for i in range(0,ln):
    b=0
    if l[i]=='(' or l[i]=='{' or l[i]=='[':
        c=l[i]
        for j in range(i+1,ln):
            if c=='(' and l[j]==')':
                b=1
            elif c=='{' and l[j]=='}':
                b=1
            elif c=='[' and l[j]==']':
                b=1
            if b==1:
                break
        if b==0:
            print("Invalid Expression")
            f=1
            break
if f!=1:
    print("Valid Expression")
