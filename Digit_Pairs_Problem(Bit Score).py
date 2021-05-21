n = int(input())
input_arr = []

for i in range(n):
    number = input()
    input_arr.append(number)

#print(input_arr)

score = []

for every in input_arr:

    temp = []
    for digit in every:

        temp.append(int(digit))

    res = max(temp)*11 + min(temp)*7
    score.append(res)
#print(score)

bit_score = []

for each in score:

    if len(str(each)) > 2:
        rem = each%100
        bit_score.append(rem)
    else:
        bit_score.append(each)    

# print(bit_score)
even = []

odd = []

for i in range(0,len(bit_score)):

    if i%2 == 0:
        even.append(bit_score[i])
    else:
        odd.append(bit_score[i])

# print(even)
# print(odd)
pair1 = 0
pair2 = 0
for i in range(0,len(odd)-1):

    for j in range(i+1,len(odd)):

        first = str(odd[i])
        second = str(odd[j])

        if first[0] == second[0]:
            if pair1 < 2:
                pair1+=1

for i in range(0,len(even)-1):

    for j in range(i+1,len(even)):

        first = str(even[i])
        second = str(even[j])

        if first[0] == second[0]:
            if pair2 < 2:
                pair2+=1

print(pair1+pair2)
        


