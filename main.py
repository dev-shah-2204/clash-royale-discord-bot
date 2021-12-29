import os
from bot import ClashRoyaler

cogs = [
    'botstats',
    'developer',
    'events',
    'clashroyale',
    'error_handler'
]

bot = ClashRoyaler(command_prefix="!!")

for cog in cogs:
    if __name__ == "__main__":
        try:
            bot.load_extension(f"cogs.{cog}")
        except Exception as e:
            print(e)

bot.run(os.environ.get('clash_royale_bot_token'))
