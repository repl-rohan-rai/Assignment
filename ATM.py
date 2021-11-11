notes = {500:0, 100:0, 50:0, 10:0, 5:0}
def ATM(value):
    if value<=0 or (value%5)!=0:
       return "Invalid Amount"
    else:
        for i in notes:
            if value>=i:
                x=int(value/i)
                value=value-i*x
                notes[i]=x
        return notes
value=int(input())
print(ATM(value))