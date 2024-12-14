import random
snake = {32:10, 60:14, 12:2, 78:24, 99:2}
lader = {13:33, 34:72, 23:91, 46:62, 50:80}

pos = {"p1":0, "p2":0}

def dice_roll():
    return random.randint(1,6)

def main(p):
    number = dice_roll()
    cnt = 1
    final_number = number
    while number == 6 :
        if cnt <3:
            cnt += 1
            number = dice_roll()
            final_number +=number 
        else:
            final_number = 0
            number = dice_roll()
            final_number = number
        
    pos_set(p, final_number)

def pos_set(p, number):
    if pos[p] + number <= 100:    
        pos[p] += number
        if pos[p] in snake:
            pos[p] = snake[pos[p]]
        elif pos[p] in lader:
            pos[p] = lader[pos[p]]
        
        print(f"postition of {p}: {pos[p]}")

while True:
    main("p1")
    main("p2")
    if pos["p1"] == 100:
        print(f"winner is p1")
        break
    
    if pos["p2"] == 100:
        print(f"winner is p2")
        break