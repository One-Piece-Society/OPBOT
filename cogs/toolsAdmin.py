import discord
from discord.ext import commands
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, ctx):
        # TODO reimplement
        # print(type(ctx.content))

        verifyCommand = config['verification']['webhookCommand']

        # ctx.webhook_id == config['verification']['webhookBotID'] and
        if verifyCommand in ctx.content:

            verifcationName = ctx.content[len(verifyCommand)+1:]

            found = False
            authChannel = self.client.get_channel(
                int(config['verification']['targetChannelID']))

            user = next((member for member in authChannel.members if str(
                member) == verifcationName), None)

            if user == None:
                print("not foudn ")
                # TODO implement error state 

            else:
                removalRole = discord.utils.get(authChannel.guild.roles, name=config['verification']['unverifiedRole'])                
                verifiedRole = discord.utils.get(authChannel.guild.roles, name=config['verification']['verifiedRole'])

                if removalRole in user.roles:
                    await user.remove_roles(removalRole)

                if verifiedRole not in user.roles:
                    await user.add_roles(verifiedRole)

            # if found == False:
            #     #  TODO add error channel code
            #     errorChan = self.client.get_channel(here)
            #     await errorChan.send("Welcome to the server!")
            # else:
            #     # send a welcome message

            #     await authChannel.send("Welcome @ping to the server!")

            await ctx.channel.send("received")
        elif "admin!debugInfo" == ctx.content and ctx.author.id == int(config['adminstration']['level1OverRide']):

            infoMessage = f'''Setup Info

            Username: {ctx.author.name}
            User ID: {ctx.author.id}
            Channel ID: {ctx.channel.id}
            Server (Guild) ID: {ctx.guild.id}
        
            Discord Usage Info: {discord.version_info}
            '''

            await ctx.channel.send(infoMessage)

    # @commands.command(name="findid")
    # async def find_id(self, ctx, name):
    #     uname = "HUM#3250"
    #     print(uname)
    #     print(discord.version_info)
    #     print(type(ctx))
    #     print(type(self.client))
    #     # user = ctx.users.find("username", "TESTname");

    #     # guild = ctx.guild
    #     # print("break0")
    #     # print(guild)
    #     # print(discord.ctx(users))
    #     # for guild in ctx.guilds:
    #     #     print("mem")
    #     #     for member in guild.members:
    #     #         print("in")

    #     # print(self.client.users)
    #     # # print("----------")
    #     # print(self.client.get_all_channels())

    #     channel = self.client.get_channel(1018874117870583828)
    #     await channel.send("Hello, world!")

    #     # print(channel.members)
    #     # print(channel.members[0])

    #     # print(channel.members[1])
    #     # print(name)
    #     for name1 in channel.members:
    #         # print(type(name1))
    #         if str(name1) == name:
    #             # print("found result of user")
    #             # print(type(name1))
    #             await channel.send(f'<@{name1.id}> pong!')

    #             # role = discord.utils.get(self.client.get_channel(1018874117870583828).roles, name='x1xx1')
    #             print("new line ")
    #             guild = self.client.get_guild(680709749960081427)

    #             print("asd")
    #             print(guild.roles)
    #             role = discord.utils.get(guild.roles, name='xxx1')

    #             # print(role)
    #             print(type(role))

    #             await name1.remove_roles(role)

    #     # print(f"error user "{name}" not found or needs manual verification ")
    #     # print(ctx.channel.id)

    #     # user_id = await find_user_id(guild, name)
    #     # print("break1")

    #     # if user_id:
    #     #     await ctx.channel.send(f'The user ID of {name} is {user_id}')
    #     # else:
    #     #     await ctx.channel.send(f'No user was found with the name {name}')


async def setup(client):
    await client.add_cog(admin(client))

    print("Loaded Admin module")
