import asyncio
import os
import discord
from discord.ext import commands


def extract_key():
    f = open("api.key", "r")
    return f.read().replace("DiscordAPI-Key =", "")


async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    # client = commands.Bot(intents=intents, command_prefix=["op!","Op!"])
    client = commands.Bot(intents=intents, command_prefix=["opt!"])
    async with client:
        for cogFile in os.listdir("cogs"):
            if cogFile.endswith(".py"):
                await client.load_extension(f'cogs.{cogFile[:-3]}')

        await client.start(extract_key())

asyncio.run(main())
