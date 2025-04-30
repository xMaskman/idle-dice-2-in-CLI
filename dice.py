import random

number_of_dice = 1

def dice(number_of_dice):
    number = []
    for i in range(number_of_dice):
        numbers = random.randint(1,6)
        number.append(numbers)
    
    return number 
list = dice(number_of_dice)

multiplyers = [1,1,1,1,1,1]

def multiplyer(list, multiplier):
    multiplied = []
    i = 0
    for lists in list: 
        multipliers = lists * multiplier[i]
        multiplied.append(multipliers)
        i += 1
    return multiplied

    


print(list)