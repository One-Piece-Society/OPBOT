import discord
from discord.ext import commands
from dataGetter import *
import configparser
import time

config = configparser.ConfigParser()
config.read('config.ini')


class Multiplayer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.activeGames = {}

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if config['testing']['DisableMultiplayer'] == "true":
            return

    @commands.command(name="start")
    async def daily_prompt(self, ctx):
        """
        A simple guess the character quiz

        Description
        ___________________________________
        Fun multiplayer game to compete with your "friends"

        Usage
        ___________________________________
        op!start
        """
        embed = discord.Embed(color=0xff8800)

        if str(ctx.channel.id) in self.activeGames:
            embed.add_field(
                name=f"There is already a game started here", value="", inline=True)
            await ctx.channel.send(embed=embed)
            return

        else:
            embed.add_field(name=f"Quiz session has started",
                            value="", inline=False)
            embed.add_field(name=f"", value="", inline=False)
            embed.add_field(name=f"Game will begin in 30 secs",
                            value="Click the tick to join", inline=False)
            sentMsg = await ctx.channel.send(embed=embed)
            await sentMsg.add_reaction('✅')

            self.activeGames[str(ctx.channel.id)] = {"state": "joining"}
            print(self.activeGames)

            time.sleep(2)
            await sentMsg.add_reaction('⏱️')
            time.sleep(1)

            message = await ctx.fetch_message(sentMsg.id)
            
            print(message.reactions)
            print(type(message.reactions[0]))
            tick = message.reactions[0]

            async for user in tick.users():
                await ctx.channel.send(f'{user} has reacted with {tick.emoji}!')


            # for reaction in message.reactions:
            #     print(f'{reaction.emoji} has been used {reaction.count} times')


            # print(sentMsg.id)
            # print(str(sentMsg.reactions))
            # for react in sentMsg.reactions:
            #     print(react)

            await ctx.channel.send("timer up")
            

            # threading.Thread(target=startServer, args=mainCog).start()


async def setup(client):
    await client.add_cog(Multiplayer(client))
    print("Loaded Multiplayer module")
