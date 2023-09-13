import random

results = [['paper','rock'],['rock','scissors'],['scissors','paper']]

choices = ['rock','paper','scissors']

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper or scissors?: ").lower()

for elements in results:
    if player == computer:
        print('Computer election:', computer)
        print('Player election:', player)
        print('Tie!')
    elif player in elements and computer in elements:
        if elements.index(player) == 0:
            print('Computer election:', computer)
            print('Player election:', player)
            print('You win!')
        else:
            print('Computer election:', computer)
            print('Player election:', player)
            print('You lose!')








