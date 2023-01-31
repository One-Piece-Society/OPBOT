import os
import random
import re
import discord
import json
from PIL import Image


def randomFile():
    return (random.choice(os.listdir("images")))


def openImageData(imgName, folder="images/"):
    with open(folder + str(imgName), 'rb') as f:
        picture = discord.File(f, filename="image.jpg")

    return picture

def openBaseImageData(imgName):
    # with open(f'images/{imgName}', 'rb') as f:
    #     picture = discord.File(f, filename="image.jpg")

    return Image.open(f'images/{imgName}')

def openCharData(charName):
    datafile = open('cleanData.json', 'r')
    data = json.load(datafile)
    return data[charName]['Statistics']


def cleanName(imageName):
    return str(imageName.replace(".jpg", ""))

def cleanCrotchets(text):
    if ']' in str(text):  
        return re.sub(r'\[.*?\]', '' , text)
    return text

def addAllData(embed, info):
    for key in info:
        if key != 'Japanese Name' and len(key) != 0:
            embed.add_field(name=key, value=cleanCrotchets(info[key]), inline=False)
    
    return embed
