import asyncio
import functools
import itertools
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('RadioBot is ready')
  
@client.command(pass_context = True)
async def summon (ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')


