import discord
from discord.ext import commands
from dataGetter import *
from PIL import Image
import io


class RPG(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="daily")
    async def daily_prompt(self, ctx):
        """
        Give you the money
        
        Description
        ___________________________________
        A way to earn some coins.
                
        Usage
        ___________________________________
        op!daily
        """

        ctx.author.id

           


        
    @commands.command(name="profile")
    async def profile_prompt(self, ctx, selected_user = None):
        """
        Gets your profile
        
        Description
        ___________________________________
        Print out stats for your profile.
        
        Usage
        ___________________________________
        op!profile [@user]
        """
        
        if selected_user == None: 
            member = ctx.author
        else:
            match = re.search(r'\d+', selected_user)
            member = [member for member in ctx.channel.members if
                    member.id == int(match.group())][0]        

        embed = discord.Embed(title=f"{member.name}'s Profile", color=0x00ff00)
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Name", value=member.name, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Account Created At", value=member.created_at.strftime("%B %d, %Y"), inline=True)
        embed.add_field(name="Server Join Date", value=member.joined_at.strftime("%B %d, %Y"), inline=True)
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(member.avatar_url)




        # await ctx.channel.send(embed=embedVar)

        
        
        

async def setup(client):
    await client.add_cog(RPG(client))
    print("Loaded RPG module")
    