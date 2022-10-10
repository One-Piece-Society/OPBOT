import discord
from discord.ext import commands


class image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="ping")
    async def ping_tester(self, ctx):
        await ctx.channel.send('pong')


async def setup(client):
    await client.add_cog(image(client))
    print("Loaded image module")
