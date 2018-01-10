from game import Game
from output import ConsoleOutput
from input import ConsoleInput


game = Game(ConsoleOutput(), ConsoleInput())

game.start()
