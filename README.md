# Tic-Tac-Toe with Q-Learning

This repository contains the implementation of a Q-learning based AI agent for playing Tic-Tac-Toe. The agent is trained to play as Player 2 (O), while Player 1 (X) plays randomly.

## Files

- `tictactoe_game.py`: Contains the main Tic-Tac-Toe game logic.
- `agent.py`: Contains the AI agent implementation using Q-learning.
- `tictactoe_main.py`: Main file to run the game and interact with the AI agent.

## AI Agent (`agent.py`)

### Overview

The `Agent` class extends the `Tictactoe` class and implements a Q-learning algorithm to train the AI to play Tic-Tac-Toe. The key components include:

- **Q-table**: Stores the Q-values for each state-action pair.
- **Epsilon-greedy policy**: Balances exploration and exploitation during training.
- **State transformations**: Considers rotations and mirror images of the board to generalize learning.

### Q-Learning

1. Resets the game.
2. Player 1 makes a random move.
3. The agent selects an action using the epsilon-greedy policy.
4. The agent takes the action and observes the reward and the next state.
5. Updates the Q-table for the current state-action pair.
6. Adds rotated and mirrored states to the Q-table with the same Q-values as the original state.
7. Repeats until the game is done.

### Running the Game

The main file `tictactoe_main.py` allows you to play against the trained AI agent. The AI agent will act as Player 2 (O), while you will play as Player 1 (X).
