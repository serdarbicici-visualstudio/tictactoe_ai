from tictactoe_game import Tictactoe
import random

class Agent(Tictactoe):
    def __init__(self):
        super().__init__()
        self.q_table = {}
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.1
        self.state = None
        self.action = None
        self.next_state = None
        self.done = None
        self.all_states = set()

    def reset(self):
        super().reset()
        self.state = None
        self.action = None
        self.next_state = None
        self.done = None
        self.all_states = set()

    def get_state(self):
        return "".join(self.board)

    def check_double(self, player):
        for i in range(9):
            if self.board[i] == "-":

                if player == self.player1:
                    self.board[i] = "X"

                else:
                    self.board[i] = "O"

                if self.winner(player):
                    self.board[i] = "-"
                    return True
                
                self.board[i] = "-"
        return False

    def get_reward(self):
        if self.winner(self.player2):
            return 1
        if self.winner(self.player1):
            return -1
        if self.is_draw():
            return -0.5
        if self.check_double(self.player1):
            return -100
        if self.check_double(self.player2):
            return 0.5
        
        return 0

    def get_possible_actions(self):
        return [i for i in range(9) if self.board[i] == "-"]

    def get_action(self, state):
        if state not in self.q_table:
            self.q_table[state] = [[action, 0] for action in self.get_possible_actions()]
        if random.random() < self.epsilon:
            return random.choice(self.get_possible_actions())
        return max(self.q_table[state], key=lambda x: x[1] if self.board[x[0]] == "-" else float('-inf'))[0]

    

    def is_draw(self):
        return "-" not in self.board

    def save_q_table(self):
        with open("q_table.csv", "w") as f:
            for state, actions in self.q_table.items():
                f.write(state + ",")
                for action in actions:
                    f.write(str(action[0]) + "," + str(action[1]) + ",")
                f.write("\n")

    def train(self, episodes):
        for episode in range(episodes):
            self.reset()
            self.state = self.get_state()
            self.done = False

            while not self.done:
                # Get the current state and select an action using epsilon-greedy policy
                self.state = self.get_state()
                self.action = self.get_action(self.state)

                # Take the action and observe the reward and the next state
                self.move(self.player2, self.action // 3, self.action % 3)
                self.next_state = self.get_state()
                reward = self.get_reward()

                # If the game is done, set the done flag
                self.done = self.winner(self.player2) or self.is_draw()

                # Initialize Q-table for next state if it doesn't exist
                if self.next_state not in self.q_table:
                    self.q_table[self.next_state] = [[action, 0] for action in self.get_possible_actions()]

                # Update the Q-table for the current state-action pair
                if self.state not in self.q_table:
                    self.q_table[self.state] = [[action, 0] for action in self.get_possible_actions()]

                current_actions = self.q_table[self.state]
                action_index = next(index for index, value in enumerate(current_actions) if value[0] == self.action)

                if self.done:
                    self.q_table[self.state][action_index][1] = reward
                else:
                    future_rewards = [q[1] for q in self.q_table[self.next_state] if self.board[q[0]] == "-"]
                    max_future_reward = max(future_rewards) if future_rewards else 0
                    q_value = (1 - self.alpha) * self.q_table[self.state][action_index][1] + self.alpha * (reward + self.gamma * max_future_reward)
                    self.q_table[self.state][action_index][1] = q_value

                # If the game isn't done, switch to the opponent's move
                if not self.done:
                    opponent_action = random.choice(self.get_possible_actions())
                    self.move(self.player1, opponent_action // 3, opponent_action % 3)
                    self.done = self.winner(self.player1) or self.is_draw()

                if episode % 1000 == 0:
                    print("Episode: ", episode)


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
                self.action = self.get_action(self.get_state())
                self.move(player, self.action // 3, self.action % 3)
                self.draw_game()
                if self.winner(player):
                    print("Player 2 (bot) wins!")
                    break
        print("\nGame Over!")

if __name__ == "__main__":
    agent = Agent()
    agent.train(5000000)
    while True:
        agent.play_with_human()
