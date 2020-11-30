from random import choice
print('Before you can proceed with this game, we need your name')
name = input('Enter your name: ').upper()

hangman_words = ['constipation','argument','monopoly','selfish','color','settle','chemistry','exercise',
                 'blessing','manual','science','warning','disturb','market','shuffle','marry','check']

word = choice(hangman_words)
hidden = []
for char in word:
    hidden.append('_')

num_of_attempts = 0
maximum_attempts = 4

game_over = False
print(f'WELCOME TO HANGMAN GAME {name}'.center(100))
while not game_over:
    print(f'\n\nyou have {maximum_attempts-num_of_attempts} attempts left')
    latest_guess = " ".join(hidden)
    print(f'The current word is {latest_guess}')
    

    print('  --------- ')
    print('   |       |')
    print('   |       ' +  ('O' if num_of_attempts > 0 else '' ))
    print('   |       ' + ('/\\' if num_of_attempts >= 1 else ''))
    print('   |       ' + (f'| {name.lower()} please save me!!!'  if num_of_attempts >= 2 else ''))
    print('   |       ' + ('/\\' if num_of_attempts >= 3 else ''))
    print('---------')
    
    guess_letter = input('Enter a letter: ')
    if guess_letter in word:
        print(f'you guessed rightly, {guess_letter} is in the word')
        for i in range(len(word)):
            character = word[i]
            if character == guess_letter:
                hidden[i] = word[i]
    else:
        print(f'you guessed wrong, {guess_letter} is NOT among')
        num_of_attempts += 1
    
    if '_' not in hidden:
        print(f'\n\nCongratulations {name}, you won!')
        game_over = True
    
    if (num_of_attempts >= maximum_attempts):
        print('Sorry! you lost, you could not save the man')
        break
        