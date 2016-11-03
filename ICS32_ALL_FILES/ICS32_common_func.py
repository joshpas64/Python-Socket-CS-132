###Joshua Pascascio ID: 52192782
### Heran Patel: 62984531


import connectfour
##Constants below to have less typing 
BOARD_ROWS = connectfour.BOARD_ROWS
BOARD_COLUMNS = connectfour.BOARD_COLUMNS
new_game = connectfour.new_game
drop = connectfour.drop
winner = connectfour.winner
pop = connectfour.pop
NONE = connectfour.NONE
RED = connectfour.RED
YELLOW = connectfour.YELLOW

def display_screen(game_state) -> None:
    """Function that displays the 7x6 board with all current moves updated, this function is usually called after every valid move call
    R is for red, Y is for Yellow, . is for no move yet made."""
    s = ""
    for i in range(1,8):
        s = s+ str(i) + "  "
    print(s)
    for row in range(BOARD_ROWS):
        row_String = ""
        for col in range(BOARD_COLUMNS):
            val = game_state.board[col][row]
            if val == NONE:
                row_String = row_String + ".  "
            elif val == RED:
                row_String = row_String + "R  "
            elif val == YELLOW:
                row_String = row_String + "Y  "
        print(row_String)
def read_move() -> list:
    """Displays input prompt for user to decide the column to drop or pop a circle, correct
    format id [DROP OR POP] then [COLUMN Number], also checks if input is valid, and wont return until input is valid"""
    try:
        move = input("PLease enter whether you want to DROP or POP and followed by column number:  ")
        move_Sets = move.split()
        while len(move_Sets) != 2:
            move = input("Please enter a column and whether to Drop or Pop:  ")
            move_Sets = move.split()
        col = int(move_Sets[1]) - 1
        action = move_Sets[0]
        action = action.lower()
        while ( action != "drop"  and action != 'pop'):
            return read_move()
        return [action,col]
    except ValueError:
        print("Invalid Move")
        return read_move()

def take_a_turn(starting_Game, moves: list) -> tuple:
    """Takes input from game board and read move output and determines if a winner has been made, if not
    the game will continue, returns NONE if game needs to continue"""
    try:
        if moves[0].lower() == 'drop':
            starting_Game = drop(starting_Game, moves[1])
        if moves[0].lower() == 'pop':
            starting_Game = pop(starting_Game, moves[1])
        victor = winner(starting_Game)
        return victor, starting_Game
    except ValueError:
        print("Invalid Move")
        inputs = read_move()
        return take_a_turn(starting_Game, inputs)
    except connectfour.GameOverError:
        print("The game is now over")
        return winner(starting_Game), starting_Game
    except connectfour.InvalidMoveError:
        print("Invalid Move")
        inputs = read_move()
        return take_a_turn(starting_Game,inputs)
