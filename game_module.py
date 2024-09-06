import random
"""
Module: game_module

Provides functions for a game of rock, paper, scissors, bomb.

Available functions:
    rock_paper_scissors(player_input, computer_input)
    computer_random()
"""

def rock_paper_scissors(player_input : str, computer_input : str) -> str:
    """
    Compares player and computer moves and returns who won the game or if its a tie.
    
    Args:
    player_input(string): string move of the player.
    computer_input(string): string move of the computer.

    Return:
    string: result of the game.
    """
    #dictionary showing the result based on player input and computer input
    results = { 'rock':{'scissors': 'Player', 'paper': 'Computer'},
                'paper': {'rock': 'Player', 'scissors': 'Computer'},
                'scissors': {'paper': 'Player', 'rock': 'Computer'}}
    
    #checks if its a tie
    if player_input == computer_input:
        return "it's a tie!"
    
    #checks if computer_input is BOMB
    if computer_input == 'BOMB':
        return 'Computer won, BOMB BLOWS EVERYTHING UP BWAWHAHWAHWHWAHWAAAHAHAHA!!!'
    
    #determines winner based on player and computer inputes
    elif player_input in results:
        winner = results[computer_input]
        if winner == 'Player':
            return f'Player won, {player_input} beats {computer_input}. Good job!'
        else:
            return f'Computer won, {computer_input} beats {player_input}. Good luck next time.'
        
def computer_random() -> str:
    """
    Randomly hooses a move for the computer from a list of specified moves.

    Return:
    string: move of the computer. 
    """    
    random_response = random.choice(['scissors','paper','rock','BOMB'])
    return random_response
