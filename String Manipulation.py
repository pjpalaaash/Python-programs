arr1 = ['j','i','w','l','q','r']

arr2 = ['a','6','s','5','a']

arr3 = []

for every in arr2:
    if not every.isdigit():
        arr3.append(every)

print(arr3)
temp = ""
l = len(arr3)-1

for each in arr1:

    ind = arr1.index(each)

    if l == -1:
        kuch = arr1[ind+1::]
        s = "".join(kuch)

        temp+= each + s
        break

    else:
        temp += each + arr3[l]
    l-=1    
    


print(temp)    