import discord
from discord.ext import commands
from dataGetter import *
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Multiplayer(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.activeGames = []

    @commands.Cog.listener()
    async def on_message(self, ctx):
        if config['testing']['DisableMultiplayer'] == "true":
            return

        print("ceas")
    
    

async def setup(client):
    await client.add_cog(Multiplayer(client))
    print("Loaded Multiplayer module")