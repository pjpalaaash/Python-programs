inp = input().split()
print(inp)

final = []


for each in inp:

    temp = []
    for every in each:
        if every.isdigit():
            temp.append(every)       
    s = "".join(temp)
    final.append(int(s))        
            
print(final)
arr_sum = []

for ele in final:
    sum = 0
    while(ele!=0):
        temp = ele%10
        sum += temp
        ele = ele//10
    arr_sum.append(sum)

print(f"Sum of Digits of a Number is {arr_sum}")        

