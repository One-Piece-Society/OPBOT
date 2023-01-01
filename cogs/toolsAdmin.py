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

    @commands.command(name="findid")
    async def find_id(self, ctx, name):
        uname = "HUM#3250"
        print(uname)
        print(discord.version_info)
        print(type(ctx))
        print(type(self.client))
        # user = ctx.users.find("username", "TESTname");

        # guild = ctx.guild
        # print("break0")
        # print(guild)
        # print(discord.ctx(users))
        # for guild in ctx.guilds:
        #     print("mem")
        #     for member in guild.members:
        #         print("in")

        print(self.client.users)
        
        # user_id = await find_user_id(guild, name)
        # print("break1")
        
        # if user_id:
        #     await ctx.channel.send(f'The user ID of {name} is {user_id}')
        # else:
        #     await ctx.channel.send(f'No user was found with the name {name}')


async def setup(client):
    await client.add_cog(admin(client))
    print("Loaded Admin module")

async def find_user_id(guild, name):
    print("break1-a")
    member = discord.utils.get(guild.members, lambda m: m.name == name)
    print(member)
    if member:
        return member.id
    return None