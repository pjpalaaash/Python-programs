l = []

def push_ele():
    n = int(input("Enter the number of Element you want to Add: "))
    for i in range(0,n):
        a = int(input("Enter the Element: "))
        l.append(a)
def pop_ele():
    if len(l)<=0:
        print("List is Empty..!!!")
    else:
        return l.pop()

def display_list():
    for i in range(len(l)-1,-1,-1):
        print(l[i]) 
while 1:
    print(''' ***************Choose your choice**********************

                        1.To Add Elements in the list.
                        2.To Delete Elements in the list.
                        3.To Display List.'''

            )

    Choose = int(input("Enter Your Choice: "))
    
    if Choose == 1:
        push_ele()
    elif Choose == 2:
        pop_ele()      

    elif Choose == 3:
        display_list()
                

    elif Choose== 4:
        exit()    

    else :
        print('Wrong Input....')
        continue



