import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

client = commands.Bot(command_prefix = '&')

@client.command()
async def load(ctx,extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx,extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if(filename.endswith('.py')):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(os.getenv("api-token"))
