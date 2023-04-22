with open('cointoss.txt', 'w') as file:
    heads = 0
    average = 0


while True:
    flip = input("Throw the coin and enter head of tail here: ?") + "\n"
    with open('cointoss.txt', 'r') as file:
        coins = file.readlines()
        coins.append(flip)
    with open('cointoss.txt', 'w') as file:
        file.writelines(coins)
    flip = flip.strip("\n")
    if flip == 'head':
        heads = heads + 1
    if heads == 0:
        average = 0
    else:
        average = float(heads / len(coins) * 100)
    print(f"Heads: {average}%")









