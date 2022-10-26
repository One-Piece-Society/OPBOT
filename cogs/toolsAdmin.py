import discord
from discord.ext import commands
import time


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="verifyGFWebHKPPServer2022")
    async def verify_ping(self, ctx):
        await ctx.channel.send('verifyiing')
        await ctx.channel.send(ctx.channel.id)

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if ctx.webhook_id == 1034044078821736458 and "verifyGFWebHKPPServer2022" in ctx.message:
            modChan = self.client.get_channel(790513461465317386)
            print(type(modChan))
            await ctx.channel.send("received")
            await modChan.send("testing message being sent from anoter server")

async def setup(client):
    await client.add_cog(admin(client))
    print("Loaded Admin module")
