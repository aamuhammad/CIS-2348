user_input = input()
sWithoutSpaces = ""
for x in user_input:
    if x != ' ':
        sWithoutSpaces += x
sReverse = ""
for x in sWithoutSpaces:
    sReverse = x + sReverse
if sWithoutSpaces == sReverse:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")