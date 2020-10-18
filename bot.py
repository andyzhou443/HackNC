
# import discord
# from discord.ext import commands
#
# client = commands.Bot(command_prefix='.')
#
#
# @client.event
# async def on_ready():
#     print('RadioBot is ready')
#
#
# client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.2nb80DzQXew57JggCiW1-gq00zc')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mlab
import matplotlib.gridspec as gridspec
from rtlsdr import *

import asyncio
import functools
import itertools
import discord

from discord.ext import commands

spectrograph = RtlSdr()
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():

    print('RadioBot is ready to receive frequency')

    print('RadioBot is ready')
  
@client.command(pass_context = True)
async def summon (ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)



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

