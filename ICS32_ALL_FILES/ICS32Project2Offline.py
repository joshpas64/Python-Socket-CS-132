###Joshua Pascascio ID: 52192782
### Heran Patel: 62984531

import connectfour
import ICS32_common_func


new_game = ICS32_common_func.new_game

NONE = ICS32_common_func.NONE
RED = ICS32_common_func.RED
YELLOW = ICS32_common_func.YELLOW

def determine_winner(winner:int)->None:
    """Output format for when a winner is determined"""
    if winner == RED:
        print("The winner is the red token")
    elif winner == YELLOW:
        print("The winner is the yellow token")
def playthrough() -> None:
    """Main interface for the offline game module, always creates a new game and keeps taking moves until a winner is made
    or game is over"""
    victor = NONE
    starting_Game = new_game()
    while (victor == NONE):
        inputs = ICS32_common_func.read_move()
        victor, starting_Game = ICS32_common_func.take_a_turn(starting_Game, inputs)
        ICS32_common_func.display_screen(starting_Game)
    determine_winner(victor)


if __name__ == '__main__':
    playthrough()
