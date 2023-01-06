import asyncio
import os
import discord
from discord.ext import commands
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
    
def extract_key():    
    return config['keys']['DiscordAPI-Key']

async def main():
    
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True

    if config['testing']['isproduction'] == 'true':
        client = commands.Bot(intents=intents, command_prefix=["op!","Op!"])
    else:
        client = commands.Bot(intents=intents, command_prefix=["opt!"])

    async with client:
        for cogFile in os.listdir("cogs"):
            if cogFile.endswith(".py"):
                await client.load_extension(f'cogs.{cogFile[:-3]}')

        await client.start(extract_key())

asyncio.run(main())
