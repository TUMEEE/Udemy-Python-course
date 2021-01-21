def solve():
    meal_cost, tip_percent, tax_percent = float(input()), int(input()), int(input())
    total_cost = meal_cost + (tip_percent/100)*meal_cost  + (tax_percent/100)*meal_cost
    print(round(total_cost))
solve()
