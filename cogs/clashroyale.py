import os
import requests
import random
import discord

from discord.ext import commands
from utils import colors 


class ClashRoyale(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot):
        self.bot = bot
        self.key = os.getenv('CLASH_ROYALE_API_KEY')  # Get your's from https://developer.clashroyale.com/
        
        
    @commands.command(name='profile', help='Get the information on a Clash Royale player.')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def get_cr_profile(self, ctx, tag, args=None):
        if tag.startswith('#'):
            tag = tag.replace('#', '%23')
        else:
            tag = f"%23{tag}"
           
        url = f'https://proxy.royaleapi.dev/v1/players/{tag}'
        r = requests.get(
            url=url, 
            headers={
                'Authorization': f'Bearer {self.key}'
                }
            )
        
        if r.status_code == 404:
            em = discord.Embed(
                title='How to find your tag',
                color=colors.l_red
            )
            em.set_image(url="https://i.imgur.com/d4VSZFM.gif")
            tag = tag.replace("%23", "#")
            
            await ctx.reply(f"No Clash Royale account was found with the tag `{tag}`", mention_author=False, embed=em)
            return
        
        if r.status_code == 200:
            r = r.json()
            if args is None:
                playing_since = "Less than a year"  # Default value
                
                for item in r['badges']:
                    if item['name'] == 'Played1Year':
                        playing_since = f"{(str(int(item['progress'])/365))[:4]} years"
                        break                


                desc = f"""
**Level**: `{r['expLevel']}`
**Trophies**: `{r['trophies']}`
**Highest Trophies**: `{r['bestTrophies']}` 
**Battles Won**: `{r['wins']}` 
**Battles Lost**: `{r['losses']}` 
**Three Crown Wins**: `{r['threeCrownWins']}`
**Total Donations**: `{r['totalDonations']}`

**Playing Since**: `{playing_since}`                 
"""
                em = discord.Embed(
                    title=f"Clash Royale profile of `{r['name']}`",
                    description=desc,
                    color=colors.l_blue
                )
                em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
                await ctx.send(embed=em)
                
            elif args.lower() == 'clan':
                desc = f""" 
**Clan Name**: `{r['clan']['name']}`
**Clan Tag**: `{r['clan']['tag']}` 
**Donations Given**: `{r['donations']}`
**Donations Received**: `{r['donationsReceived']}`          
"""
                em = discord.Embed(
                    title=f"`{r['name']}`'s clan",
                    description=desc,
                    color=colors.l_blue
                )
                em.set_footer(text="For more details about the clan, run the 'claninfo' command")
                await ctx.send(embed=em)
                
            if args is not None and args.lower() != 'clan':
                await ctx.send("Invalid arguments. Valid argument(s) are: `clan`")
                
    
    @commands.command(name='claninfo', help="Get information on a Clash Royale clan.")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def get_clan_info(self, ctx, tag):
        if tag.startswith('#'):
            tag = tag.replace('#', '%23')
        else:
            tag = f"%23{tag}"
           
        url = f'https://proxy.royaleapi.dev/v1/clans/{tag}'
        r = requests.get(
            url=url, 
            headers={
                'Authorization': f'Bearer {self.key}'
                }
            )
        
        if r.status_code == 404:
            em = discord.Embed(
                title="Here's how to find your clan tag",
                color=colors.m_red
            )
            em.set_image(url="https://i.imgur.com/VQYmehU.gif")
            tag = tag.replace("%23", "#")
            
            await ctx.reply(f"No Clash Royale clan found with the tag `{tag}`", mention_author=False, embed=em)
            return
        
        if r.status_code == 200:
            r = r.json()
            desc = f"""
**Clan Tag**: {r['tag']}
**Description**: {r['description']}
**Location**: {r['location']['name']}
**Members**: {r['members']}
**Clan Score**: {r['clanScore']}
**Clan War Trophies**: {r['clanWarTrophies']}
**Required Trophies**: {r['requiredTrophies']}
**Donations per Week**: {r['donationsPerWeek']}
"""
            em = discord.Embed(
                title=f"Clash Royale clan `{r['name']}`",
                description=desc,
                color=colors.l_blue
            )
            em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
            
        
        
def setup(bot):
    bot.add_cog(ClashRoyale(bot))
    print("ClashRoyale cog loaded")
