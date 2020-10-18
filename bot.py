import asyncio
import functools
import itertools
import math
import random

import discord
from async_timeout import timeout
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('RadioBot is ready')

@client.command(name='join', invoke_without_subcommand=True)
async def join(ctx):
   destination = ctx.author.voice.channel
   if ctx.voice_state.voice:
     await ctx.voice_state.voice.move_to(destination)
     return

   ctx.voice_state.voice = await destination.connect()
   await ctx.send(f"Joined {ctx.author.voice.channel} Voice Channel")
     
spectrograph = RtlSdr()

from discord.ext import commands

@client.event
async def on_ready():
    print('RadioBot is ready to receive frequency')

@client.event
async def on_message(message):
    global frequency
    userInput = await client.wait_for('message')
    frequency = (int(userInput))


spectrograph.sample_rate = frequency
spectrograph.center_freq = frequency * 45
spectrograph.gain = 'auto'

spectrograph.close()

psd()

client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')


