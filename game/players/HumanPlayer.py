from board import Move

class HumanPlayer:

    def __init__(self):
        pass

    def get_move(self, board):
        print(board)
        print("Time to make a move!")
        print("Please enter a move in the following format: x1 y1 x2 y2")
        move = [int(i) for i in input("Your move: ").split()]
        move = Move(move[0], move[1], move[2], move[3])
        return move