import discord
from discord.ext import commands
from dataGetter import *
import configparser
import time
import random


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

    @commands.command(name="pickme")
    async def randomUser_prompt(self, ctx, inputTime=10):
        """
        Picks 1 user from a group 

        Description
        ___________________________________
        A way to choose a person from a group, 
        you can optionally select a time for
        the picking process

        Usage
        ___________________________________
        op!pickme [secs]
        """

        if not str(inputTime).isdigit():
            ctx.channel.send("Time specified must be a int")
            return

        embed = discord.Embed(color=0xa903fc)
        embed.add_field(name=f"Choosing a random user",
                        value="", inline=False)
        embed.add_field(name=f"", value="", inline=False)
        embed.add_field(name=f"",
                        value="Click the tick to join", inline=False)
        sentMsg = await ctx.channel.send(embed=embed)
        await sentMsg.add_reaction('✅')

        time.sleep(int(inputTime))
        message = await ctx.fetch_message(sentMsg.id)

        usersjoined = [user async for user in message.reactions[0].users() if user.id != sentMsg.author.id]

        embed = discord.Embed(color=0xa903fc)
        if usersjoined == []:
            embed.add_field(name=f"There was no winners, no one was chosen :cry:",
                            value="", inline=False)
        else:
            randUser = random.choice(usersjoined)
            embed.add_field(name=f"Congrats to {randUser} !!!!",
                            value="You have been chosen as captain", inline=False)

        await ctx.channel.send(embed=embed)

    @commands.command(name="startquiz")
    async def pictureGame_prompt(self, ctx):
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

        # Setup states for joining
        embed.add_field(name=f"Quiz session has started",
                        value="", inline=False)
        embed.add_field(name=f"", value="", inline=False)
        embed.add_field(name=f"Game will begin in 30 secs",
                        value="Click the tick to join", inline=False)
        sentMsg = await ctx.channel.send(embed=embed)
        await sentMsg.add_reaction('✅')

        self.activeGames[str(ctx.channel.id)] = {"state": 0}
        print(self.activeGames)

        time.sleep(2)
        await sentMsg.add_reaction('⏱️')
        time.sleep(1)

        message = await ctx.fetch_message(sentMsg.id)
        usersjoined = [user async for user in message.reactions[0].users() if user.id != sentMsg.author.id]

        # Sends game start confirmation
        embed = discord.Embed(color=0xa903fc)
        if len(usersjoined) == 0:
            embed.add_field(name=f"No one has joined",
                            value="The game will cease to run", inline=False)
            await ctx.channel.send(embed=embed)
            del self.activeGames[str(ctx.channel.id)]
            return

        # elif len(usersjoined) == 1:
        #     embed.add_field(name=f"Seams no one wants to join yet",
        #         value="try again when there are more people (solo feature to be added later)", inline=False)
        #     await ctx.channel.send(embed=embed)
        #     del self.activeGames[str(ctx.channel.id)]
        #     return

        else:
            embed.add_field(name=f"Players joined",
                            value="The game will start in 10 secs", inline=False)
            embed.add_field(name=f"",
                            value="50/50 and skips can be used every 5 rounds", inline=False)

            self.activeGames[str(ctx.channel.id)]["state"] = 1
            self.activeGames[str(ctx.channel.id)]["players"] = {}
            for user in usersjoined:
                self.activeGames[str(ctx.channel.id)]["players"][str(user.id)] = {
                    "name": user.name[:10],
                    "skip": 0,
                    "50": 0,
                    "health": 3,
                }

                embed.add_field(name=f"{user.name}", value="", inline=False)

            await ctx.channel.send(embed=embed)

        print(self.activeGames)

        # for reaction in message.reactions:
        #     print(f'{reaction.emoji} has been used {reaction.count} times')

        # print(sentMsg.id)
        # print(str(sentMsg.reactions))
        # for react in sentMsg.reactions:
        #     print(react)

        await ctx.channel.send("timer up")

        # threading.Thread(target=startServer, args=mainCog).start()

    @commands.command(name="test1")
    async def screen1_prompt(self, ctx):
        roundNo = 12
        answerName = "luffy"
        answerValue = "A"
        playerInfo = {'279119312072081408': {'name': "alex", 'skip': 0, '50': 0, 'health': 3, "previousAns": "C", "change": 1},
                      '279119312072081409': {'name': "alex2", 'skip': 5, '50': 2, 'health': 1, "previousAns": "50", "change": 1},
                      '279119312072081411': {'name': "alex4", 'skip': 5, '50': 2, 'health': 0, "previousAns": "None", "change": 1},
                      '279119312072411': {'name': "alex44", 'skip': 5, '50': 2, 'health': 0, "previousAns": "None", "change": 0},
                      '279119312072081410': {'name': "alex3wwwww", 'skip': 1, '50': 3, 'health': 2, "previousAns": "skip", "change": 0}}
        sortedplayerInfo = sorted(playerInfo.items(), key=lambda x: (
            x[1]["health"], x[1]["change"]))[::-1]

        embed = discord.Embed(color=0xff8800)

        embed.add_field(name=f"Round results ({roundNo})",
                        value=f"The correct answer was :regional_indicator_{answerValue.lower()}: {answerName}", inline=False)
        embed.add_field(name=f"", value="", inline=False)
        embed.add_field(
            name=f"Name (:heart: Health / :negative_squared_cross_mark: 50/50 / :fast_forward: Skips / :capital_abcd: Answer )", value="", inline=False)

        for key in sortedplayerInfo:
            idx = key[0]

            name = playerInfo[idx]['name']

            if playerInfo[idx]['health'] > 0:
                hearts = ":heart:" * playerInfo[idx]['health']
                if playerInfo[idx]['change'] == 1:
                    hearts += ":no_entry_sign:"
            else:
                hearts = ":skull:"

            if playerInfo[idx]['skip'] > 0:
                skips = f":negative_squared_cross_mark: in {playerInfo[idx]['skip']}"
            else:
                skips = f":negative_squared_cross_mark: ready"

            if playerInfo[idx]['50'] > 0:
                halfs = f":fast_forward: in {playerInfo[idx]['50']}"
            else:
                halfs = f":fast_forward: ready"

            if playerInfo[idx]['previousAns'] == "None":
                givenAns = ":x:"
            elif playerInfo[idx]['previousAns'] == "50":
                givenAns = ":negative_squared_cross_mark:"
            elif playerInfo[idx]['previousAns'] == "skip":
                givenAns = ":fast_forward:"
            else:
                givenAns = f":regional_indicator_{playerInfo[idx]['previousAns'].lower()}:"

            if playerInfo[idx]['change'] == 0 and playerInfo[idx]['health'] == 0:
                embed.add_field(name=f"{name} ({hearts})",
                                value=f"", inline=False)
            else:
                embed.add_field(
                    name=f"{name} ({hearts})", value=f"{skips} / {halfs} / you answered {givenAns}", inline=False)

        await ctx.channel.send(embed=embed)


async def setup(client):
    await client.add_cog(Multiplayer(client))
    print("Loaded Multiplayer module")
