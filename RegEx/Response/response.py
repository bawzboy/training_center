import validators

if validators.email(input("Your email address: ")):
    print("Valid")
else:
    print("Invalid")
