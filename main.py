import discord
import json
from discord .ext import commands

with open('settin.json','r',encoding=''utf8)as jfile: #chek the external
    jdata = json.load(jfile)

intent = discord.Intents.default()
intent.typing = False
intent.presences = False


bot = commands.Bot(command_prefix='!', intents=intent)

@bot.event
async def on_read():
    print(">> Bot is awake<<")
    
@bot.event
async def on_member_join(member):
  channel = bot.get_channel()
  await channel.send(f'{member}join!')

async def on_member_remove(member):
  channel = bot.get_channel()
  await channel.send(f'{member}leave!')
 
@bot.command()
async def ping(ctx):
  awit ctx.send(F'{round(bot.latency*1000)}ms')

bot.run(jdata['TOKEN'])
bot.run('MTA1NjkzNjEyNTM0NTg0NTM0OQ.G4JdL4.M65r3UKFbh71EbNT5N3nGY9R47uzWoiiEVnLaE')
