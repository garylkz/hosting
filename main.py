import sys
from dscord import bot, wake

wake.up()
bot.load('system')
bot.run(sys.argv[1])

