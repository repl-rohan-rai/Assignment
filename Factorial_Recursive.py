def fact(n):
    if number.isdigit()!=true:
        return "Enter an integer value"
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*fact(n-1)
    
n=int(input())
print(fact(n))
