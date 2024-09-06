import game_module as gm

def main():
    #welcome message
    print("""Welcome to 'Rock, paper, scissors... BOMB!!!'
This game is a variation of a classical rock paper scissors game, but
with a slight change. The computer opponent has a random chance of
throwing a bomb into the game.
*********************************************************************
RULES
1. As a player the responses you can enter are: 'paper', 'rock' and 'scissors'. 
2. Be careful with your responses since the app is case sensitive. 
3. Have fun!\n""")
    #loop for the main game
    while True:
        #loop for user's response 
        while True:
            user_input = input('Enter your move here: ')
            if user_input in ['paper', 'rock', 'scissors']:#checks if user's response is valid 
                computer_input = gm.computer_random()
                print('\nYour move is', user_input, 'computer\'s move is', computer_input, '\n')
                print(gm.rock_paper_scissors(user_input, computer_input))
                break
            else:
                print('Ooooops that doesn\'t seem like a valid response. Please try again!')
                       
        #checks if the user wants to continue playing
        continue_game = input('\nWould you like to play another round? (Type yes or no): ')
        if continue_game == 'yes':
            pass
        elif continue_game == 'no':
            print('Thanks for playing the game!')
            break
        else:
            print('Invalid response. Game quits.')
            break









if __name__== "__main__":
    main()