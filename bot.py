import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('RadioBot is ready')

client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.2nb80DzQXew57JggCiW1-gq00zc')
