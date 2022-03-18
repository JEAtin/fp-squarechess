# chess.py

from player import Player
import numpy as np

class Chess():
    """This class holds information about the chess."""

    def __init__(self, size):
        self.size = size
        self.chess_matrix = np.array([['-']*size]*size)
        pass

    def show(self):
        nums = [str(i) for i in range(self.size)]
        print(' ' * 3 + ' '.join(nums))
        for i in range(self.size):
            print(str(i) + ' '*2 + ' '.join(self.chess_matrix[i].tolist()))
        print()
        pass

    def isWin(self,x,y,player):
        if x-1>=0 and y-1>=0:
            if self.chess_matrix[x-1][y-1] == player.chess_symbol and self.chess_matrix[x-1][y] == player.chess_symbol \
                and self.chess_matrix[x][y-1] == player.chess_symbol:
                return True

        if x-1>=0 and y+1<self.size:
            if self.chess_matrix[x-1][y] == player.chess_symbol and self.chess_matrix[x-1][y+1] == player.chess_symbol \
                and self.chess_matrix[x][y+1] == player.chess_symbol:
                return True

        if y-1>=0 and x+1<self.size:
            if self.chess_matrix[x][y-1] == player.chess_symbol and self.chess_matrix[x+1][y-1] == player.chess_symbol \
                and self.chess_matrix[x+1][y] == player.chess_symbol:
                return True

        if x+1<self.size and y+1<self.size:
            if self.chess_matrix[x+1][y+1] == player.chess_symbol and self.chess_matrix[x+1][y] == player.chess_symbol \
                and self.chess_matrix[x][y+1] == player.chess_symbol:
                return True

        return False

    def isTie(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.chess_matrix[i][j] == '-':
                    return False
        return True

    def move(self,x,y,player):
        self.chess_matrix[x][y] = player.chess_symbol
        pass



