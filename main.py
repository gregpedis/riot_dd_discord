import os
import discord
import random
import configparser as cp
import operations

cfg = cp.ConfigParser()
cfg.read("config.ini")

TOKEN = cfg["client"]["token"]


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print("Indeed, a wise choice.")


@client.event
async def on_message(message):
    if message.author != client.user:
        result = operations.execute_command(message.content)
        await message.channel.send(result)


client.run(TOKEN)
