
temp = []
arr = list(map(int, input().split()))


while len(arr)>=2:

    arr.sort()
    sum1 = 0
    sum1 = arr[0] + arr[1]
    arr.remove(arr[0])
    arr.remove(arr[0])
    temp.append(int(sum1))
    arr.append(sum1)

res = sum(temp)
print(res)    
    





