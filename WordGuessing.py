    

def cityGuess():
    with open("city.txt","r") as f:
        content = f.read()
        


    display = "."*(len(content))

    gameOver = False
    tries = 3
    while not gameOver:

        print((display))
        print("Guess city name......")    
        guess = input("Guess any letter: ")
        guess =  guess.lower()
    
        i = 0
        if guess in content:
                
            while content.find(guess,i) != -1:
                i = content.find(guess,i)
                display = display[:i] +guess + display[i+1:]
                i+=1
            print("Correct")    

        else:
            print("Wrong Guess...")
            tries-=1
        if display[0:-1] == content[0:-1]:
            print("Congrats You guessed it right....") 
            print(content)
            gameOver = True
        if tries == 0:
            print("You are out of chances....")
            gameOver = True       
       
def playerGuess():
    with open("player.txt","r") as f:
        content = f.read()
        


    display = "."*(len(content))

    gameOver = False
    tries = 3
    while not gameOver:

        print((display))
        print("Guess Player name......")    
        guess = input("Guess any letter: ")
        guess =  guess.lower()
    
        i = 0
        if guess in content:
                
            while content.find(guess,i) != -1:
                i = content.find(guess,i)
                display = display[:i] +guess + display[i+1:]
                i+=1
            print("Correct")    

        else:
            print("Wrong Guess...")
            tries-=1
        if display[0:-1] == content[0:-1]:
            print("Congrats You guessed it right....") 
            print(content)
            gameOver = True
        if tries == 0:
            print("You are out of chances....")
            gameOver = True       




print('''   
            .................Choose any Option.....................
                            1.CITY NAME
                            2.PLAYER NAME''')

choice = int(input("Your Choice: "))

if choice == 1:
    cityGuess()
if choice == 2:
    playerGuess() 
else:
    print("Wrong Input....")       