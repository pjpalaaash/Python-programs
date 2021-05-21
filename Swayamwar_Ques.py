n = int(input())

br = input()

gr = input()

bride = []
groom = []

for i in range(0,n):
    bride.append(br[i])

for i in range(0,n):
    groom.append(gr[i])


r_cnt_gr = groom.count("r")
m_cnt_gr = groom.count("m")
#print(r_cnt_gr)
#print(m_cnt_gr)
lst = [i for i in bride]

#print(lst)
for b in lst:
    if b =="r":
        if r_cnt_gr == 0:
            #print("r",r_cnt_gr)
            #print(lst)
            print(len(lst),end=" ")
            break
        r_cnt_gr -=1 
        lst.pop(0)
        #print(bride)
        #print(r_cnt_gr)

    elif b =="m":
        if m_cnt_gr == 0:
            print(len(lst),end=" ")
            break
        m_cnt_gr -=1
        lst.pop(0)
        #print("M",m_cnt_gr)
else:
    print("0",end=" ")         


