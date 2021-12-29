import discord 

from utils import colors
from discord.ext import commands


class BotStats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ping', help="Shows the bot's ping.")
    async def ping(self, ctx):
        latency = round(self.bot.latency*1000)
        if latency > 10 and latency < 20:
            color = colors.l_green
        elif latency > 20 and latency < 100:
            color = colors.l_yellow
        else:
            color = colors.m_red
        
        em = discord.Embed(
            title='Pong!',
            description=f"{latency}ms",
            color=color
        )
        
        await ctx.send(embed=em)
        
    @commands.command(name='invite', help="Invite the bot to your server")
    async def invite(self, ctx):
        em = discord.Embed(
            title='Thanks for inviting me!',
            description=f"Click [here](https://discord.com/api/oauth2/authorize?client_id={self.bot.user.id}&permissions-8&scope=bot) to add me to your server",
            color=colors.l_green
        )
        em.set_footer(
            text=f"Bot created by {self.bot.get_user(self.bot.owner_id)}",
            icon_url=self.bot.get_user(self.bot.owner_id).avatar_url
        )
        await ctx.reply(embed=em)
    



def setup(bot):
    bot.add_cog(BotStats(bot))
    print("BotStats has been loaded")
