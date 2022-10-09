import discord
from discord.ext import commands

print("tools loded")


class tool(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="kick")
    async def my_kick_command(self, ctx):
        print("kicking rayell")

    @commands.Cog.listener()
    async def on_ready(self):
        # an example event with cogs
        print("1")

    @commands.command()
    async def command(self, ctx):
        # an example command with cogs
        print("2")


async def setup(client):  # Must have a setup function
    await client.add_cog(tool(client))  # Add the class to the cog.
