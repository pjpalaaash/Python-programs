import random 

randNum = random.randint(1,100)
guesses = 0
userNum = None
#print(randNum)
while userNum != randNum:
    userNum = int(input("Enter the number b/w 1-100: "))
    guesses +=1
    if userNum == randNum:
        print("You Guessed it right...!!!")
    else:
        print("You guessed it Wrong....!!")
        if userNum > randNum:
            print("Enter the Smaller number...")
        else:
            print("Enter the larger number...")    
        print("Guess again...")
print("You guessed in ",+guesses, "guesses...")

with open("hiscore.txt","r") as f:
     hiscore = int(f.read())

if guesses<hiscore: 
      with open("hiscore.txt","w") as f:
          f.write(str(guesses))
          print(f"You had breaked the high score of {hiscore} guessed")          
     