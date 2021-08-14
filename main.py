
import json
import sys
from random import randint

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
    print("Score: %f" % board.score_for_next_player())
    print(" ---------------")

for i in range(10):
    board.reverse_last_move()

print("#########")
print(board)