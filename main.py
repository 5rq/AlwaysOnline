import discord, json
from discord.ext import commands

with open('config.json') as c:
    config = json.load(c)

token = config.get('token')
status = config.get('status')

bot = commands.Bot(self_bot=True, status=discord.Status.{status})

@bot.event
async def on_ready():
    print(f'Running as {bot.user.name}#{bot.user.discriminator}')

bot.run(token)
