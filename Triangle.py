def triangle(l):
    list_length=len(l)
    if list_length==1:
        return l[0]
    elif list_length==0:
        return "List cannot be empty"
    else:
        path_value=l[0][0]
        j=0
        for i in range(1,list_length):
            path_value+=min(l[i][j],l[i][j+1])
            j=l[i].index(min(l[i][j],l[i][j+1]))
        return path_value
l=[[2],[3,7],[8,5,6],[6,1,9,3]]
print(triangle(l))