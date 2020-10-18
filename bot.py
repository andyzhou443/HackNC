import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('RadioBot is ready')
  
@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')


