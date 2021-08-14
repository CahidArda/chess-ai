
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

from board import Board

board = Board()
print(board)
board.get_all_possible_moves()