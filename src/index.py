#pipenv shell - py src/index.py
from decouple import config
import discord
from discord.ext import commands
from discord import client

bot = commands.Bot(command_prefix="=>")

@bot.command()
async def ping(ctx):#contexto
    await ctx.send("pong")

@bot.command()
async def play(ctx,url):
    canal = ctx.guild.voice_channels
    canaldevoz = discord.utils.get(canal, name = "General") #obtener canal de voz "General"
    voz = discord.utils.get(client.voice_clients, guild= ctx.guild)
    await canaldevoz.connect()
    if not voz.is_connection(): #si ya esta conectado en un canal de voz no lo vuelva a conectar
        await ctx.send(f"reproduciendo:{url}")

@bot.command()    
async def pausa(ctx):
    voz = discord.utils.get(client.voice_clients, guild= ctx.guild)
    if voz.is_playing():
        voz.pause()
    else:
        await ctx.send("MK, el bot no esta reproduciendo nada no joda y si todas estas mierdas estan validadas xd")

@bot.command()
async def resume(ctx):
    voz = discord.utils.get(client.voice_clients, guild= ctx.guild)
    if voz.is_paused():
        voz.resume()
    else:
        await ctx.send("MK, el audio no esta pausado...")

bot.run(config('token'))