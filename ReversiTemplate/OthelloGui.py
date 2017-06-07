import tkinter
import ReversiLogic
DEFAULT_FONT = ('Helvetica', 20)
DIMENSION_OPTIONS = ('4','6','8','10','12','14','16')

##Name: Joshua Pascascio
##ID: 52192782
class Square:
    '''Tile Coordinate Object for the main GUI'''
    def __init__(self,x1,y1,x2,y2,fill):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.fill = fill
    def get_Point(self):
        '''Return tile's corner points'''
        return self.x1,self.x2,self.y1,self.y2
    def draw(self,canva):
        '''Draw main tiles of the board'''
        canva.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill = self.fill, outline = 'blue')
    def drawOval(self,canva,filler):
        '''Draw an oval within the tile'''
        canva.create_oval(self.x1,self.y1,self.x2,self.y2, fill = filler, outline = 'blue')
class App:
    def __init__(self):
        self.over = False
        self.COLOR = 'black'
        self.ranges = []
        self.circleCoord = []
    def make_Pattern(self,row: int, col: int)->str:
        '''Create an alternating pattern for the board'''
        if ((row % 2 ==0) and (col % 2 == 0)):
            return 'blue'
        elif ((row % 2 ==0) and (col % 2 == 1)):
            return 'red'
        elif ((row % 2 ==1) and (col % 2 == 0)):
            return 'red'
        elif ((row % 2 ==1) and (col % 2 == 1)):
            return 'blue'
    def drawBoard(self):
        '''Draw the board on initialization or on redraw when resizing'''
        yscale = self.canva.winfo_height()/self.rowCount
        xscale = self.canva.winfo_width()/self.colCount
        x = 0
        y = 0
        xnew = xscale
        ynew = yscale
        for e in range(self.rowCount):
            colRange = []
            for i in range(self.colCount):
                square_Fill = self.make_Pattern(e,i)
                sq = Square(x,y,xnew,ynew,square_Fill)
                sq.draw(self.canva)
                if self.circleCoord[e][i] != 0:
                    sq.drawOval(self.canva,self.circleCoord[e][i])
                colRange.append(sq)
                x =  xnew
                xnew += xscale
            self.ranges.append(colRange)
            x=0
            xnew = xscale
            y = ynew
            ynew += yscale
    def startGame(self):
        '''Start Game after the dimensions from input form has been submitted'''
        self.window = tkinter.Tk()
        self.blackCount = tkinter.StringVar()
        self.blackCount.set('Black Count: 2')
        self.whiteCount = tkinter.StringVar()
        self.whiteCount.set('White Count: 2')
        self.player = tkinter.StringVar()
        self.player.set('TURN: ' + self.setPlayerLabel(self.othello.current_player))
        self.canva = tkinter.Canvas( master = self.window, width = 500, height = (float(self.rowCount) / self.colCount)*500, background = '#006000')
        self.canva.grid(row = 0, column = 0, rowspan = 3,padx = 10, pady  = 10, sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)
        self.canva.bind('<Button-1>',self.motionFunc)
        self.canva.bind('<Configure>',self.resize)
        self.frame = tkinter.Frame(master = self.window)
        self.frame.grid(row = 0, column = 1, padx = 0, pady = 0, sticky = tkinter.E + tkinter.W + tkinter.S + tkinter.N)
        self.ruleLabel = tkinter.Label(master  = self.frame, text = 'Rules: Full', font= DEFAULT_FONT)
        self.ruleLabel.grid(row = 0, column = 0, padx = 10, pady =20, sticky = tkinter.N + tkinter.W)
        self.blackTileLabel = tkinter.Label(master = self.frame,textvariable = self.blackCount, font = DEFAULT_FONT)
        self.blackTileLabel.grid(row = 1, column = 0, padx = 10, pady = 20, sticky = tkinter.N + tkinter.W)
        self.whiteTileLabel = tkinter.Label(master = self.frame, textvariable = self.whiteCount, font = DEFAULT_FONT).grid(row = 2, column = 0, padx = 10, pady = 20, sticky = tkinter.N + tkinter.W)
        self.playerLabel = tkinter.Label(master = self.frame, textvariable = self.player, font = DEFAULT_FONT).grid(row = 3, column = 0, padx = 10, pady = 20, sticky = tkinter.N + tkinter.W)
        self.drawBoard()
        self.window.rowconfigure(0, weight = 1)
        self.window.columnconfigure(0, weight = 1)
    def resize(self, event: tkinter.Event):
        '''Delete and redraw the whole board when parent window is resized'''
        self.ranges = []
        self.canva.delete(tkinter.ALL)
        self.drawBoard()
    def setDimensions(self):
        '''Create input form to initialize the GUI Othello game and submit its results'''
        self.initWindow = tkinter.Frame(self.firstWindow)
        title_Label = tkinter.Label(master = self.initWindow, text = 'Please set your Othello parameters', font = DEFAULT_FONT)
        title_Label.grid(row = 0, column = 0, columnspan = 3, padx = 20, pady = 20)
        row_Label = tkinter.Label(master = self.initWindow, text = 'How many rows?',anchor = 'w', font = DEFAULT_FONT)
        row_Label.grid(row = 1, column = 0, padx = 10, pady = 20,sticky=tkinter.W)
        self.row_Spinbox = tkinter.Spinbox(master = self.initWindow, values = DIMENSION_OPTIONS)
        self.row_Spinbox.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 20)
        col_Label = tkinter.Label(master = self.initWindow, text = 'How many columns?', font = DEFAULT_FONT)
        col_Label.grid(row = 2, column = 0, padx = 10, pady = 20,sticky=tkinter.W)
        self.col_Spinbox = tkinter.Spinbox(master = self.initWindow, values = DIMENSION_OPTIONS)
        self.col_Spinbox.grid(row = 2, column = 1, columnspan = 2,padx = 10, pady = 20)
        firstP_Label = tkinter.Label(master = self.initWindow, text = 'Who shall play first?', font = DEFAULT_FONT)
        firstP_Label.grid(row = 3, column = 0, padx = 10, pady = 20,sticky=tkinter.W)
        self.firstChoiceString = tkinter.StringVar()
        first_Choice = tkinter.Radiobutton(master = self.initWindow, text = 'Black',variable = self.firstChoiceString, value = 'black')
        first_Choice.grid(row = 3, column = 1, padx = 10, pady = 5)
        first_Choice.select()
        second_Choice = tkinter.Radiobutton(master = self.initWindow, text = 'White',variable = self.firstChoiceString, value = 'white')
        second_Choice.grid(row = 3, column = 2, padx = 10, pady = 5)
        secondP_Label = tkinter.Label(master = self.initWindow, text = 'Who will be in the top left', font = DEFAULT_FONT)
        secondP_Label.grid(row = 4, column = 0, padx = 10, pady = 20)
        self.secondChoiceString = tkinter.StringVar()
        second_Choice2 = tkinter.Radiobutton(master = self.initWindow, text = 'Black',variable = self.secondChoiceString, value = 'black')
        second_Choice2.grid(row = 4, column = 1, padx = 10, pady = 5)
        second_Choice2.select()
        second_Choice3 = tkinter.Radiobutton(master = self.initWindow, text = 'White',variable = self.secondChoiceString, value = 'white')
        second_Choice3.grid(row = 4, column = 2, padx = 10, pady = 5)
        final_Choice_Label = tkinter.Label(master=self.initWindow, text = 'How does one win?', font = DEFAULT_FONT)
        final_Choice_Label.grid(row = 5, column = 0 , padx =10, pady = 20, sticky = tkinter.W)
        self.thirdChoiceString = tkinter.StringVar()
        finalRadiobutton1 = tkinter.Radiobutton(master = self.initWindow, text = '>', variable = self.thirdChoiceString, value = '>')
        finalRadiobutton1.grid(row = 5, column = 1, padx=10, pady=5)
        finalRadiobutton1.select()
        finalRadiobutton2 = tkinter.Radiobutton(master = self.initWindow, text = '<', variable = self.thirdChoiceString, value = '<')
        finalRadiobutton2.grid(row = 5, column = 2, padx = 10, pady = 20)
        submit = tkinter.Button(master = self.initWindow, text = 'Submit', font = DEFAULT_FONT, command = self.submitDimensions)
        submit.grid(row = 6, column = 0, columnspan = 3, pady = 20)
        self.initWindow.pack(expand=True, fill = 'both')
        self.firstWindow.rowconfigure(0, weight = 1)
        self.firstWindow.columnconfigure(0, weight = 1)
    def checkInput(self, inputs):
        '''Checks to make sure row and column dimensions are in specified range'''
        try:
            num = int(inputs)
            if ((num >= 4) and (num <= 16) and (num%2 == 0)):
                return True
            return False
        except TypeError:
            return False
    def submitDimensions(self):
        '''Submit the values from the input form to initialize the Othello game'''
        self.rowCount = self.row_Spinbox.get()
        self.colCount = self.col_Spinbox.get()
        while((self.checkInput(self.rowCount) == False) or (self.checkInput(self.colCount) == False)):
            return
        self.rowCount = int(self.rowCount)
        self.colCount = int(self.colCount)
        self.firstPlay = self.firstChoiceString.get()
        self.topPlay = self.secondChoiceString.get()
        self.winFactor = self.thirdChoiceString.get()
        self.firstWindow.destroy()
        self.circleCoord = []
        for i in range(self.rowCount):
            colRange = []
            for e in range(self.colCount):
                colRange.append(0)
            self.circleCoord.append(colRange)
        self.othello = ReversiLogic.Othello(self.rowCount,self.colCount, self.firstPlay[0].upper(),self.topPlay[0].upper(),self.winFactor)
        self.startGame()
        self.COLOR = self.firstPlay
        self.updateTiles()
    def checkRange(self,x,y,point):
        '''Check if the an events coordinates is in a tile on the canvas'''
        if x>=point.get_Point()[0] and x<=point.get_Point()[1]:
            if y>=point.get_Point()[2] and y<=point.get_Point()[3]:
                return True
        return False
    def motionFunc(self,event: tkinter.Event):
        '''Make a move on the tile when clicked and valid'''
        for i in range(len(self.ranges)):
            for e in range(len(self.ranges[i])):
                if self.checkRange(event.x,event.y,self.ranges[i][e]) == True:
                    if self.circleCoord[i][e] == 0:
                        valid = self.othello.make_move(i,e,self.COLOR[0].upper())
                        if valid == 0:
                            self.updateTiles()
                            self.setTileColor(self.othello.current_player)
                            bcount,wcount = self.othello.count_pieces()
                            self.blackCount.set('Black Count: ' + str(bcount))
                            self.whiteCount.set('White Count: ' + str(wcount))
                            if self.othello.check_game_State(self.othello.current_player) != -1:
                                self.player.set('TURN: ' + self.setPlayerLabel(self.othello.current_player))
                            else:
                                self.setWinner()
                            self.ranges = []
                            self.drawBoard()
    def setWinner(self):
        '''Set the winner by changing the player label and create retry form'''
        self.player.set('GAME OVER \n' + self.othello.find_winner(self.winFactor))
        self.retry_window = tkinter.Toplevel()
        prompt_Label = tkinter.Label(master= self.retry_window, text = 'Play another game ?', font = DEFAULT_FONT)
        prompt_Label.grid(row = 0, column = 0, columnspan = 2, padx = 10, pady = 10)
        yesButton = tkinter.Button( master = self.retry_window, text = 'YES', font = DEFAULT_FONT, command = self.newGame)
        yesButton.grid(row = 1, column = 0, padx = 10, pady = 10)
        noButton = tkinter.Button(master = self.retry_window, text = 'NO', font = DEFAULT_FONT, command = self.closeGame)
        noButton.grid(row = 1, column = 1, padx = 10, pady = 10)
    def newGame(self):
        '''Makke a new game and recreate input form'''
        self.window.destroy()
        self.start()
    def closeGame(self):
        '''Close the window and end game'''
        self.window.destroy()

    def setPlayerLabel(self, move:str):
        '''Change the current player label upon a move made'''
        if move == 'B':
            return 'Black'
        else:
            return 'White'
    def setTileColor(self, move:str):
        '''Set the oval color when a move is a made'''
        if move == 'B':
            self.COLOR = 'black'
        else:
            self.COLOR = 'white'
    def updateTiles(self):
        '''Update the the circle coordinate list to correspond with the othello board'''
        for i in range(len(self.othello.board)):
            for e in range(len(self.othello.board[i])):
                if self.othello.board[i][e] == 'B':
                    self.circleCoord[i][e] = 'black'
                elif self.othello.board[i][e] == 'W':
                    self.circleCoord[i][e] = 'white'     
    def start(self):
        '''Start the othello game and create the input form to begin the game'''
        self.firstWindow = tkinter.Tk()
        self.setDimensions()
if __name__ == '__main__':
    app = App()
    app.start()
