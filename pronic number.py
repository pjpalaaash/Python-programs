n = input().split()


print(n)

final = []

for each in n:

    final.append(int(each))

temp = []
for ele in final:

    ele2 = ele + 1
    if ele * ele2 in final:

        print(f"for {ele} in list and its pronicle {ele} * {ele2} is {ele*ele2} ")
        print(f" {ele*ele2} is present in final list...")



        





