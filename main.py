import discord, os, keep_alive
from discord.ext import commands

activity = discord.Activity(type=discord.ActivityType.watching, name="femboys")

client = commands.Bot(command_prefix='7', self_bot=True, activity=activity, status=discord.Status.dnd)

client.remove_command('help')

@client.event
async def on_ready():
  print("Working")

keep_alive.keep_alive()

client.run(os.getenv("TOKEN"), bot=False)
