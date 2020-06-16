
class Draughts:
    def __init__(self):
        board = [
            [' ', 'r',' ','r',' ','r',' ','r'],
            ['r',' ','r',' ','r',' ','r',' '],
            [' ', 'r',' ','r',' ','r',' ','r'],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ',' ',' ',' ',' ',' ',' ',' '],
            [' ', 'b',' ','b',' ','b',' ','b'],
            ['b',' ','b',' ','b',' ','b',' '],
            [' ', 'b',' ','b',' ','b',' ','b']]
        self.board = board
        self.turn = 'blacks turn'
        self.print_board()
        print('')
        print(self.turn)
        print('')

    def print_board(self):
        print('  A B C D E F G H')
        i=1
        for row in self.board:
            print(f'{i}|{row[0]}|{row[1]}|{row[2]}|{row[3]}|{row[4]}|{row[5]}|{row[6]}|{row[7]}|')
            i+=1

    def available_moves(self,player):
        colSpots = 'ABCDEFGH'
        rowSpots = '12345678'
        if player == 'r':
            possibleMoves = []
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == 'r':
                        if (row!=len(self.board)-1)&(col!=len(self.board[0])-1):
                            if (self.board[row+1][col+1] ==' '):
                                possibleMoves.append((rowSpots[row]+colSpots[col],rowSpots[row+1]+colSpots[col+1]))
                        if (row!=len(self.board)-1)&(col!=0):
                            if (self.board[row+1][col-1] ==' '):
                                possibleMoves.append((rowSpots[row]+colSpots[col],rowSpots[row+1]+colSpots[col-1]))

        elif player == 'b':
            possibleMoves = []
            for row in range(len(self.board)):
                for col in range(len(self.board[0])):
                    if self.board[row][col] == 'b':
                        if (row!=0)&(col!=len(self.board[0])-1):
                            if (self.board[row-1][col+1] ==' '):
                                possibleMoves.append((rowSpots[row]+colSpots[col],rowSpots[row-1]+colSpots[col+1]))
                        if (row!=0)&(col!=0):
                            if (self.board[row-1][col-1] ==' '):
                                possibleMoves.append((rowSpots[row]+colSpots[col],rowSpots[row-1]+colSpots[col-1]))

        return possibleMoves

    def move(self,initPos,finPos,player):
        available = self.available_moves(player)
        if not (initPos,finPos) in available:
            print(initPos,'to',finPos,'is not a valid move.')
            return
        colSpots = 'ABCDEFGH'
        rowSpots = '12345678'

        initRow = rowSpots.find(initPos[0])
        initCol = colSpots.find(initPos[1])

        finRow = rowSpots.find(finPos[0])
        finCol = colSpots.find(finPos[1])


        self.board[initRow][initCol] = ' '
        self.board[finRow][finCol] = player

        if self.turn == 'blacks turn':
            self.turn = 'reds turn'
        elif self.turn == 'reds turn':
            self.turn = 'blacks turn'

        self.print_board()
        print('')
        print(self.turn)
        print('')

game = Draughts()

game.move('3B','4C','b')
