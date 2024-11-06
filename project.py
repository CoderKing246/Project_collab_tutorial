import math 
import datetime 

print("Start the project.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def greet():
    current = datetime.datetime.now().strftime("%H")
    if int(current) >= 6 and int(current) < 12:
        print("Good morning!")
    elif int(current) >= 12 and int(current) < 16:
        print("Good afternoon!")
    else:
        print("Good evening!")