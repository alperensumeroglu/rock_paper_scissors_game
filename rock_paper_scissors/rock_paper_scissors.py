"""
Rock-Paper-Scissors game
Random selections are made between the user and the computer:Rock, Paper ,or Scissors.
The user makes their choice as 1 (Rock), 2 (Paper), 3 (Scissors).
The computer makes a random choice.
Choices are printed on the screen and the winner is determined:
Rock crushes Scissors, Scissors cuts paper.
Paper covers Rock, Rock crushes Scissors.
Scissors cuts Paper, Paper covers Rock.
The winner is announced at the end of each round, and the user is aked if they want to play another game.
"""
import random
print('Welcome to Rock-Paper-Scissors game!')
print('Options: 1. Rock, 2. Paper, 3. Scissors')
while True:
   try:
        user_choice = int(input('Please make your choice(1/2/3): '))
        computer_choice = random.randint(1,3)
        options = ['Rock','Paper','Scissors']
        print(f'Your choice: {options[user_choice - 1]} -- Computer choice: {options[computer_choice - 1]}')
        if user_choice == computer_choice:
          print(f'It is a tie! Please try again.')
        elif (user_choice == 1 and computer_choice == 3) or\
             (user_choice == 2 and computer_choice == 1)or \
             (user_choice ==3 and computer_choice ==2 ):
           print('Congratulations! You won.')
        else:
           print('Sorry, Computer won.') 
        play_again = input('Would you like to play another game?(Yes/No):').lower()
        if play_again !='yes':
             break
   except ValueError:
      print('Please enter a valid number (1,2 or 3) for your choice.')
      