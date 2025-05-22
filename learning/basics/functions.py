is_student = False
gpa = 3.4

def students(is_online):
    if is_online:
        print("Online")
    else:
        print("Offline")
    
students(is_student)

name = "adam"
age = 34
print(name)

def testing():
    x = 4
    if x > 3:
        print("hello")
    
testing()
print(f"My name is {name} and I am {age} years old!!!")

ages = [23, 34, 54, 31, 21, 77, 87, 21]

def oldest():
    the_oldest = max(ages)
    print(the_oldest)
    
oldest()