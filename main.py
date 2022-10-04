from dataGetter import *

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

        if message.content == 'op!ping':
            await message.channel.send('pong')

        if message.content == 'op!rimage':

            imageName = randomFile()
            image = openImageData(imageName)
            charName = clean(imageName)
            
            info = openCharData(charName)
            
            embedVar = discord.Embed(title=charName, color=0xed8b02)
            embedVar.set_image(url="attachment://image.jpg")

            await message.channel.send(file=image, embed=embedVar)

        if message.content == 'op!rdata':

            imageName = randomFile()
            image = openImageData(imageName)
            charName = clean(imageName)
            
            info = openCharData(charName)
            
            embedVar = discord.Embed(title=f"{charName} ()", color=0xed8b02)
            embedVar.set_image(url="attachment://image.jpg")

            await message.channel.send(file=image, embed=embedVar)
            
        if message.content == 'op!help':
            embedVar = discord.Embed(title='Commands', description='To use bot type op![command]', color=0x1d02ed)
            embedVar.add_field(name="Image 🖼️", value='rimage, rdata', inline=False)
            embedVar.add_field(name="Utility ⚙️", value='ping', inline=False)
            
            await message.channel.send(embed=embedVar)

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run(extract_key())

    
    