
import json
import sys

config = None

try:
    file = open("config.json")
    config = json.load(file)
    file.close()
except:
    print("ERROR: config file not found.")
    sys.exit()

from games.checkers import CheckersGame
from board import Board

game = CheckersGame()
board = Board(game)
print(board)