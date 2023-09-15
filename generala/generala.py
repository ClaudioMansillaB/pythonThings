import random

def new_dices(current_dices):

    dices = [1,2,3,4,5,6]

    print('Do you want to keep some dices?')
    print('If yes, Type the position of number that do you want to keep (1-6): (example: 1,2,3)')
    print('If no, just type no')
    list_options = input().upper()
    if list_options != 'NO':
        list_options = list(list_options)
        keep_dices = []

        for number in list_options:
            if number != ',':
                keep_dices.append(int(number)-1)
        
        for number in range(6):
            if number not in keep_dices:
                current_dices[number] = random.choice(dices)
    else:
        print('Keeping numbers and pass turn')
    
    return current_dices


def is_ladder(dices):
    
dices = [1,2,3,4,5,6]

current_dices = [random.choice(dices) for _ in range(6)]
#print(current_dices)

current_dices = new_dices(current_dices)
#print('---------')
#print(current_dices)
