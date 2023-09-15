import random

def new_dices(current_dices):

    dices = [1,2,3,4,5,6]

    print('Do you want to change some dices?')
    print('If yes, Type the position of number that do you want to change (1-6): (example: 1,2,3)')
    print('If no, just type no')
    list_options = input().upper()
    if list_options != 'NO':
        list_options = list(list_options)
        change_dices = []

        for number in list_options:
            if number != ',':
                change_dices.append(int(number)-1)
        
        for number in range(6):
            if number in change_dices:
                current_dices[number] = random.choice(dices)
    else:
        print('Keeping numbers and pass turn')
    
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
    
dices = [1,2,3,4,5,6]


for _ in range(10):
    current_dices = [random.choice(dices) for _ in range(5)]

    current_dices = new_dices(current_dices)

