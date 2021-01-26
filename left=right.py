a = [6,2,2,11,23,4,6,3,8]

templeft = sum(a[0:int((len(a))/2)])
tempright = sum(a[int((len(a))/2)+1:len(a)])
yes = False

if templeft == a[int((len(a))/2)] and tempright ==  a[int((len(a))/2)] :


    yes = True

  #   print(a[int((len(a))/2)])

if yes:

    print("YESSSS") 


else :

    print("Nopeee")
