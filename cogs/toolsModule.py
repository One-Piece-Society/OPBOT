import discord
from discord.ext import commands


class tool(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="ping")
    async def ping_tester(self, ctx):
        await ctx.channel.send('pong')

    # @commands.command(name="help")
    # async def my_kick_command(self, ctx):
    #     # embedVar = discord.Embed(
    #     #     title='Commands', description='To use bot type op![command]', color=0x1d02ed)
    #     # embedVar.add_field(
    #     #     name="Image 🖼️", value='rimage, rdata', inline=False)
    #     # embedVar.add_field(name="Utility ⚙️", value='ping', inline=False)

    #     # await ctx.channel.send(embed=embedVar)
    #     await ctx.channel.send('asdasd')


async def setup(client):
    await client.add_cog(tool(client))
    print("Loaded tools module")
