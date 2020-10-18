import discord
import argparse
import ctypes
import os
import youtube_dl
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

players = {}

#code to start the discord bot when compiled
@client.event
async def on_ready():
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


#bot token
client.run('NzY3MDY2MTIwMzA1MjQ2MjE4.X4sf_g.RjIpDVFJ3UKD0bRAPRE7dk1Vqe4')


