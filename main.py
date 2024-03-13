from game import Game
from players import Sheep, Sheepdog1, Sheepdog2, Sheepdog3

if __name__ == "__main__":
    game = Game()
    sheep = Sheep(game.grid)
    bot = Sheepdog2(game.grid)

    game.sheep = sheep
    game.bot = bot

    won = game.run(1000000) # max 1 million turns; return 1 if won

    if won:
        print("Game finished with", game.turns, "turns.")
    else:
        print("Game lost with", game.turns, "turns.")