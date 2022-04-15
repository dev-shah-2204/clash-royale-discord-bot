import os

from dotenv import load_dotenv
from bot import ClashRoyaler


load_dotenv()

cogs = [
    'botstats',
    'developer',
    'events',
    'clashroyale',
    'error_handler'
]

bot = ClashRoyaler(command_prefix=">")
bot.remove_command('help')

for cog in cogs:
    if __name__ == "__main__":
        try:
            bot.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(e)

bot.load_extension('jishaku')

bot.run(os.environ.get('clash_royale_bot_token'))
