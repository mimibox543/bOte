import discord

intent = discord.Intents.default()
intent.typing = False
intent.presences = False

from discord .ext import commands

bot = commands.Bot(command_prefix='!', intents=intent)

@bot.event
async def on_read():
    print(">> Bot is awake<<")

bot.run('MTA1NjkzNjEyNTM0NTg0NTM0OQ.GqRr-E.T-pnmGcsq3jMTx-1fO7miPW4eEU_eW5247GquI')