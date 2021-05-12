s,r = [int(x) for x in input().split()]
count = 0
res = []

samp = [int(x) for x in input().split()]

for i in range(r):

    upp,lower = [int(x) for x in input().split()]
    for ele in samp:
        if ele>=upp and ele<=lower:
            count+=1
    res.append(count)
    count=0

for i in res:
    print(i,end=" ")    






