
from game import Game, Move, Player
import numpy as np
import copy
import random


class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()
        self.player_id = 1
        
    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move
    
class MinimaxPlayer(Player):
    def __init__(self, max_depth=3, id = -1):
        super().__init__()
        self.max_depth = max_depth
        self.player_id = id
        self.round = 1

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        _, best_move = self.minimax(game, self.max_depth, True)
        return best_move

    def minimax(self, game, depth, maximizing_player):
        if depth == 0 or game.check_winner() != -1:
            return self.evaluate(game), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None

            for move in self.get_possible_moves(game, self.player_id):
                new_game = copy.deepcopy(game)
                eval = 0
                new_game._Game__move(move[0], move[1], self.player_id)
                eval, _ = self.minimax(new_game, depth - 1, False)

                if eval > max_eval:
                    max_eval = eval
                    best_move = move

            return max_eval, best_move
        
        else:
            min_eval = float('inf')
            best_move = None

            for move in self.get_possible_moves(game, self.player_id):
                new_game = copy.deepcopy(game)
                eval = 0
                new_game._Game__move(move[0], move[1], self.player_id)
                eval, _ = self.minimax(new_game, depth - 1, True)

                if eval < min_eval:
                    min_eval = eval
                    best_move = move

            return min_eval, best_move

    def evaluate(self, game):
        if game.check_winner() == 0:
            return 100
        elif game.check_winner() == 1:
            return -100
        # Check the pieces of the user and check if they are next to each other
        # Check if user has any pieces in the game
        else:
            user_pieces = []
            for col in range(5):
                for row in range(5):
                    if game._board[col][row] == 0:
                        user_pieces.append((row, col))

            conrners = [(0, 0), (0, 4), (4, 0), (4, 4)]
            sides = [[(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], [(4, 1), (4, 2), (4, 3)], [(1, 4), (2, 4), (3, 4)]]

            for piece in user_pieces:
                points = 0
                if piece == conrners[0]:
                    for i in range(piece[0], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[i][i] == 0:
                            points += 1
                        else:
                            break
                elif piece == conrners[1]:
                    for i in range(piece[0], 5):
                        if game._board[piece[0]][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                elif piece == conrners[2]:
                    for i in range(piece[1], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0] - i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0] - i][i] == 0:
                            points += 1
                        else:
                            break
                elif piece == conrners[3]:
                    for i in range(0, 5):
                        if game._board[piece[0]][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0] - i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0] - i][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                elif piece in sides[0]:
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break 
                    for i in range(0, piece[1] + 1):
                        if game._board[piece[0]][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
                elif piece in sides[1]:
                    for i in range(piece[0], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break 
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0] - i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                elif piece in sides[2]:
                    for i in range(piece[0], 5):
                        if game._board[piece[0] - i][piece[1]] == 0:
                            points += 1
                        else:
                            break 
                    for i in range(piece[1], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0]][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                elif piece in sides[3]:
                    for i in range(piece[1], 5):
                        if game._board[piece[0]][piece[1] - i] == 0:
                            points += 1
                        else:
                            break 
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0]- i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                elif piece[0] == 2 and piece[1] == 2:
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break 
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0]][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0]][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0] + i][piece[1] + i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0] - i][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0] + i][piece[1] - i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0] + 1):
                        if game._board[piece[0] - i][piece[1] + i] == 0:
                            points += 1
                        else:
                            break
                else:
                    for i in range(piece[0], 5):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break 
                    for i in range(0, piece[0]):
                        if game._board[i][piece[1]] == 0:
                            points += 1
                        else:
                            break
                    for i in range(piece[0], 5):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
                    for i in range(0, piece[0]):
                        if game._board[piece[0]][i] == 0:
                            points += 1
                        else:
                            break
            
            return points
        
    def get_possible_moves(self, game, id):

        moves = []
        all_piece = [(x, y) for x in range(5) for y in range(5)]
        sides = [Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT]

        # Find all the pieces that the user can move
        for piece in all_piece:
            if game._board[piece] == id or game._board[piece] == -1:
                for side in sides:
                    new_game = copy.deepcopy(game)
                    if new_game._Game__move(piece, side, id):
                        moves.append((piece, side))

        return moves


if __name__ == '__main__':

    #Single game
    """ g = Game()
    g.print()
    player1 = MinimaxPlayer(id = 0)
    player2 = RandomPlayer()
    
    winner = g.play(player1, player2)
    g.print()
    print(f"Winner: Player {winner}")
 """
    #Multi game
    me = 0
    opponent = 0
    draw = 0
    for i in range(25):
        g = Game()
        player1 = MinimaxPlayer(id = 0)
        player2 = RandomPlayer()
        print(f"Game {i}")
        winner = g.play(player1, player2)
        print(f"Winner: Player {winner}")
        if winner == 0:
            me += 1
        elif winner == 1:
            opponent += 1
        else:
            draw += 1
    print(f"Winrate: MyPlaye ={me / 25} - Opponent = {opponent / 25} - Draw = {draw / 25}")
