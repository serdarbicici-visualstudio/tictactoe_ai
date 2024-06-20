from tictactoe_game import Tictactoe
from agent import Agent

if __name__ == "__main__":
    # read the q_table from the file and use it to play the game
    agent = Agent()
    agent.load_q_table()

    # play the game with the human
    agent.play_with_human()
    