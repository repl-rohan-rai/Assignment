def triangle(triangle_list):
    list_length=len(triangle_list)
    if all(isinstance(x, int) for x in triangle_list)!=True:
        return "Input Integer value only"
    if list_length==1:
        return triangle_list[0]
    elif list_length==0:
        return "List cannot be empty"
    else:
        path_value=triangle_list[0][0]
        j=0
        for i in range(1,list_length):
            path_value+=min(triangle_list[i][j],triangle_list[i][j+1])
            j=l[i].index(min(triangle_list[i][j],triangle_list[i][j+1]))
        return path_value
triangle_list=[[2],[3,7],[8,5,6],[6,1,9,3]]
print(triangle(triangle_list))
