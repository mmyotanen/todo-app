new_password = input("Enter a password: ")


def password_checker(password):
    password_status = {}

    if len(password) < 8:
        password_status['length'] = False
    else:
        password_status['length'] = True

    digit = False
    capitalized = False

    for item in password:
        if item.isdigit():
            digit = True
        if item.isupper():
            capitalized = True

    password_status['digit'] = digit
    password_status['capitalized'] = capitalized

    if all(password_status.values()):
        print("Strong password")
    else:
        print("Weak password")


password_checker(new_password)