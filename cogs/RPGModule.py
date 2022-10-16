import discord
from discord.ext import commands
# from dataGetter import *
from PIL import Image
import io


class RPG(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name="gold")
    async def random_imassge(self, ctx):
        """
        Generates a TESTSTETSTSTESTTESTTS
        
        Description
        ___________________________________
        From all images on the OP fandom, generate a random image.
        
        Usage
        ___________________________________
        op!gold
        """
        
        # # imageName = randomFile()
        # # print(imageName)
        imageName = "Chiya.jpg"
        # # image = openImageData(imageName)
        # imagb = openBaseImageData(imageName)
        # charName = cleanName(imageName)
        # print(1)
        
        # width, height = imagb.size
        # print(width, height)
        # # image.thumbnail()

        # info = openCharData(charName)

        # print(2)
        # image = discord.File(imagb, filename="image.jpg")
        # print(3)
        
        # embedVar = discord.Embed(title=charName, color=0xed8b02)
        # print(4)
    
        # embedVar.set_image(url="attachment://image.jpg")
        # print(5)

        # await ctx.channel.send(file=image, embed=embedVar)
        # await ctx.channel.send(file=image.thumbnail(), embed=embedVar)
        print("test0")
        
        # imagb = Image.open(r"images/Chiya.jpg")
        # width, height = imagb.size
        # print(width, height)
        # print("test1")
        # image = discord.File(imagb, filename="image.jpg")
        # print("test2")
        
        # image = discord.to_file(filename="../images/Chiya.jpg")
    
        image = Image.open(f'images/{imageName}')
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)
        # image.save('temp.jpg')

        # image.show()
        # image2.show() 
        
        # print("test2")
        # picture = discord.File(image, filename="image.jpg")
        
        # await ctx.channel.send(file=picture)
        # print("test3")
        
        # print(2)
        # buf = io.BytesIO()
        # image.save(buf, format='JPEG')
        # byte_im = buf.getvalue()
        # print(2)


        # image = discord.File(byte_im, filename="image.jpg")
        # print(3)
        # # picture = discord.File(f, filename="image.jpg")
        
        # embedVar = discord.Embed(title="asdasdasd", color=0xed8b02)
        # print(4)
    
        # embedVar.set_image(url="attachment://image.jpg")
        # print(5)

        # await ctx.channel.send(file=byte_im, embed=embedVar)
        
        
        
        imageName = randomFile()
        image = openImageData(imageName)
        charName = cleanName(imageName)

        info = openCharData(charName)

        embedVar = discord.Embed(title=charName, color=0xed8b02)
        embedVar.set_image(url="attachment://image.jpg")

        await ctx.channel.send(file=image, embed=embedVar)
        
    @commands.command(name="profile")
    async def random_imassge(self, ctx):
        """
        Gets your profile
        
        Description
        ___________________________________
        Print out stats for your profile.
        
        Usage
        ___________________________________
        op!profile 
        """
        
        await ctx.channel.send("getpass.getuser()")
        await ctx.channel.send(ctx.author.id)
        await ctx.channel.send(ctx.author.name)
        
        embedVar = discord.Embed()
        embedVar.add_field(name="id", value=ctx.author.id, inline=False)
        embedVar.add_field(name="name", value=ctx.author.name, inline=False)
        

        await ctx.channel.send(embed=embedVar)

        
        
        

async def setup(client):
    await client.add_cog(RPG(client))
    print("Loaded RPG module")
    