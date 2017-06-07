import ReversiLogic

### Name: Joshua Pascascio
#### ID: 52192782


def check_range(dimension:int)->bool:
    ''' Checks that the range of inputs meets the dimension requirements'''
    if ((dimension>=4) and (dimension<=16) and (dimension%2 == 0)):
        return True
    return False
def start_game():
    '''Starts the game, gets called if in main call'''
    while True:
        try:
            valid_tiles = [ReversiLogic.BLACK , ReversiLogic.WHITE]
            rows = int(input())
            while (check_range(rows) == False):
                rows = int(input())
            cols = int(input())
            while (check_range(cols) == False):
                cols = int(input())
            first_player = input()
            first_player = first_player.strip().upper()
            while (first_player not in valid_tiles):
                first_player = input()
                first_player = first_player.strip().upper()
            top_player = input()
            top_player = top_player.strip().upper()
            while ((top_player not in valid_tiles)):
                top_player = input()
                top_player = top_player.strip().upper()
            token = input()
            token = token.strip()
            while ((token != '>') and (token != '<')):
                token = input()
                token = token.strip()
            break
        except ValueError:
            pass
    return rows,cols,first_player,top_player,token
def prompt_move():
    '''Takes input from the console and feeds into the reversi logic game object'''
    while True:
        try:
            moves = input()
            movesList = moves.split()
            row = int(movesList[0]) - 1
            col = int(movesList[1]) - 1
            return [row,col]
        except ValueError:
            print("INVALID")
        except IndexError:
            print("INVALID")
def interface():
    '''Main user interface of the Othello game is where Othello game object gets instantiated'''
    print("FULL")
    inputs = start_game()
    Othello1 = ReversiLogic.Othello(*inputs)
    Othello1.print_board(Othello1.board)
    print("Current Player:  " + Othello1.current_player)
    while (Othello1.check_game_State(Othello1.current_player) != -1):
        try:
            dimensions = prompt_move()
            x = Othello1.make_move(dimensions[0],dimensions[1],Othello1.current_player)
            Othello1.print_board(Othello1.board)
            if x == 1:
                print("Invalid")
            else:
                print("Current Player:  " + Othello1.current_player)
        except IndexError:
            dimensions = prompt_move()
            Othello1.make_move(dimensions[0],dimensions[1],Othello1.current_player)
if __name__ == '__main__':
    interface()
