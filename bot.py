import os

import discord
from discord.ext import commands

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(
    command_prefix='!'
)


@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(f'{bot.user.name} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})'
          )


@bot.command(name='sign', help='Reminds everyone to sign the attendance popup in Odyssey')
async def sign(ctx):
    response = '@everyone Émargement disponible !'
    await ctx.send(response)


@bot.command(name='sign', help='Reminds everyone to sign the attendance popup in Odyssey')
async def sign(ctx):
    response = '@everyone Émargement disponible !'
    await ctx.send(response)


bot.run(TOKEN)