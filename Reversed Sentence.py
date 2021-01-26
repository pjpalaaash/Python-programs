inp = input("Enter the String: ")

temp = inp.split(" ")
print(temp)

sentence = " ".join(reversed(temp))

print(sentence)