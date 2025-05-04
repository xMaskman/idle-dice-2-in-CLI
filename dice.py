import random
import time
import json

GLOBAL_GAME_STATE = False



upgrade = [
        10.0,
        100.0,
        1000.0,
        10000.0,
        100000.0,
     
    ]


level = [1,1,1,1,1]
availability_of_dice = [1,0,0,0,0]
number_of_dice1 = 1
GLOBAL_TOTAL_MONEY = 0
dice_roll = []
price = [100,100,1000,10000,100000]
average_roll_10 = []



def bad_fix(upgrade1,level1,dice,money1,average):
    global upgrade
    global level
    global availability_of_dice
    global GLOBAL_TOTAL_MONEY
    global average_roll_10

    upgrade = upgrade1
    level = level1
    availability_of_dice = dice 
    GLOBAL_TOTAL_MONEY = money1
    average_roll_10 = average

def  time_counter(previous_time):
    current_time = time.time()
    difference = current_time - previous_time
    save_game_data(difference)

def json_unpacker(): 
    save_state = False
    with open("gamesavadata.json","r") as read:
        save_date = json.load(read)
    if save_date["save_state"] == True:
        upgrade = save_date["upgrade"]
        level = save_date["level"]
        availability_of_dice = save_date["availability_of_dice"]
        GLOBAL_TOTAL_MONEY = save_date["GLOBAL_TOTAL_MONEY"]
        average_roll_10 = save_date["average_roll_10"]
        previous_time = save_date["last_login"]
        #It is a bad fix
        bad_fix(upgrade,level,availability_of_dice,GLOBAL_TOTAL_MONEY,average_roll_10)
        time_counter(previous_time)
        

def required_dice():
    if dice_status() == True:
        availability_of_dice.index(10)


def money():
    global GLOBAL_TOTAL_MONEY
    current_money = 0
    dice1 = dice_roll
    multiplier1 = multiplier(availability_of_dice,level)
    for i in range(len(dice1)):
        current_money = dice1[i] * multiplier1[i]
        GLOBAL_TOTAL_MONEY = current_money + GLOBAL_TOTAL_MONEY
    return GLOBAL_TOTAL_MONEY

def current_money():
    current_money = 0
    total_current_money = 0
    dice1 = dice_roll
    multiplier1 = multiplier(availability_of_dice,level)
    for i in range(len(dice1)):
        current_money = dice1[i] * multiplier1[i]
        total_current_money = total_current_money+current_money
    return total_current_money

def number_of_dice():
    t = 0
    for list in availability_of_dice:
        z = list
        t = z+t
    return t
    
def dice(manynumber):
    global dice_roll
    number = []
    for i in range(manynumber):
        numbers = random.randint(1,6)
        number.append(numbers)
    dice_roll = number  
    return number 

def dice_status():
    try:
        index = availability_of_dice.index(0) 
        index = index - 1
        if level[index] >= 10:
            return True
        else:
            message = "No"
            return message
    except ValueError:
        return False

def print_message(status):
    if status == True:
        yes = "yes"

        return yes
    elif status == "No":
        max = "You don't have enough level"
        return max
        
    else:
        no = "You have reached maximum number of dice"
        return no



def multiplier(list, multiplier):
    multiplied = []
    i = 0
    for lists in list: 
        multipliers = lists * multiplier[i]
        if multipliers > 0 :
            multiplied.append(multipliers)
        i += 1
    
    return multiplied



def upgrading():
    global GLOBAL_TOTAL_MONEY
    print(f""" 
1. Upgrade dice one level is {level[0]} and the price is {round(upgrade[0])}
2. Upgrade dice two level is {level[1]} and the price is {round(upgrade[1])}
3. Upgrade dice three level is {level[2]} and the price is {round(upgrade[2])}
4. Upgrade dice four level is {level[3]} and the price is {round(upgrade[3])}
5. Upgrade dice five level is {level[4]} and the price is {round(upgrade[4])}
""")
    try:
        user_input = input("Please select an option: ")
        user_input = int(user_input)
        user_input = user_input-1
        if GLOBAL_TOTAL_MONEY >= upgrade[user_input]:
            GLOBAL_TOTAL_MONEY = GLOBAL_TOTAL_MONEY - upgrade[user_input]
            upgrade[user_input] = round(upgrade[user_input] * 1.52)
            level[user_input] = level[user_input] + 1
    
        else :
            print("You don't have enough money to buy")
    except ValueError:
        print("Please enter a vaild key")

