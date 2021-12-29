import discord
from discord.ext import commands


class ClashRoyaler(commands.Bot):
    def __init__(self, command_prefix=">>"):
        super().__init__(
            command_prefix=command_prefix,
            intents=discord.Intents.all(),
            case_insensitive=True,
            allowed_mentions=discord.AllowedMentions(everyone=False), # (everyone:bool, users:bool, roles:bool, replied_user:bool)
            owner_id=416979084099321866  # Your ID here
        )
