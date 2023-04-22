import random


def random_number(lower, upper):
    try:
        number = random.randint(lower + 1, upper - 1)
        return number
    except ValueError:
        print("Boundaries are incorrect, make sure there is atleast one number inbetween, and lower value first")


lower_bound = int(input("Enter lower bound: "))
upper_bound = int(input("Enter upper bound: "))
random.randrange(lower_bound, )
print(random.randrange(lower_bound, upper_bound))
print(random_number(lower_bound, upper_bound))
