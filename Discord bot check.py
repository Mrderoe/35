import discord
from bot_logic import gen_pass
from bot_logic import randemoj
from bot_logic import gamerps
from bot_logic import coin
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)
a = 'l'
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('code'):
        response = gen_pass(10)
        await message.channel.send(response)
    elif message.content.startswith('coin'):
        response = coin()
        await message.channel.send(response)
    elif message.content.startswith('game'):
        response = gamerps()
        await message.channel.send(response)
    elif message.content.startswith('lol'):
        response = randemoj()
        await message.channel.send(response)
    elif message.content.startswith('hello'):
        await message.channel.send("Hi")
    elif message.content.startswith('bye'):
        await message.channel.send("goodbye")
    elif message.content.startswith('hey?'):
        await message.channel.send("what?")
    else:
        await message.channel.send(message.content)
client.run('MTExNjAyNDcyNjEwMDM4NTg1Mg.GltsBb.VH7RTWUIPpnCu1ocPeEs0AzqoGo7VG-1vuqCmM')