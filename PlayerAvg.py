Scores = []
Boundaries = []

def calAvg():
    Sc = int(input("Enter the Player Score: "))
    Scores.append(Sc)
    Avg = sum(Scores)/len(Scores)
    print(f"Player's Current Average is: {Avg}")

def BoundPercent():
    Bound = int(input("Enter the No of Boundaries: "))
    Boundaries.append(Bound)
    lstScore = Scores[-1]
    BoundAvg = (Bound/lstScore)*100
    print(BoundAvg)
def total_BoundPer():
    print(f"Total Score is: {sum(Scores)} ")
    print(f"Total Boundaries are: {sum(Boundaries)}")
    total = (sum(Boundaries)/sum(Scores))*100 
    print(total)   

while 1:

    print(''' 
              1. To Calculate Avg of a player.
               
              2. To Calculate Boundary Percentage of an Inning.


              3. To Calculate Total Boundary Percent.

              4. To Exit.'''
    
     )


    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        calAvg()
    elif choice == 2:
        BoundPercent()
    elif choice == 3:
        total_BoundPer()

    elif choice == 4:
        exit()
    else:
        print("Wrong Input...!!!!!")               
