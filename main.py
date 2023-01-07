import discord
import json
from discord .ext import commands


with open('settin.json','r',encoding=''utf8)as jfile: #chek the external
    jdata = json.load(jfile)

    
intent = discord.Intents.default()
intent.typing = False
intent.presences = False


bot = commands.Bot(command_prefix='!', intents=intent) #版本


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
 

@bot.command()                                      #ex A: HI (上文) [使用者, id, 所在伺服器, 所在頻道]
async def ping(ctx):    # "ctx" context 上下文           B: HI (下文)
  awit ctx.send(F'{round(bot.latency*1000)}ms') #"ctx" 包含上述資訊 ⇧⇧⇧ 的變數
  #awit 送出                  #延遲

    
@bot.command()
async def 梗圖(ctx):
    pic = discord.File() #主機圖片連結 \\轉譯
    awiat ctx.send()

    
    
bot.run(jdata['TOKEN'])         #"TOKEN" create 
bot.run('MTA1NjkzNjEyNTM0NTg0NTM0OQ.G4JdL4.M65r3UKFbh71EbNT5N3nGY9R47uzWoiiEVnLaE')
