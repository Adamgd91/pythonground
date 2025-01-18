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