from tictactoe_game import Tictactoe
import random

class Agent(Tictactoe):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.q_table = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        self.state = None
        self.action = None
        #self.reward = None
        self.next_state = None
        self.done = None
        
    def reset(self):
        super().reset()
        self.state = None
        self.action = None
        #self.reward = None
        self.next_state = None
        self.done = None

    def get_state(self):
        return "".join(self.board)
    
    
    



if __name__ == "__main__":
    pass
