
from board import Piece

import json

class Game:
    
    def __init__(self, configPath):
        with open(configPath) as file:
            self.config = json.load(file)