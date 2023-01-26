import discord
from discord.ext import commands
from dataGetter import *


class Image(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="rimage")
    async def random_image(self, ctx):
        """
        Generates a random image
        
        Description
        ___________________________________
        From all images on the OP fandom, generate a random image.
        
        Usage
        ___________________________________
        op!rimage
        """
        
        imageName = randomFile()
        image = openImageData(imageName)
        charName = cleanName(imageName)

        info = openCharData(charName)

        embedVar = discord.Embed(title=charName, color=0xed8b02)
        embedVar.set_image(url="attachment://image.jpg")

        await ctx.channel.send(file=image, embed=embedVar)

    @commands.command(name="rdata")
    async def random_image_data(self, ctx):
        """
        Generates a random image with data
        
        Description
        ___________________________________
        From all images on the OP fandom, generate a random image
        and the character stats.
        
        Usage
        ___________________________________
        op!rdata
        """
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
    await client.add_cog(Image(client))
    print("Loaded image module")
