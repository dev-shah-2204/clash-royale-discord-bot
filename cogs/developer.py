import discord 

from discord.ext import commands 
from utils import colors 


class Developer(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot 
        
    @commands.command(name='reloadcog', help="A developer command")
    @commands.is_owner()
    async def reload_cog(self, ctx, cog):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.reply(f"Reloaded {cog} cog")
        except Exception as e:
            await ctx.reply(f"Error!\n```{e}```")
            
    
    @commands.command(name='loadcog', help="A developer command")
    @commands.is_owner()
    async def load_cog(self, ctx, cog):
        try:
            self.bot.load_extension(f"cogs.{cog}")
            await ctx.reply(f"Loaded {cog} cog")
        except Exception as e:
            await ctx.reply(f"Error!\n```{e}```") 
    
    
    @commands.command(name='unloadcog', help="A developer command")
    @commands.is_owner()
    async def unload_cog(self, ctx, cog):
        try:
            self.bot.unload_extension(f"cogs.{cog}")
            await ctx.reply(f"Unloaded {cog} cog")
        except Exception as e:
            await ctx.reply(f"Error!\n```{e}```") 
    
    
def setup(bot):
    bot.add_cog(Developer(bot))
    print("Developer cog loaded")