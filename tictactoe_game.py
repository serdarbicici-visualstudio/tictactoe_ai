import numpy as np


class Tictactoe:
    def __init__(self):
        self.board = ["-" for i in range(9)]
        self.player1 = 1 # X
        self.player2 = 2 # O

    def reset(self):
        self.board = ["-" for i in range(9)]

    def move(self, player, x, y):
        

        if self.board[x * 3 + y] == "-":
            if player == self.player1:
                self.board[x * 3 + y] = "X"
            else:
                self.board[x * 3 + y] = "O"
            return True
                
        raise ValueError("Invalid move!")
        
    
    def winner(self, player):
        if player == 1:
            p = "X"
        
            for i in range(3):
                if self.board[i] == p and self.board[i + 3] == p and self.board[i + 6] == p:
                    return 1
                
                if self.board[3 * i] == p and self.board[3 * i + 1] == p and self.board[3 * i + 2] == p:
                    return 1
                
            if self.board[0] == p and self.board[4] == p and self.board[8] == p:
                return 1
            
            if self.board[2] == p and self.board[4] == p and self.board[6] == p:
                return 1
            
        else:
            p = "O"
            
            for i in range(3):
                if self.board[i] == p and self.board[i + 3] == p and self.board[i + 6] == p:
                    return 2
                
                if self.board[3 * i] == p and self.board[3 * i + 1] == p and self.board[3 * i + 2] == p:
                    return 2
                
            if self.board[0] == p and self.board[4] == p and self.board[8] == p:
                return 2
            
            if self.board[2] == p and self.board[4] == p and self.board[6] == p:
                return 2
            
                
        return False            
            

    def draw_game(self):
        print("\n\n")

        print("x-------")
        for i in range(3):
            print(i, self.board[i * 3], self.board[i * 3 + 1], self.board[i * 3 + 2], sep="|", end="|\n")
            print(" -------")
        print("  0 1 2 y")

        

        

    def game_loop(self):
        
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
                

                while True:
                    try:
                        x, y = map(int, input().split())
                        self.move(player, x, y)
                        break
                    except:
                        print("Invalid move, try again!")
                    

                self.draw_game()

                if self.winner(player):
                    print("Player 2 wins!")
                    break

            

        print("\nGame Over!")



            
        

if __name__ == '__main__':
    game = Tictactoe()
    game.game_loop()
