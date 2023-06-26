import requests
import random
import discord
import asyncio
from discord.ext import commands

import os
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mem(ctx):
    f = ['images', 'barotrauma']
    j = (random.choice(f))
    a = (os.listdir (j))
    print(a)
    b = random.choice(a)
    print(b)
    with open(f'{j}/{b}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
 
@bot.command()
async def cat(ctx):
    a = (os.listdir('cats'))
    print(a)
    b = random.choice(a)
    print(b)
    with open(f'cats/{b}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("MTExNjAyNDcyNjEwMDM4NTg1Mg.Gjj3Ra.1KLb6Lk589Qi-AbxaEK7c9LokCEEF8cx00Ush4")