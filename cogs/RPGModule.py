import discord
from discord.ext import commands
from dataGetter import *
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
    async def buy_prompt(self, ctx, item=None):
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

    @commands.command(name="top")
    async def top_prompt(self, ctx):
        """
        Finds the richest user

        Description
        ___________________________________
        A leaderboard for users wealth

        Usage
        ___________________________________
        op!top
        """
        self.data = addUser(self.data, str(ctx.author.id))

        embed = discord.Embed(color=0xff00e6)
        embed.add_field(name=f"Leaderboard", value="", inline=False)

        for item in sorted(self.data.items(), key=lambda x: x[1]["bal"])[:-6:-1]:
            try:
                user = [member for member in ctx.channel.members if
                        member.id == int(item[0])][0]
                username = user.name

            except:
                username = "?????"

            ubal = item[1]["bal"]
            embed.add_field(name=f"{username} (🪙 {ubal})",
                            value="", inline=False)

        await ctx.channel.send(embed=embed)
        saveData(self.data)

    @commands.command(name="gamble")
    async def gamble_prompt(self, ctx, amount):
        """
        Double your money 

        Description
        ___________________________________
        Gives a chance to double your money or 
        get more???

        Usage
        ___________________________________
        op!gamble <amount/all>
        """
        self.data = addUser(self.data, str(ctx.author.id))

        embed = discord.Embed(color=0xff00e6)
        embed.add_field(
            name=f"Gamble", value="Weird odds are used", inline=False)

        if self.data[str(ctx.author.id)]["bal"] == 0:
            embed.add_field(
                name=f"A bit lacking on funds, Come back later", value="", inline=False)

        else:

            if amount == "all":
                amount = str(self.data[str(ctx.author.id)]["bal"])

            if amount.isnumeric() and self.data[str(ctx.author.id)]["bal"] >= int(amount):
                self.data[str(ctx.author.id)]["bal"] -= int(amount)
                odds = random.randint(1, 1000)
                win = 0

                if odds == 1:
                    embed.add_field(
                        name=f"100x your money (wait thats an option?)", value="", inline=False)
                    win = int(amount)*100

                elif odds < 10:
                    embed.add_field(
                        name=f"10x your money (Looks like someone got a jackpot)", value="", inline=False)
                    win = int(amount)*10

                elif odds < 100:
                    embed.add_field(name=f"3x your money (Nice)",
                                    value="", inline=False)
                    win = int(amount)*3

                elif odds < 500:
                    embed.add_field(name=f"2x your money (Nice)",
                                    value="", inline=False)
                    win = int(amount)*2

                else:
                    embed.add_field(
                        name=f"Well you have lost all your money", value="", inline=False)

                self.data[str(ctx.author.id)]["bal"] += int(win)

            else:
                embed.add_field(
                    name=f"You cant gamble what you dont have", value="", inline=False)

            currentbal = self.data[str(ctx.author.id)]["bal"]
            embed.add_field(name=f"Current Balance",
                            value=f"🪙 {currentbal}", inline=False)

        await ctx.channel.send(embed=embed)
        saveData(self.data)

    @commands.command(name="steal")
    async def steal_prompt(self, ctx, target):
        """
        Take some coins from another ship 

        Description
        ___________________________________
        A way to get rich.

        Usage
        ___________________________________
        op!steal <@user>
        """

        self.data = addUser(self.data, str(ctx.author.id))

        match = re.search(r'\d+', target)
        targetUser = [member for member in ctx.channel.members if
                      member.id == int(match.group())][0]

        embed = discord.Embed(color=0xff00e6)

        self.data = addUser(self.data, str(targetUser.id))
        if targetUser.id == ctx.author.id:
            embed.add_field(
                name=f"You cant steal from yourself", value="", inline=False)
        elif self.data[str(targetUser.id)]["bal"] <= 0:
            embed.add_field(
                name=f"{targetUser.name} is poor, there is nothing to steal :(", value="", inline=False)
        else:

            userHealth = self.data[str(ctx.author.id)]["health"]
            targetHealth = self.data[str(targetUser.id)]["health"]
            userDefence = self.data[str(ctx.author.id)]["defence"]
            targetDefence = self.data[str(targetUser.id)]["defence"]
            userAttack = self.data[str(ctx.author.id)]["attack"]
            targetAttack = self.data[str(targetUser.id)]["attack"]

            userHealth -= max(targetAttack - random.randint(0, userDefence), 0)
            targetHealth -= max(userAttack -
                                random.randint(0, targetDefence), 0)

            if userHealth <= 0 and targetHealth <= 0:
                embed.add_field(
                    name=f"Seams you have both died :(", value=f"A small fortune was swept away by the ocean", inline=False)

                self.data = resetUser(self.data, ctx.author.id)
                self.data = resetUser(self.data, targetUser.id)

            elif userHealth <= 0:
                embed.add_field(
                    name=f"You have died, could be worse :(", value=f"", inline=False)

                self.data = resetUser(self.data, ctx.author.id)
                self.data[str(targetUser.id)]["health"] = targetHealth

            elif targetHealth <= 0:
                targetBal = self.data[str(targetUser.id)]["bal"]

                embed.add_field(
                    name=f"Your target has dies and left you with a small fortune", value=f"🪙 {str(targetBal)}", inline=False)

                self.data = resetUser(self.data, targetUser.id)
                self.data[str(ctx.author.id)]["bal"] += targetBal

                userBal = self.data[str(ctx.author.id)]["bal"]

                embed.add_field(
                    name=f"Balance", value=f"🪙 {str(userBal)}", inline=False)

                self.data[str(ctx.author.id)]["health"] = userHealth

                embed = genSymbolEmbed(
                    embed, userHealth, '❤️', 'Health', False)

            else:
                if self.data[str(targetUser.id)]["health"] - targetHealth == 0:
                    embed.add_field(
                        name=f"Your target dodged your attack", value="", inline=False)

                lootPerc = (self.data[str(targetUser.id)]["health"] -
                            targetHealth) / self.data[str(targetUser.id)]["health"]
                loot = int(self.data[str(targetUser.id)]["bal"]
                           * lootPerc * (random.randint(80, 100) / 100))

                self.data[str(ctx.author.id)]["health"] = userHealth
                self.data[str(targetUser.id)]["health"] = targetHealth
                self.data[str(ctx.author.id)]["bal"] += loot
                self.data[str(targetUser.id)]["bal"] -= loot

                userBal = self.data[str(ctx.author.id)]["bal"]

                embed.add_field(
                    name=f"You got away with", value=f"🪙 {str(loot)}", inline=False)
                embed.add_field(
                    name=f"Balance", value=f"🪙 {str(userBal)}", inline=False)

                embed = genSymbolEmbed(
                    embed, userHealth, '❤️', 'Health', False)

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

        bal = self.data[str(member.id)]["bal"]
        health = self.data[str(member.id)]["health"]
        attack = self.data[str(member.id)]["attack"]
        defence = self.data[str(member.id)]["defence"]

        embed.add_field(name="Balance", value=f"🪙 {bal}", inline=True)

        embed = genSymbolEmbed(embed, health, '❤️', 'Health')
        embed = genSymbolEmbed(embed, attack, '🗡️', 'Attack')
        embed = genSymbolEmbed(embed, defence, '🛡️', 'Defence', False)

        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Account Created At", value=member.created_at.strftime(
            "%B %d, %Y"), inline=True)
        embed.add_field(name="Server Join Date", value=member.joined_at.strftime(
            "%B %d, %Y"), inline=True)

        await ctx.channel.send(embed=embed)
        await ctx.channel.send(member.avatar_url)


def genSymbolEmbed(embed, multiple, symbol, text, connected=True):
    if multiple <= 10:
        embed.add_field(
            name=text, value=symbol*multiple, inline=connected)
    else:
        embed.add_field(
            name=text, value=symbol*10 + '+' + str(multiple-10), inline=connected)

    return embed


def resetUser(data, uid):
    del data[str(uid)]
    return addUser(data, uid)


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
