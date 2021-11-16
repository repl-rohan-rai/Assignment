def longest_substring(number,length):
    if any(not i.isdigit() for i in number):
        return "Invalid String!.Contains non-integer values"
    num=0
    first_half=0
    second_half=0
    result=0
    for i in range(0,length-1):
        for j in range(i+1,length):
            part_integer=number[int(i):int(j)+1]
            if len(part_integer)%2==0:
                for k in part_integer[0:int(len(part_integer)/2)]:
                    first_half+=int(k)
                for k in part_integer[int(len(part_integer)/2):]:
                    second_half+=int(k)
                if first_half==second_half:
                    if num<first_half:
                        num=first_half
                        result=len(part_integer)
            first_half=0
            second_half=0
    return result
number="123123"
length=len(number)
print(longest_substring(number,length))