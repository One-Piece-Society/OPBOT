import discord
from discord.ext import commands
from dataGetter import *
from PIL import Image
import io
import json
import time
import random

class Multiplayer(commands.Cog):
    def __init__(self, client):
        self.client = client

async def setup(client):
    await client.add_cog(Multiplayer(client))
    print("Loaded Multiplayer module")