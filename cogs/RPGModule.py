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
        self.data = loadData("rpgData.json")
        self.shopInfo = loadData("shop.json")

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
        self.data = addUser(self.data, str(ctx.author.id))

        prevDaily = time.time() - self.data[str(ctx.author.id)]["last_daily"]
        if prevDaily > 72000:
            newAmount = random.randint(100, 1000)
            self.data[str(ctx.author.id)]["bal"] += newAmount
            self.data[str(ctx.author.id)]["last_daily"] = time.time()

            embed = discord.Embed(color=0xff8c00)
            embed.add_field(
                name=f"You got 🪙 {newAmount}", value="", inline=True)

        else:
            hours = (72000 - prevDaily) // 3600
            minutes = ((72000 - prevDaily) - (hours * 3600)) // 60

            embed = discord.Embed(color=0xff0000)
            if hours >= 1:
                embed.add_field(
                    name=f"Arnt no tresure to be seen, Try again in {int(hours)} hours", value="", inline=True)
            else:
                embed.add_field(
                    name=f"Hey we haven't found the treasure yet, Try again in {int(minutes)} minutes", value="", inline=True)

        await ctx.channel.send(embed=embed)
        saveData(self.data)

    @commands.command(name="bal")
    async def bal_prompt(self, ctx):
        """
        How rich are you

        Description
        ___________________________________
        Tells you how rich you are 

        Usage
        ___________________________________
        op!bal
        """

        embed = discord.Embed(color=0xf2ff00)

        self.data = addUser(self.data, str(ctx.author.id))

        currentBal = self.data[str(ctx.author.id)]["bal"]
        if currentBal == 0:
            embed.add_field(
                name=f"Seems lonely you have 🪙 0", value="Here is a free cookie 🍪", inline=True)
            self.data[str(ctx.author.id)]["bal"] += 10

        else:
            embed.add_field(
                name=f"You have 🪙 {currentBal}", value="", inline=True)

        await ctx.channel.send(embed=embed)
        saveData(self.data)

    @commands.command(name="shop")
    async def shop_prompt(self, ctx, item=None):
        """
        Things you can buy

        Description
        ___________________________________
        From fish to candy what can one buy?
        The follow command lists out the 
        individual items available for purchase.

        Usage
        ___________________________________
        op!shop [item]
        """

        embed = discord.Embed(color=0xf2ff00)

        if item in self.shopInfo:
            embed.add_field(
                name=item, value=self.shopInfo[item]["description"], inline=False)
            embed.add_field(name="", value="", inline=False)

            embed.add_field(
                name="Cost", value=self.shopInfo[item]["cost"], inline=False)

            embed.add_field(
                name="❤️", value=self.shopInfo[item]["health"], inline=True)
            embed.add_field(
                name="🗡️", value=self.shopInfo[item]["attack"], inline=True)
            embed.add_field(
                name="🛡️", value=self.shopInfo[item]["defence"], inline=True)

            await ctx.channel.send(embed=embed)
            return

        embed.add_field(
            name=f"Luffy's Shop", value="Do op!shop [item] for more info", inline=False)
        embed.add_field(name="", value="", inline=False)

        for item in self.shopInfo:
            cost = str(self.shopInfo[item]["cost"])
            formatted_text = "{:<{}}{:>{}}".format(
                str(item), 20, f"{cost} 🪙", 20)
            embed.add_field(name=formatted_text, value="", inline=False)

        await ctx.channel.send(embed=embed)

    @commands.command(name="buy")
    async def shop_prompt(self, ctx, item=None):
        """
        Chooses an item to buy 

        Description
        ___________________________________
        Allow you to buy an item 

        Usage
        ___________________________________
        op!buy <item>
        """
        self.data = addUser(self.data, str(ctx.author.id))

        embed = discord.Embed(color=0xf2ff00)

        if item == None:
            embed.add_field(name="Please specifiy an item",
                            value="", inline=False)
            await ctx.channel.send(embed=embed)
            return

        if item in self.shopInfo and self.data[str(ctx.author.id)]["bal"] >= self.shopInfo[item]["cost"]:
            embed.add_field(
                name=f"You have obtained a {item}", value="", inline=False)
            self.data[str(ctx.author.id)]["bal"] -= self.shopInfo[item]["cost"]
            self.data[str(ctx.author.id)
                      ]["health"] += self.shopInfo[item]["health"]
            self.data[str(ctx.author.id)
                      ]["attack"] += self.shopInfo[item]["attack"]
            self.data[str(ctx.author.id)
                      ]["defence"] += self.shopInfo[item]["defence"]

        await ctx.channel.send(embed=embed)
        saveData(self.data)

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


def loadData(path):
    if not os.path.exists(path):
        with open(path, "w") as file:
            json.dump({}, file)

    with open(path) as file:
        return json.load(file)


def saveData(data):
    with open("rpgData.json", "w") as file:
        json.dump(data, file, indent=4)


def addUser(data, uid):
    if str(uid) not in data:
        data[str(uid)] = {}
        data[str(uid)]["last_daily"] = 0
        data[str(uid)]["bal"] = 0
        data[str(uid)]["health"] = 10
        data[str(uid)]["attack"] = 1
        data[str(uid)]["defence"] = 1

    return data


async def setup(client):
    await client.add_cog(RPG(client))
    print("Loaded RPG module")
