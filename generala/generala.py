import random

def new_dices(current_dices):

    dices = [1,2,3,4,5,6]

    list_options = list(list_options)
    change_dices = []

    for number in list_options:
        if number != ',':
            change_dices.append(int(number)-1)
    
    for number in range(6):
        if number in change_dices:
            current_dices[number] = random.choice(dices)
        
    return current_dices


def is_ladder(dices):
    options = [[1,2,3,4,5],[2,3,4,5,6],[1,3,4,5,6]]
    if dices in options:
        return True
    else:
        return False
    
def is_full(dices):
    unique_dices = list(set(dices))
    if len(unique_dices) == 2:
        if dices.count(unique_dices[0]) == 3 and dices.count(unique_dices[1]) == 2 or dices.count(unique_dices[0]) == 2 and dices.count(unique_dices[1]) == 3:
            return True
        else:
            return False  
    else:
        return False

def is_poker(dices):
    unique_dices = list(set(dices))
    if len(unique_dices) == 1:
        return True
    elif len(unique_dices) == 2:
        if dices.count(unique_dices[0]) == 4 or dices.count(unique_dices[1]) == 4:
            return True
        else:
            return False
    else:
        return False

def is_generala(dices):
    if len(list(set(dices))) == 1:
        return True
    else:
        return False
    
def sum_points(dices,antique_dices,made_changes,used_options):

    turn_points = 0

    print('what do you want to sum? first, second o current dices (type 1,2 or 3)')
    what_sum = int(input())

    if what_sum == 2:
        dices = antique_dices[1]
    elif what_sum == 1:
        dices = antique_dices[0] #Escribir fuera, igual que la doble generala

    options = ["1. Sum of 1's","2. Sum of 2's","3. Sum of 3's","4. Sum of 4's","5. Sum of 5's","6. Sum of 6's",
              '7. Ladder','8. Full','9. Poker','10. Generala' ]

    print('in what categorie do you want to sum your points?')
    for option in range(len(options)):
        if options[option] != used_options[option]:
            print(options[option]) 

    categorie = int(input())

    if categorie > 0 and categorie < 7:
        turn_points += categorie * dices.count(categorie)
        used_options[categorie - 1] = options[categorie - 1]
        return turn_points,used_options
    
    elif categorie == 7:
        if is_ladder(dices) == True:
            if made_changes == False:
                turn_points += 25
            else:
                turn_points += 20
            used_options[categorie - 1] = options[categorie - 1] 
            return turn_points,used_options
        else:
            print('There is no valid ladder, choose another categorie')
            tur_points,used_options = sum_points(dices,antique_dices,made_changes)

    elif categorie == 8:
        if is_full(dices) == True:
            if made_changes == False:
                turn_points += 35
            else:
                turn_points += 30
            used_options[categorie - 1] = options[categorie - 1]
            return turn_points,used_options 
        else:
            print('There is no valid full, choose another categorie')
            turn_points,used_options = sum_points(dices,antique_dices,made_changes)

    elif categorie == 9:
        if is_poker(dices) == True:
            if made_changes == False:
                turn_points += 45
            else:
                turn_points += 40
            used_options[categorie - 1] = options[categorie - 1]
            return sum_points,used_options 
        else:
            print('There is no valid poker, choose another categorie')
            turn_points,used_options = sum_points(dices,antique_dices,made_changes)
    elif categorie == 10:
        if is_generala(dices) == True:
            if made_changes == False:
                turn_points += 10000000
            else:
                turn_points += 50
            used_options[categorie - 1] = options[categorie - 1]
            return sum_points,used_options 
        else:
            print('There is no valid poker, choose another categorie')
            turn_points,used_options = sum_points(dices,antique_dices,made_changes)

    
dices = [1,2,3,4,5,6]

dices = [5,5,5,4,1]

antique_dices = []

points = 0
used_options = [0 for _ in range(10)]
for _ in range(10):
    #generala_numbers = 0
    current_dices = [random.choice(dices) for _ in range(5)]
    print('Current dices: ' + str(current_dices))
    antique_dices = []
    print('Do you want to change some dices?')
    print('If yes, Type the position of number that do you want to change (1-6): (example: 1,2,3)')
    print('If no, just type no')
    list_options = input().upper()

    if list_options == 'NO':
        made_changes = False
        turn_points, used_options_turn = sum_points(dices,antique_dices,made_changes,used_options)
    else:
        made_changes = True
        antique_dices.append(current_dices)
        current_dices= new_dices(current_dices)
        print('Do you want to change some dices again?')
        print('If yes, Type the position of number that do you want to change (1-6): (example: 1,2,3)')
        print('If no, just type no')
        if list_options == 'NO':
            turn_points, used_options_turn = sum_points(dices,antique_dices,made_changes,used_options)
        else:
            antique_dices.append(current_dices)
            current_dices = new_dices(current_dices)
            turn_points, used_options_turn = sum_points(dices,antique_dices,made_changes,used_options)

    print(current_dices)
    
    
    points += turn_points

    for op in range(len(used_options_turn)):
        if used_options_turn[op] != 0:
            used_options[op] = used_options_turn[op]




