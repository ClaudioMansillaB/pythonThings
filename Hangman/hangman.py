import random

words = ['universidad']
word = random.choice(words)

attempts = 0
hidden_letter = ['_' for _ in range(len(word))]
hidden_letter_join = ' '.join(hidden_letter)
used_letters = []

while attempts < 10:

    print(hidden_letter_join)
    print('Guess the word letter by letter: ')

    letter = input()
    while letter in used_letters:
        print('Letter already used: ')
        letter = input()

    used_letters.append(letter)

    if letter in word:
        for pos in range(len(word)):
            if word[pos] == letter:
                hidden_letter[pos] = letter
        hidden_letter_join = ' '.join(hidden_letter)
    else:
        attempts += 1

    if '_' not in hidden_letter:
        print('You win!')
        print(word)
        break
    else:
        print('Used letters: '+ str(used_letters))
        print('Intentos restantes: '+str(10 - attempts))
    
    if attempts == 10:
        print('You lose, the word was: '+str(word))



    
