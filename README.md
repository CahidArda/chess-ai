# Chess AI

In this project, I wrote a chess engine to simulate a chess. This chess engine was then used to generate a list of possible moves in any chess board state. The list of moves is used to construct a minimax tree and search for ideal moves.

## Future Plans

- Optimization: Currently, only optimization in the minimax search is alpha-beta tuning. Optimizations that can be applied are not limited to alpha-beta tuning however. One idea is to use hashing, chess board states can be hashed and searching moves for the same chess state multiple times can be avoided.
- MCTS: AI is set up with minimax tree search. But MCTS can be a better idea. I need to learn more about MCTS and implement an AI with MCTS
- Reinforcement Learning: Currently, chess boards are being evaluated with a simple hand-crafted function. I am planning to implement a reinforcement learning model to evaluate chess board states.
