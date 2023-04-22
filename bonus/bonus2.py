meals = ['1.pasta', '1.pizza', '1.salad']

meals = [meal.replace(".", "-") + ".txt" for meal in meals]

print(meals)
