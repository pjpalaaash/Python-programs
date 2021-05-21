s1 = input()

s2 = input()

def cal(s1,s2):

    ans = s1.rfind(s2)

    if ans < 0:
        return 0

    else:
        l = s1[:ans]

        r = s1[ans+len(s2):]

        return 1 + cal(l+r,s2)



res = cal(s1,s2)

fin = len(s1) - res * len(s2)

print(fin)
      