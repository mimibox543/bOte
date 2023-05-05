import discord
import json
import random
import os
from discord.ext import commands

intents = discord.Intents.all()
                          #read(mode)模式
with open('setting.json','r',encoding='utf8')as jfile:  #chek the external
    jdata = json.load(jfile)         #編碼              #資料庫



    
#_________________________________________________________________________________________________________________


#bot = commands.Bot(command_prefix='!', intents=intents)  #版本 
bot = commands.Bot(command_prefix='!', help_command=commands.DefaultHelpCommand()) 


@bot.event                                              #bot awake
async def on_ready():
    print(">>bot is online<<")

@bot.event                                              #member join
async def on_member_join(member):
  channel = bot.get_channel(int[jdata['welcome_channel']])                           #頻道 ID
  await channel.send(f'{member}下來了')

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(int[jdata['leave_channel']])                             #頻道 ID
  await channel.send(f'{member}上了西天')
"""
@bot.command()                                                                      #ex A: HI (上文) [使用者, id, 所在伺服器, 所在頻道]
async def ping(ctx):                                    # "ctx" context 上下文          B: HI (下文)    ⇧⇧⇧
        await ctx.send(F'{round(bot.latency*1000)}ms')                         #"ctx" 包含上述資訊 ⇧⇧⇧ 的變數
        #awit 送出         #四捨五入         #延遲

@bot.command()
async def 梗圖(ctx):
   randm_pic = random.choice(jdata['pic'])
   pic = discord.File(randm_pic) #主機圖片連結 \\轉譯                                                        #主機端圖片
   await ctx.send(file = pic)

@bot.command()
async def web(ctx):
   randm_pic = random.choice(jdata['url_pic'])
   await ctx.send(randm_pic)
"""

"""for Filename in os.listdir('./cmds'):                #list 列表
   if Filename.endswith('.py'):                         #偵查尾句.py
      bot.load_extension(F'cmds.{Filename[:-3]}') """      # -3 →倒數格字，print算到那為止

@bot.command()
async def load(ctx, extension):
   bot.load_extension(F'cmds.{extension}')
   await ctx.send(f'loaded {extension} done.')

@bot.command()
async def unload(ctx, extension):
   bot.unload_extension(F'cmds.{extension}')
   await ctx.send(f'unloaded {extension} done.')

@bot.command()
async def reload(ctx, extension):
   bot.reload_extension(F'cmds.{extension}')
   await ctx.send(f'reloaded {extension} done.')   
   
if __name__ == "__main__":
  bot.run(jdata['TOKEN'])
