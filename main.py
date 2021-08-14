
import json
import sys
from random import randint
from heuristics.positional_heuristic import positional_heuristic

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

for i in range(10):
    moves = board.get_moves_for_next_player()
    move = moves[randint(0, len(moves)-1)]
    board.apply_move(move)
    print("Applied %s" % move)
    print(board)
    piece_loc_tuples = board.get_piece_loc_tuples()
    print("Score: %f" % positional_heuristic(piece_loc_tuples, board.next_player, board.config))
    print(" ---------------")

for i in range(10):
    board.reverse_last_move()

print("#########")
print(board)