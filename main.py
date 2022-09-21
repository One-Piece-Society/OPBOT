import discord
import os, random
import json

def extract_key():
    f = open("api.key", "r")
    return f.read().replace("DiscordAPI-Key =", "")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == 'randomimage':

            imageName = random.choice(os.listdir("images"))
            with open(f'images/{imageName}', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
            
            await message.channel.send(imageName.replace(".jpg", ""))

        if message.content == 'datarandomimage':

            imageName = random.choice(os.listdir("images"))
            with open(f'images/{imageName}', 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
            
            datafile = open('cleanData.json', 'r')
            data = json.load(datafile)
            info = data[str(imageName.replace(".jpg", ""))]
            
            await message.channel.send(info)


if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(extract_key())

    
    