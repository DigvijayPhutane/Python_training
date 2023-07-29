string = input("enter the email: ")
mail = ("@gmail.com")
if string[0].isupper():
    print("plz lowercase the email")
else:
    for i in string:
        if mail in string:
            print("Valid email")
            break
        else:
            print("Invalid email")
            break
