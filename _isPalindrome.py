inp = input("Enter the Number: ")

def _isPalindrome(inp):

    rev = inp[::-1]

    if inp == rev:
        return True

    else:
        return False

if _isPalindrome(inp):

    print("Number is Palindrome")

else:

    print("Number is not a Palindrome")                