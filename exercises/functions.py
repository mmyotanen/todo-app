temp0 = 0
temp100 = 100


def liquid_state(temp):
    if temp >= temp100:
        print("Gas")
    elif temp > temp0:
        print("Liquid")
    else:
        print("Solid")

