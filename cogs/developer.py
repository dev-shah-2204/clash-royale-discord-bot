import discord

from discord.ext import commands
from utils import colors

class Developer(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
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


    @commands.command(name='sendmessage', help="A developer command")
    @commands.is_owner()
    async def send_message(self, ctx, user_id, *, message):
        em = discord.Embed(
            title="Message from my developer",
            description=message,
            color=colors.l_red
        )
        owner = self.bot.get_user(self.bot.owner_id)
        if owner is not None:
            em.set_footer(text=f"For more information contant {owner}", icon_url=owner.avatar_url)

        user = self.bot.get_user(user_id)
        if user is None:
            await ctx.send("User not found")
            return

        try:
            await user.send(embed=em)
        except discord.Forbidden:
            await ctx.send("Forbidden.")

    
    
def setup(bot):
    bot.add_cog(Developer(bot))
    print("Developer cog loaded")
