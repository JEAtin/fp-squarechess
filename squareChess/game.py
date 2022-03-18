import chess
from chess import Chess
from player import Player
class Game():
    """This class holds information about the game."""

    def __init__(self):
        size = input("Please enter checkerboard size:")
        while True:
            try:
                self.size = int(size)
                break
            except:
                size = input("Input error, please re-enter:")

        self.chess = Chess(self.size)

        n = input("Please enter the number of players:")
        while True:
            try:
                self.n = int(n)
                break
            except:
                n = input("Input error, please re-enter:")

        self.players = []
        for i in range(self.n):
            self.players.append(Player(i))
            temp_p = self.players[i]

            change_symbol = input(f"{temp_p.name}: Whether to modify your chessman character ?(Y or N)")
            if change_symbol.lower() == 'y':
                chess_symbol = input("Please set new symbol as your chessman character (single character)")
                while True:
                    if chess_symbol == '-':
                        chess_symbol = input(f"{chess_symbol} is not allowed as a chessman character!")
                        continue
                    if len(chess_symbol) > 1:
                        chess_symbol = input(f"{chess_symbol} length is too long, please re-enter!")
                        continue
                    for p2 in self.players:
                        if p2.chess_symbol == chess_symbol:
                            chess_symbol = input(f"{chess_symbol} has used, please re-enter!")
                            continue
                    break
                temp_p.chess_symbol = chess_symbol

        self.help()
        print("Start your game!\n")
        self.over = False
        self.game_loop()

    def game_loop(self):
        while ~self.over:
            for p in self.players:
                self.chess.show()
                while True:
                    command = p.next_step()
                    try:
                        if command.lower() == 'help':
                            self.help()
                            continue
                        elif command.lower() == 'exit':
                            self.players.remove(p)
                            if len(self.players)==0:
                                self.game_over(self.players[0]);
                                return
                            break
                        else:
                            x,y = command.split(',')
                            x = int(x)
                            y = int(y)
                            if self.chess.chess_matrix[x][y] != '-':
                                print(f"{x},{y} are already chess pieces here")
                                continue
                            self.chess.move(x,y,p)
                            if self.chess.isWin(x,y,p):
                                self.game_over(p);
                                return
                            if self.chess.isTie():
                                print("Congratulations to draw~~~")
                                return
                            break
                    except:
                        print("Input error, please re-enter!")

    def help(self):

        print(f"\nAfter the game starts, {self.n} players play chess in order.\n"
              f"Players can input x,y to indicate the location of the pieces, the pieces can not overlap.\n"
              f"A player wins when his pieces form a 2-by-2 square.\n"
              f"When n-1 players exit the game, the last player wins.\n"
              f"A draw occurs when all positions on the board are matched\n")

    def game_over(self,p):
        print(f"Game over ~ {p.name} win!")