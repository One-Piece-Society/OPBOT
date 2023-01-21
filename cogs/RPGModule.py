import discord
from discord.ext import commands
from dataGetter import *
from PIL import Image
import io
import json
import time
import random


class RPG(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.data = loadData()

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

        if ctx.author.id not in self.data:
            self.data[ctx.author.id] = {}
            self.data[ctx.author.id]["last_daily"] = 0
            self.data[ctx.author.id]["bal"] = 0

        prevDaily = time.time() - self.data[ctx.author.id]["last_daily"]
        if prevDaily > 72000:
            newAmount = random.randint(100, 1000)
            self.data[ctx.author.id]["bal"] += newAmount
            self.data[ctx.author.id]["last_daily"] = time.time()

            embed = discord.Embed(color=0xff8c00)
            embed.add_field(
                name=f"You got 🪙 {newAmount}", value="", inline=True)
            # await ctx.channel.send(embed=embed)

        else:
            hours = (prevDaily + 72000) // 3600
            minutes = ((prevDaily + 72000) - (hours * 3600)) // 60

            embed = discord.Embed(color=0xff0000)
            if hours >= 1:
                embed.add_field(
                    name=f"Arnt no tresure to be seen, Try again in {int(hours)} hours", value="", inline=True)
            else:
                embed.add_field(
                    name=f"Hey we haven't found the treasure yet, Try again in {int(minutes)} minutes", value="", inline=True)

        await ctx.channel.send(embed=embed)
        print(self.data)

    @commands.command(name="profile")
    async def profile_prompt(self, ctx, selected_user=None):
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
        embed.add_field(name="Account Created At", value=member.created_at.strftime(
            "%B %d, %Y"), inline=True)
        embed.add_field(name="Server Join Date", value=member.joined_at.strftime(
            "%B %d, %Y"), inline=True)
        await ctx.channel.send(embed=embed)
        await ctx.channel.send(member.avatar_url)

        # await ctx.channel.send(embed=embedVar)


def loadData():
    if not os.path.exists("rpgData.json"):
        with open("rpgData.json", "w") as file:
            json.dump({}, file)

    with open("rpgData.json") as file:
        return json.load(file)

# def get_user(data, uid):
#     if uid in data:
#         return

# def get_user_bank(uid):
#     user = get_user(get_RPG_data(), uid)


async def setup(client):
    await client.add_cog(RPG(client))
    print("Loaded RPG module")
