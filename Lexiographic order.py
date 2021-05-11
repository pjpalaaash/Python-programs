t = int(input("Test Cases: "))

while t > 0:

    lex = input("Enter lexi order: ")
    orig = input("Enter original: ")

    result = ""
    if len(lex) <=26:

        for ele in lex:
            if ele in orig:
                result += ele
    else:
        print(-1)            

    print(result)
    t -= 1        