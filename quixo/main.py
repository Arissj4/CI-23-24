from game import Game, Move, Player
import copy

class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move

class MyPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        _, move = self.minimax(game, self, depth=3)
        print(_, move)
        return _, move

    def minimax(self, game, player, depth):
        print("Start the MiniMax")
        print(bool(game.check_winner()))

        print("Setting the best score and best move")
        best_score = float('-inf') if player == self else float('inf')
        best_move = None
        print(game._Game__take((1,3), self))
        print("Looping through the moves")
        for move in game._Game__slide(player):
            new_game = copy.deepcopy(game)
            new_game.apply_move(player, move)
            score, _ = self.minimax(new_game, self if player != self else game.get_opponent(self), depth - 1)

            if player == self:
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move

        return best_score, best_move

if __name__ == '__main__':
    g = Game()
    g.print()
    player1 = MyPlayer()
    player2 = RandomPlayer()
    winner = g.play(player1, player2)
    g.print()
    print(f"Winner: Player {winner}")

""" from game import Game, Move, Player
import copy
import random  # Don't forget to import the 'random' module

class RandomPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        from_pos = (random.randint(0, 4), random.randint(0, 4))
        move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
        return from_pos, move

class MyPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def make_move(self, game: 'Game') -> tuple[tuple[int, int], Move]:
        _, move = self.minimax(game, self, depth=3)
        print(_, move)
        return _, move

    def minimax(self, game, player, depth):
        print("Start the MiniMax")
        print(bool(game.check_winner()))

        print("Setting the best score and best move")
        best_score = float('-inf') if player == self else float('inf')
        best_move = None

        print("Looping through the moves")
        for move in game.__slide(player):  # Corrected the method name to '__slide'
            new_game = copy.deepcopy(game)
            from_pos = (random.randint(0, 4), random.randint(0, 4))  # You need to choose a valid from_pos
            move = random.choice([Move.TOP, Move.BOTTOM, Move.LEFT, Move.RIGHT])
            new_game._Game__move(from_pos, move, player)  # Corrected the method name to '__move'
            score, _ = self.minimax(new_game, self if player != self else game.get_opponent(self), depth - 1)

            if player == self:
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move

        return best_score, best_move

if __name__ == '__main__':
    g = Game()
    g.print()
    player1 = MyPlayer()
    player2 = RandomPlayer()
    winner = g.play(player1, player2)
    g.print()
    print(f"Winner: Player {winner}")
 """