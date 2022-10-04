import os
import random
import discord
import json


def randomFile():
    return (random.choice(os.listdir("images")))


def openImageData(imgName):
    with open(f'images/{imgName}', 'rb') as f:
        picture = discord.File(f, filename="image.jpg")

    return picture


def openCharData(charName):
    datafile = open('cleanData.json', 'r')
    data = json.load(datafile)
    return data[charName]


def clean(imageName):
    return str(imageName.replace(".jpg", ""))
