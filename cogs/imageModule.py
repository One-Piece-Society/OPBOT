import discord
from discord.ext import commands
from dataGetter import *


class image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rimage")
    async def random_image(self, ctx):
        imageName = randomFile()
        image = openImageData(imageName)
        charName = cleanName(imageName)

        info = openCharData(charName)

        embedVar = discord.Embed(title=charName, color=0xed8b02)
        embedVar.set_image(url="attachment://image.jpg")

        await ctx.channel.send(file=image, embed=embedVar)

    @commands.command(name="rdata")
    async def random_image_data(self, ctx):
        imageName = randomFile()
        image = openImageData(imageName)
        charName = cleanName(imageName)

        info = openCharData(charName)

        embedVar = discord.Embed(
            title=f"{charName} - {info['Japanese Name']}", color=0xed8b02)
        embedVar.set_image(url="attachment://image.jpg")

        embedVar = addAllData(embedVar, info)
        await ctx.channel.send(file=image, embed=embedVar)


async def setup(client):
    await client.add_cog(image(client))
    print("Loaded image module")
