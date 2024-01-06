import random

def randomnum():
    min_value = int(input("set minimum : "))
    max_value = int(input("set maximum : "))
    print("minimum = " + str(min_value))
    print("maximum = " + str(max_value))
    random_number = random.randint(min_value, max_value)
    
    return random_number
    
value = randomnum()
"""print(value)"""
    
def answer():
    player_answer = int(input("Your answer : "))
    if player_answer == value:
        print("You are winner")
        print("CONGRATULATION")
    else:
        print("You are miss")
        print("The correct answer is : " + str(value))

answer()