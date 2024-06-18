    def train(self, episodes):
        for episode in range(episodes):
            self.reset()
            self.state = self.get_state()
            self.done = False

            for round in range(9):
                reward = 0  # Initialize reward

                if round % 2 == 0:
                    # Player 1's turn (random moves)
                    player = self.player1
                    self.action = random.choice(self.get_possible_actions())
                    self.move(player, self.action // 3, self.action % 3)
                    self.next_state = self.get_state()

                    reward = self.get_reward()
                    if self.winner(player) or self.is_draw():
                        self.done = True

                else:
                    # Player 2's turn (bot)
                    player = self.player2
                    self.action = self.get_action(self.state)
                    self.move(player, self.action // 3, self.action % 3)
                    self.next_state = self.get_state()

                    reward = self.get_reward()
                    if self.winner(player) or self.is_draw():
                        self.done = True

                    if self.next_state not in self.q_table:
                        self.q_table[self.next_state] = [[action, 0] for action in self.get_possible_actions()]

                    if self.state not in self.q_table:
                        self.q_table[self.state] = [[action, 0] for action in self.get_possible_actions()]

                    if len(self.q_table[self.next_state]) > 0:
                        max_q_next = max(self.q_table[self.next_state], key=lambda x: x[1])[1]
                    else:
                        max_q_next = 0

                    for entry in self.q_table[self.state]:
                        if entry[0] == self.action:
                            entry[1] += self.alpha * (
                                reward + self.gamma * max_q_next - entry[1])

                    self.state = self.next_state

                if self.done:
                    if self.state not in self.q_table:
                        self.q_table[self.state] = [[action, 0] for action in self.get_possible_actions()]
                    for entry in self.q_table[self.state]:
                        if entry[0] == self.action:
                            entry[1] = reward
                    break

            if episode % 100 == 0:
                print(f"Episode {episode + 1}/{episodes}")