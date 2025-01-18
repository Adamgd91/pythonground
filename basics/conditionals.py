your_age = int(input("What is your age? "))
age = 22
string_age = str(age)

if your_age >= 21:
    print(f'You can drink since you are {your_age - 21} years above the drinking cutoff! ')
else:
    print(f'You can NOT drink!')
    
    
quantity = int(input("How many pizzas do you want? "))
price = 6.99
total = quantity * price

print(f'You ordered {quantity} pizzas and your total is ${total}! ')

my_weight = float(input("What is your weight? "))
unit = input("Kilograms or Lbs? (K or L): ").upper()

if unit == "K":
    my_weight = my_weight * 2.205
    unit = "Lbs"
elif unit == "L":
    my_weight = my_weight / 2.205
    unit = "Kgs"
else:
    print(f'{unit} was not valid')

print(f'Your weight is: {round(my_weight, 2)} {unit}!')