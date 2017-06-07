BLACK = 'B'
WHITE = 'W'
### Name: Joshua Pascascio
#### ID: 52192782

##Same Logic File only with the print statements edited or deleted out

class Othello:
    '''Unique Othello game between two players, is called and instantiated from a main interface'''
    def __init__(self, rows:int, cols: int, first_player: str, top_player: str,token:str):
        self.rows = rows
        self.cols = cols
        self.board = []
        self.current_player = top_player
        self.token = token
        for i in range(rows):
            self.board.append([])
            for e in range(cols):
                self.board[i].append('.')
        self._find_center()
        self.current_player = first_player
        self.b_Valid_Moves = self.find_Valid_moves(BLACK)
        self.w_Valid_Moves = self.find_Valid_moves(WHITE)
        self.has_winner = 0
    def _find_center(self):
        '''Part of instantiation process, finds the center of the board and sets tiles accordingly'''
        centerX = int((self.cols/2)) - 1
        centerY = int((self.rows/2)) -1
        self.board[centerY][centerX] = self.current_player
        self.board[centerY+1][centerX+1] = self.current_player
        self.switch_player()
        self.board[centerY][centerX+1] = self.current_player
        self.board[centerY+1][centerX] = self.current_player
    def apply_Reversal(self,row,col,xScale,yScale):
        '''Reverses the tiles of a certain in a certain coordinate in a specified direction'''
        rcol = xScale
        tRow = yScale
        while ((self.board[row+tRow][col + rcol] == self.getOpposite(self.current_player))):
            self.board[row+tRow][col + rcol] = self.current_player
            rcol = rcol + xScale
            tRow = tRow + yScale
    def _is_filled(self):
        '''Checks if board is completely filled Black or White tiles'''
        for i in self.board:
            for e in i:
                if e == '.':
                    return False
        return True
    def find_winner(self, token)->str:
        '''Counts the remaining pieces and determines a winner based on token'''
        stats = self.count_pieces()
        if stats[0] > stats[1]:
            if token == '>':
                return 'WINNER: BLACK'
            else:
                return 'WINNER: WHITE'
        elif stats[0] < stats[1]:
            if token == '>':
                return 'WINNER: WHITE'
            else:
                return 'WINNER: BLACK'
        else:
            return "WINNER: NONE"
    def _check_board(self, move_list, opponent_list)->int:
        '''Checks the board to see if current player can make a valid move or if game is over'''
        if (((len(move_list) == 0) and (len(opponent_list) == 0)) or (self.is_filled() == True)):
            self.find_winner()
            return 0
        elif ((len(move_list) == 0)):
            self.switch_player()
            return 1
    def _renew_Valid_Moves(self,player):
        '''Renews the set of valid moves for each player each time the board is updated'''
        if (player == BLACK):
            move_list = self.b_Valid_Moves
            opponent_list = self.w_Valid_Moves
        else:
            move_list = self.w_Valid_Moves
            opponent_list = self.b_Valid_Moves
        return (move_list,opponent_list)
    def check_game_State(self,player):
        '''Checks the game to see if game is over or not'''
        new_Moves = self._renew_Valid_Moves(player)
        move_list = new_Moves[0]
        opponent_list = new_Moves[1]
        if (((len(move_list) == 0) and (len(opponent_list) == 0)) or (self._is_filled() == True)):
            self.find_winner(self.token)
            return -1
        elif ((len(move_list) == 0)):
            self.switch_player()
            return 0
        return 1
    def make_move(self,row, col, player):
        '''Makes a move if it is valid and applies reversals if possible'''
        reversals = self._is_Valid(row,col,player)
        if reversals == []:
            return 1
        self.board[row][col] = player
        for i in reversals:
            self.apply_Reversal(row,col,i[0],i[1])
        ##Check for winner or end game state
        self.b_Valid_Moves = self.find_Valid_moves(BLACK)
        self.w_Valid_Moves = self.find_Valid_moves(WHITE)
        self.switch_player()
        self.check_game_State(self.current_player)
        return 0
    def _is_Valid(self,row,col,player):
        '''Checks if a move is valid'''
        if (player == BLACK):
            moveList = self.b_Valid_Moves
        else:
            moveList = self.w_Valid_Moves
        for i in moveList:
            if [col,row] == i[0]:
                return i[1]
        return []
    def switch_player(self):
        '''Switches the current player'''
        if self.current_player == BLACK:
            self.current_player = WHITE
        else:
            self.current_player = BLACK
    def getOpposite(self,player):
        '''Returns the opposite of the current player but leaves the current player attribute unchanged'''
        if player == BLACK:
            return WHITE
        else:
            return BLACK
    def count_pieces(self):
        b_count = 0
        w_count = 0
        for i in self.board:
            for e in i:
                if e == BLACK:
                    b_count += 1
                elif e == WHITE:
                    w_count += 1
        return b_count,w_count
    def _check_adjacent(self,row,col,player)->bool:
        '''Checks the adjacent rows in all directions if a tile is opposite to the current move'''
        if (row - 1 > -1):
            if ((self.board[row - 1][col] == self.getOpposite(player))):
                return True
            if (col - 1 > -1):
                if ((self.board[row - 1][col - 1] == self.getOpposite(player)) or (self.board[row][col - 1] == self.getOpposite(player))):
                    return True
            if (col + 1 < self.cols):
                if ((self.board[row - 1][col + 1] == self.getOpposite(player)) or (self.board[row][col + 1] == self.getOpposite(player))):
                    return True
        if (row + 1 < self.rows):
            if((self.board[row+1][col] == self.getOpposite(player))):
                return True
            if(col - 1 > -1):
                if ((self.board[row+1][col-1] == self.getOpposite(player))):
                    return True
            if (col + 1 < self.cols):
                if ((self.board[row+1][col + 1] == self.getOpposite(player))):
                    return True
        return False
    def _check_Direction(self,row,col,xScale,yScale,player)->bool:
        '''Intended to be private data, checks if a reversal can be made in a given direction. X and Y Scale can only be -1 or 0 or 1'''
        result = False
        rcol = xScale
        tRow = yScale
        orig_Rcol = rcol
        orig_Trow = tRow
        while ((row + tRow < self.rows) and (col + rcol < self.cols) and (row + tRow > -1) and (col + rcol > -1 ) and (self.board[row+tRow][col + rcol] == self.getOpposite(player))):
            rcol = rcol + xScale
            tRow = tRow + yScale
        if (((col + rcol > -1) and (col + rcol < self.cols)) and ((row + tRow > -1) and (row + tRow < self.rows)) and (self.board[row+tRow][col+rcol] == player)):
            if ((rcol != orig_Rcol) or (tRow != orig_Trow)):
                result = True  
        return result
    def _is_Reversable(self,row,col,player)->list:
        '''Checks if a move can reverse any adjacent pieces according to the rules'''
        direction_list = []
        if self._check_Direction(row,col,1,1,player) == True:
            direction_list.append([1,1])
        if self._check_Direction(row,col,1,0,player) == True:
            direction_list.append([1,0])
        if self._check_Direction(row,col,-1,0,player) == True:
            direction_list.append([-1,0])
        if self._check_Direction(row,col,-1,-1,player) == True:
            direction_list.append([-1,-1])
        if self._check_Direction(row,col,0,1,player) == True:
            direction_list.append([0,1])
        if self._check_Direction(row,col,0,-1,player)== True:
            direction_list.append([0,-1])
        if self._check_Direction(row,col,1,-1,player) == True:
            direction_list.append([1,-1])
        if self._check_Direction(row,col,-1,1,player) == True:
            direction_list.append([-1,1])
        return direction_list
        
    def find_Valid_moves(self,player)->list:
        '''Creates a valid move list from the current game state'''
        move_List = []
        ##Check all free spaces that can be matched with an adjacent opposite tile
        for i in range(self.rows):
            for e in range(self.cols):
                if ((self.board[i][e] == '.') and (self._check_adjacent(i,e,player) == True)):
                    reversal_List = self._is_Reversable(i,e,player)
                    if len(reversal_List) > 0:
                        #Check if a reversal can be made in any direction if true add to valid move list
                        move_List.append([[e,i],reversal_List])                
        return move_List
    def print_board(self, game_board):
        rows = len(game_board)
        cols = len(game_board[0])
        for i in game_board:
            baseStr = ""
            for e in i:
                baseStr += e
            print(baseStr)
        

        
        
