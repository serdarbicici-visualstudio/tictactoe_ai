from tictactoe_game import Tictactoe
import random

class Agent(Tictactoe):

    #agent plays player 2 (O)

    def __init__(self):
        super().__init__()
        self.q_table = {}
        # q_table = {"state": [action, Q-value]}
        # state = "---------"
        # action = 0-8
        # Q-value = 0-1

        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        self.state = None
        self.action = None
        self.next_state = None
        self.done = None

    def reset(self):
        super().reset()
        self.state = None
        self.action = None
        self.next_state = None
        self.done = None

    def get_state(self):
        return "".join(self.board)

    def get_reward(self):

        if self.winner(self.player2):
            return 1
        
        if self.winner(self.player1):
            return -1
        
        return 0

    def get_possible_actions(self):
        return [i for i in range(9) if self.board[i] == "-"]
    
    def get_action(self, state):
        if state not in self.q_table.keys():
            self.q_table[state] = [[action, 0] for action in self.get_possible_actions()]
        
        if random.random() < self.epsilon:
            return random.choice(self.get_possible_actions())
        
        return max(self.q_table[state], key=lambda x: x[1])[0]
    
    def train(self, episodes):
    # train the agent to play against player 1
    # choose only player 2's moves, make player 1 play randomly
        for episode in range(episodes):
            self.reset()
            self.state = self.get_state()
            self.done = False

            for round in range(9):
                reward = 0  # Initialize reward

                if round % 2 == 0:
                    player = self.player1
                    self.action = random.choice(self.get_possible_actions())

                    self.move(player, self.action // 3, self.action % 3)

                    self.next_state = self.get_state()

                    if self.winner(player):
                        reward = -1
                        self.done = True

                else:
                    player = self.player2
                    self.action = self.get_action(self.state)

                    self.move(player, self.action // 3, self.action % 3)

                    self.next_state = self.get_state()

                    if self.winner(player):
                        reward = 1
                        self.done = True

                if self.done:
                    if self.state not in self.q_table:
                        self.q_table[self.state] = [[action, 0] for action in self.get_possible_actions()]
                    for entry in self.q_table[self.state]:
                        if entry[0] == self.action:
                            entry[1] = reward
                    break

                if self.next_state not in self.q_table:
                    self.q_table[self.next_state] = [[action, 0] for action in self.get_possible_actions()]

                if self.state not in self.q_table:
                    self.q_table[self.state] = [[action, 0] for action in self.get_possible_actions()]

                for entry in self.q_table[self.state]:
                    if entry[0] == self.action:
                        entry[1] += self.alpha * (
                            reward + self.gamma * max(self.q_table[self.next_state], key=lambda x: x[1])[1] - entry[1])

                self.state = self.next_state

                if episode % 10 == 0:
                    print(f"Episode {episode + 1}/{episodes}")






                
                        




    def play_with_human(self):
        
        self.reset()
        self.draw_game()

        for round in range(9):

            if round % 2 == 0:
                player = self.player1

                print("Player 1's turn, enter the position (x, y): ")
                
                
                while True:
                    try:
                        x, y = map(int, input().split())
                        self.move(player, x, y)
                        break
                    except:
                        print("Invalid move, try again!")
                    


                self.draw_game()

                if self.winner(player):
                    print("Player 1 wins!")
                    break

            else:
                player = self.player2

                print("Player 2's turn, enter the position (x, y): ")
                
                # get best action from q_table
                self.action = self.get_action(self.get_state())
                self.move(player, self.action // 3, self.action % 3)


               
                    

                self.draw_game()

                if self.winner(player):
                    print("Player 2 (bot) wins!")
                    break

            

        print("\nGame Over!")

    
    

    

if __name__ == "__main__":
    # train the agent and print output, then play with human
    agent = Agent()
    agent.train(100)

    agent.play_with_human()

