from variants import Variants
from player import Player

bot = Player()

alex = Player(Variants.SCISSORS, 'Alex')
print(Player.whoWins(bot, alex))