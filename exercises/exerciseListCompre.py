usernames = ["john 1990", "alberta1970", "magnola2000"]

usernames = [float(len(username)) for username in usernames]

print(sum(usernames))
