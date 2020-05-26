print("enter a meal cost")
meal = input()
def all(meal):
    tax = 0.07
    meal_cost = float(meal)
    tax = meal_cost * tax
    meal_and_tax = meal_cost + tax
    tip = meal_and_tax * 0.20
    answer = meal_cost + tax + tip
    print(answer)
    
all(meal)


