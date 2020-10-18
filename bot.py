
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mlab
import matplotlib.gridspec as gridspec
from rtlsdr import *
#test
import asyncio
import functools
import itertools
import discord
import youtube_dl


from discord.ext import commands

spectrograph = RtlSdr()
client = commands.Bot(command_prefix='.')


players = {}

#code to start the discord bot when compiled
@client.event
async def on_ready():

    print('RadioBot is ready to receive frequency')

    print('RadioBot is ready')

#code to allow bot to connect to voice channel
@client.command(pass_context=True)
async def join(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()

#code to allow bot to play audio stream
@client.command(pass_context=True)
async def play (ctx,url):
    server = ctx.message.server
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
    player = await voice_client.create_ytdl_player(url)
    player.start

@client.command(pass_context=True)
async def tune (ctx):

    client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')

@client.event
async def on_message(message):
    global frequency
    userInput = await client.wait_for('message')
    frequency = (float(userInput))


# This is to create a large enough data set for the
# psuedo random generator for this plot to work
np.random.seed(142069999)

eigenvalue = 0.01
ax = np.arange(0, 10, eigenvalue)
n = np.random.rand(len(ax))
by = np.exp(-ax / 0.05)

convolved = np.convolve(n, by) * eigenvalue
convolved = convolved[:len(ax)]
sides = 0.01 * np.sin(2 * np.pi * ax) + convolved

# This plots the values for the power spectral density graph
plt.subplot(200)
plt.plot(ax, sides)
plt.subplot(215)
plt.psd(sides, 515, 1 / eigenvalue)

plt.show()

