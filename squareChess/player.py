# player.py

class Player():
    """This class holds information about the player."""

    def __init__(self, number):
        self.name = "player " + chr(65+number)
        self.number = number
        self.chess_symbol = chr(65+number)

    def next_step(self):
        """Get the player's next step"""
        command = input(f"{self.name}: Please enter next - Move(x,y); View the game rules(help); Exit game(exit); ")
        return command
