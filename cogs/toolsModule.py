import discord
from discord.ext import commands
import time


class tool(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.st = time.time()

    @commands.command(name="ping")
    async def ping_tester(self, ctx):
        """
        Tests connection to the bot server

        Description
        ___________________________________
        Returns a pong once a request to the server is seen. 
        To test speed you must count the time yourself.

        Usage
        ___________________________________
        op!ping
        """
        await ctx.channel.send('pong')

    @commands.command(name="uptime")
    async def uptime_tool(self, ctx):
        """
        Recalls the uptime of the bot

        Description
        ___________________________________
        Returns the ammount of time the docker instance has been running for.

        Usage
        ___________________________________
        op!uptime
        """
        seconds = time.time() - self.st
        days = seconds // 86400
        hours = (seconds - (days * 86400)) // 3600
        minutes = (seconds - (days * 86400) - (hours * 3600)) // 60
        sec = int(seconds - (days * 86400) - (hours * 3600) - minutes*60)

        await ctx.channel.send(f"OPBOT up since {time.ctime(self.st)} \nUp for {int(days)} days, {int(hours)} hours, {int(minutes)} minutes and {sec} seconds")


async def setup(client):
    await client.add_cog(tool(client))
    print("Loaded tools module")
