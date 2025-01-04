name = input("What is your name? ")
salary = float(input("What is your salary? "))
bonus = float(input("What is your bonus percentage? "))

print(f"Hello, {name}! Your total salary is {int(1000 + (salary * bonus))}")