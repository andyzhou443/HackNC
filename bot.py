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
import matplotlib as matplotlib

from rtlsdr import *

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
