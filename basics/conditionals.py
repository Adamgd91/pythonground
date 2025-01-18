your_age = int(input("What is your age? "))
age = 22
string_age = str(age)

if your_age >= 21:
    print(f'You can drink since you are {your_age - 21} years above the drinking cutoff! ')
else:
    print(f'You can NOT drink!')