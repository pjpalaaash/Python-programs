import random

def Winner(comp,you):
   
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    elif comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True
    else:
        print("Wrong Entry....!!") 

numba = int(input("Number of chances you want??: "))
for i in range(0,numba):
    total = 0
    total2 = 0
    rand = random.randint(1,3)
    if rand == 1:
        comp = "r"
    elif rand == 2:
        comp = "p"
    elif rand == 3:
        comp = "s" 


    you = input("Choose Rock(r),Papper(p),Scissor(s)....?? : ")


    cool = Winner(comp,you)

    print(f"Computer chooses {comp} and You chooses {you}")
    if cool:
         total +=1
         print("YoOhOOoo!!! You wOnn....")
       
    elif cool == None:
        print("Oohhh!! Its a Tie...!!")
    
    else:
         total2+=1
         print("Computer Won") 
       
print(f"Your total points are {total} and Computer points are {total2}")
print("Thankyou for playing!!")