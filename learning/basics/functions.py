is_student = False
gpa = 3.4

def students(is_online):
    if is_online:
        print("Online")
    else:
        print("Offline")
    
students(is_student)
#################################################
def testing():
    x = 4
    if x > 3:
        print("hello")
    
testing()

#################################################
ages = [23, 34, 54, 31, 21, 77, 87, 21]

def oldest():
    the_oldest = max(ages)
    print(the_oldest)
    print(f'Ages list length is: {len(ages)}')
    
oldest()