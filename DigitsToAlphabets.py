n = input("Enter the Number: ")
temp = ""
ans = ""
for i in n:
    if int(i) == 1:
        temp = "One"
    if int(i) == 2:
        temp = "Two"
    if int(i) == 3:
        temp = "Three"
    if int(i) == 4:
        temp = "Four"
    if int(i) == 5:
        temp = "Five"
    if int(i) == 6:
        temp = "Six"
    if int(i) == 7:
        temp = "Seven"
    if int(i) == 8:
        temp = "Eight"
    if int(i) == 9:
        temp = "Nine"
    if int(i) == 0:
        temp = "Zero"
    
    ans = ans +" " + temp


print(ans,sep=" ")        