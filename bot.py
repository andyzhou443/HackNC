import asyncio
import functools
import itertools
import math
import random

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('RadioBot is ready')

@client.command(name='summon')
@commands.has_permissions(manage_guild=True)
async def _summon(self, ctx: client.Context, *, channel: discord.VoiceChannel = None):
    """Summons the bot to a voice channel.
    If no channel was specified, it joins your channel.
    """

    if not channel and not ctx.author.voice:
        raise VoiceError('You are neither connected to a voice channel nor specified a channel to join.')

    destination = channel or ctx.author.voice.channel
    if ctx.voice_state.voice:
        await ctx.voice_state.voice.move_to(destination)
        return

ctx.voice_state.voice = await destination.connect()
     
spectrograph = RtlSdr()

from discord.ext import commands

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print('RadioBot is ready to receive frequency')


bot.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')


@bot.event
async def on_message(message):
    global frequency
    userInput = await bot.wait_for('message')
    frequency = (int(userInput))


spectrograph.sample_rate = frequency
spectrograph.center_freq = frequency * 45
spectrograph.gain = 'auto'

spectrograph.close()

psd()


client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')


