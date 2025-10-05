import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='greg°', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} has declared readiness status.")

@bot.event
async def on_connect():
    print(f"{bot.user.name} has successfully connected to Discord. Awaiting readiness status from {bot.user.name}")

@bot.command()
async def hai(ctx):
    await ctx.reply(f"Hai {ctx.author}!")

@bot.command()
async def greg(ctx):
    await ctx.reply('Oh, you wanna see me? Alrighty.')
    img = discord.File('greggy/caption.jpg','gregor.jpg')
    await ctx.send('here',file=img)

@bot.command()
async def backstory(ctx):
    text = open('greggy/meta.txt', 'rt')
    await ctx.reply("Sure! I'll tell you my backstory in just a second :3")
    x = 0
    while x <= 61:
        bs = text.read(2000)
        await ctx.send(bs)
        x += 1

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
