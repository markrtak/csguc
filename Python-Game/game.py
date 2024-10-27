import random 
bag1, bag2, bag3 = 10, 10, 10
turn = True
game_over = False
while not game_over:
    valid = True
    
    if turn:  # Player's turn
        bag = eval(input("select a bag: "))
        remove = eval(input("select number of objects: "))
    else:  # Computer's turn
        bag = random.randint(1, 3)
        min_val = 6
        if bag == 1 and bag1 < 5:
            min_val = bag1
        elif bag == 2 and bag2 < 5:
            min_val = bag2
        elif bag == 3 and bag3 < 5:
            min_val = bag3
        if min_val >= 5:
            min_val = 5
        remove = random.randint(1, min_val)
    if bag > 3 or bag < 1:
        print("please select a correct bag")
        valid = False
    if remove == 0:
        print("please enter a valid number")
        valid = False
    if remove > 5 or remove < 1:
        print("please enter a valid number")
        valid = False
    if (bag == 1 and remove > bag1) or (bag == 2 and remove > bag2) or (bag == 3 and remove > bag3):
        print("you cannot select this number")
        valid = False
    
    if valid:
        if bag == 1:
            bag1 -= remove
        elif bag == 2:
            bag2 -= remove
        elif bag == 3:
            bag3 -= remove
        if turn:
            player = "you"
        else:
            player = "computer"
        print(player, "took:", remove, "objects from bag:", bag)
        print(bag1, bag2, bag3)
        if bag1 == 0 and bag2 == 0 and bag3 == 0:
            game_over = True
            if turn:
                print("Computer wins")
            else:
                print("You win")
        turn = not turn
