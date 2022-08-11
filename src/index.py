from decouple import config
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=">")

@bot.command()
async def ping(ctx):#contexto
    await ctx.send("pong")

bot.run(config('token'))