def average_roll(diceroll):
    if  current_money() > 0:
        average_roll_10.extend(dice_roll)
    total_count_of_dice = 0
    if len(average_roll_10) != 0:
        for roll in average_roll_10:
            total_count_of_dice = total_count_of_dice + roll
        average = total_count_of_dice / len(average_roll_10)
    if len(average_roll_10) >= 11:
        average_roll_10.pop(0)
        return average_roll_10

def total_average():
    
    total_roll = 0
    average_roll1 = 0
    if len(average_roll_10) >= 1:
        for rolls in average_roll_10:
            total_roll = total_roll + rolls
        average_roll1 = total_roll / len(average_roll_10)
    return average_roll1

def time_function(difference):
    global GLOBAL_TOTAL_MONEY
    times = difference / 5

    money = round(times * total_average())
    GLOBAL_TOTAL_MONEY = GLOBAL_TOTAL_MONEY + money
    return money

def save_game_data(difference):
    
    AVERAGE_ROLL =f" While you were gone, you earned this much money. {time_function(difference)}"
    print(AVERAGE_ROLL)

def global_variable_acceess(difference):
    
    AVERAGE_ROLL =f" While you were deciding, you earned this much money. {time_function(difference)}"
    print(AVERAGE_ROLL)

def dice_price():
    if number_of_dice() < 5 : 
        index = availability_of_dice.index(0)
        available_dice_price = price[index]
        return available_dice_price
    else:
        print("You have maximum amount of dice")

def buying_dice():
    global GLOBAL_TOTAL_MONEY
    index = availability_of_dice.index(0)
    print(f"The price of the dice is {price[index]}")
    if dice_status() == True:
        index = availability_of_dice.index(0)
        price1 = price[index]
        print(f"The price of the dice is {price1}")
        if GLOBAL_TOTAL_MONEY >= price1:
            GLOBAL_TOTAL_MONEY= GLOBAL_TOTAL_MONEY-price1
            availability_of_dice[index] = 1
        else: 
            print("You don't have enough money")
    return True
    
    
def game_switch(user_input):
    global GLOBAL_GAME_STATE
    if user_input == "1" :
        GLOBAL_GAME_STATE = True
    else : 
        GLOBAL_GAME_STATE = False
def end_game():
        global GLOBAL_GAME_STATE
        print("You have selected end game. Are you sure you want to end game? Y/N ")
        input1 = input()
        input1 = str(input1)
        input1 = input1.capitalize()
        if input1 == "Y":
            save_state = True
            last_time_login = time.time()
            game_data = {
    "save_state" : save_state,
    "upgrade": upgrade,
    "level": level,
    "availability_of_dice": availability_of_dice,
    "GLOBAL_TOTAL_MONEY": GLOBAL_TOTAL_MONEY,
    "average_roll_10": average_roll_10,
    "last_login": last_time_login,
}
            with open("gamesavadata.json","w") as save:
                json.dump(game_data,save)
                GLOBAL_GAME_STATE = False
        else: 
            return

def ui(): 
        average_roll(current_money())
        print(f"""
              
number of dice is {number_of_dice()}
Your dice roll are this {dice(number_of_dice())}
Multipliers = {multiplier(availability_of_dice,level)}
are you available to buy the next dice: {print_message(dice_status())}
""")
        
        
        
        print(f"""
              
money earned = {current_money()}
total money = {money()}
Option:
1. Upgrade dice
2. Buy dice 
3. Roll dice
4. End the game

                """),
        
        
            
        before_input = int(time.time())
        ingame_input = input()
        after_input = int(time.time())
        difference = after_input - before_input
        if difference >= 5:
            global_variable_acceess(difference)
            
        options.get(ingame_input, lambda: print("Option doesn't exist"))()
        
            


def messaging_system():
    
    user_input = input("""
        Do you want to start the game?
        Prese 1 to continue 
        Press 2 to cancel""")

    
    game_switch(user_input)
    while GLOBAL_GAME_STATE is True:
       ui()
       
        
    
options = {

            "1" : upgrading,
            "2" : buying_dice,
            "3" : ui,
            "4" : end_game,
            }
json_unpacker()
messaging_system()