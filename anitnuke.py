import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

bot.command = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Antinuke is ready!")

@bot.command()
@commands.has_permissions(manageChannels=True)
async def clearnuke(ctx, channelName):
    guild = ctx.guild

    embed = discord(title="Success", description="{} Has been succesfully created!".format(channelName))
    await guild.create_text_channel(name="{}".format(channelName))
    await ctx.send(embed=embed)

bot.run('OTc1NzgwODA5OTg4NTE3OTI4.Gd67Ip.EmqeRRlL36zyzuZi-NVJxg1m7UslcCa2rmIo0o')