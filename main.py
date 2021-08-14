
import json
import sys
from random import randint
from heuristics.positional_heuristic import positional_heuristic
from board import Board

from heuristics.minimax import minimax
from heuristics.positional_heuristic import positional_heuristic


config = None

try:
    file = open("config.json")
    config = json.load(file)
    file.close()
except:
    print("ERROR: config file not found.")
    sys.exit()

board = Board()

for i in range(10):
    moves = board.get_moves_for_next_player()
    move = moves[randint(0, len(moves)-1)]
    board.apply_move(move)
    
print(board)
print(minimax(board, 3))
print(positional_heuristic(board))