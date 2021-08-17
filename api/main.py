
import json
import sys

from ai.minimax import minimax
from ai.heuristics.positional_heuristic import positional_heuristic
from game import *

config = None

try:
    file = open("config.json")
    config = json.load(file)
    file.close()
except:
    print("ERROR: config file not found.")
    sys.exit()

game = ChessGame((HeuristicPlayer(minimax), HeuristicPlayer(minimax)))
#game = ChessGame((HumanPlayer(), HeuristicPlayer(minimax)))
game.run_game(20)
