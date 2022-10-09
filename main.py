import asyncio
import discord
from dataGetter import *
from discord.ext import commands
from cogs.toolsModule import setup

prefix = 'opt!'

def extract_key():
    f = open("api.key", "r")
    return f.read().replace("DiscordAPI-Key =", "")

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('Logged on as', self.user)

#     async def on_message(self, message):
#         # don't respond to ourselves
#         if message.author == self.user:
#             return
        
#         # clean up message 
#         if message.content.lower().startswith(prefix + 'ping'):
#             await message.channel.send('pong')

        # if message.content.lower().startswith(prefix + 'rimage'):

        #     imageName = randomFile()
        #     image = openImageData(imageName)
        #     charName = cleanName(imageName)
            
        #     info = openCharData(charName)
            
        #     embedVar = discord.Embed(title=charName, color=0xed8b02)
        #     embedVar.set_image(url="attachment://image.jpg")

        #     await message.channel.send(file=image, embed=embedVar)

        # if message.content.lower().startswith(prefix + 'rdata'):

        #     imageName = randomFile()
        #     image = openImageData(imageName)
        #     charName = cleanName(imageName)
            
        #     info = openCharData(charName)
            
        #     embedVar = discord.Embed(title=f"{charName} - {info['Japanese Name']}", color=0xed8b02)
        #     embedVar.set_image(url="attachment://image.jpg")

        #     embedVar = addAllData(embedVar, info)
        #     await message.channel.send(file=image, embed=embedVar)

            
        # if message.content.lower().startswith(prefix + 'help'):
        #     embedVar = discord.Embed(title='Commands', description='To use bot type op![command]', color=0x1d02ed)
        #     embedVar.add_field(name="Image 🖼️", value='rimage, rdata', inline=False)
        #     embedVar.add_field(name="Utility ⚙️", value='ping', inline=False)
            
        #     await message.channel.send(embed=embedVar)
            
        # if message.content.lower().startswith(prefix + 'image'):
        #     print("look up image")
    
# # if __name__ == '__main__':
# intents = discord.Intents.default()
# intents.message_content = True
# # client = MyClient(intents=intents)
# # client = commands.Bot(command_prefix="opt!") # <- Choose your prefix
# # client.load_extension("toolsModule.py")

# client = commands.Bot(intents=intents, command_prefix = "opt!") 
# async with client:
    
#     # client.add_cog("toolsModule")
#     # setup(client)
#     await client.run(extract_key())
    
async def main():
    intents = discord.Intents.default()
    intents.message_content = True
    client = commands.Bot(intents=intents, command_prefix = "opt!") 
    async with client:
        await client.load_extension("cogs.toolsModule")
        await client.start(extract_key())

asyncio.run(main())


