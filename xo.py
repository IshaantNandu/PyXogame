import sys

class XO:
    def __init__(self,*args,**kwargs):
        self.board=['*','*','*','*','*','*','*','*','*']
        self.win=0
        self.player1='Player 1 (X)'
        self.player2='Player 2 (O)'
        self.iterCount=0
    def verify(self,array: list,*args,**kwargs):
        
        if len(array) != 9:
            raise(SyntaxWarning("Array in not 9 in length"))
        else:
            return array
    
    def isInt(self,string):
        try:
            y=int(string)  
            return True  
        except ValueError:
            return False  
    def numify(self,array:list,*args,**kwargs)->list:
        newlist=[]
        for i in array:
            if i == '*':
                newlist+=[0]
            elif i=='X':
                newlist+=[1]
            elif i=='O':
                newlist+=[2]
            else:
                raise(SyntaxWarning("Unknown character"))
        return newlist
        
    def checkRow(self,array:list,*args,**kwargs)->int:
        x=self.verify(array)
        if x[0]==x[3] and x[3]==x[6]:
            return x[0]
        elif x[1]==x[4] and x[4]==x[7]:
            return x[1]
        elif x[2]==x[5] and x[5]==x[8]:
            return x[2]
        else:
            return 0
        
    def checkColumn(self,array:list,*args,**kwargs)->int:
        x=self.verify(array)
        if x[0]==x[1] and x[1]==x[2]:
            return x[0]
        elif x[3]==x[4] and x[4]==x[5]:
            return x[3]
        elif x[6]==x[7] and x[7]==x[8]:
            return x[7]
        else:
            return 0
    def checkDiagonal(self,array:list,*args,**kwargs)->int:
        x=self.verify(array)
        if x[0]==x[4] and x[4]==x[8]:
            return x[0]
        elif x[2]==x[4] and x[4]==x[6]:
            return x[2]
        else:
            return 0
            
    def check(self,*args,**kwargs)->bool:
        draw=True
        array=self.numify(self.board)
        for i in array:
            if i==0:
                draw=False
            else:
                draw=True

        if self.checkRow(array)==1 or self.checkColumn(array)==1 or self.checkDiagonal(array)==1:
            self.win==1
            print(f'The winner is player 1')
            sys.exit()
            return False
        elif self.checkRow(array)==2 or self.checkColumn(array)==2 or self.checkDiagonal(array)==2:
            self.win==2
            print(f'The winner is player 2')
            sys.exit()
            return False
        elif draw==True:
            self.win==0
            print("The match is a draw")
            sys.exit()
            return False
        else:
            self.win==3
            return True
        
    def displayboard(self,*args,**kwargs):
        print("Board:")
        boardstr=''
        for index,i in enumerate(self.board):
            if index % 3 == 0 and index != 0 :
                boardstr+='\n'
            boardstr+=i
        print(boardstr)
    def chooseMove(self,play:bool,*args,**kwargs)->int:
        if play==False:
            player=self.player2
        else:
            player=self.player1
        print(f"{player}, choose your move-")
        possibleMoves=''
        moves=''
        possible=[]
        for index,i in enumerate(self.board):
            if i != '*':
                possibleMoves+='*'
            else:
                possibleMoves+=f'{str(index+1)}'
                possible+=[index+1]
        for i in range(len(possibleMoves)):
            if i%3==0 and i!=0:
                moves+='\n'
            moves+=possibleMoves[i]
        
        print(f'Possible moves- \n\r{moves}')
        self.displayboard()

        x=input()
        if self.isInt(x)==False:
            print(f"'{x}' Is invalid input, Please enter input again.")
            x=1
            if self.iterCount <1000:
                self.chooseMove(play)
            self.iterCount+=1
        y=int(x)
        if y not in possible and y > 0 and y < 10:
            print(f"Position number '{y}' already taken, Please enter input again.")
            if self.iterCount <1000:
                self.chooseMove(play)
            self.iterCount+=1
        if y not in possible:
            print(f"'{y}' Is invalid input, Please enter input again.")
            if self.iterCount <1000:
                self.chooseMove(play)
            self.iterCount+=1

        y-=1
        if play:
            self.board[y]='X'
        else:
            self.board[y]='O'


        
    def gameplay(self,*args,**kwargs):

        print("Welcome to Tic Tac Toe \n Player 1 is X, Player 2 is O")
        while self.check():
            self.chooseMove(True)
            if self.check():
                self.chooseMove(False)

        


            

    
x=XO()
x.gameplay()
            
            
        
