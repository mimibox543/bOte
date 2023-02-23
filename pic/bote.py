import discord
import json
import random

from discord .ext import commands


with open('settin.json','r',encoding='utf8')as jfile:  #chek the external
    jdata = json.load(jfile)                           #隻料庫

    
intent = discord.Intents.default()
intent.typing = False
intent.presences = False


bot = commands.Bot(command_prefix='!', intents=intent)  #版本


@bot.event
async def on_read():
    print(">> Bot is awake<<")                          #啟動
    
    
@bot.event
async def on_member_join(member):
  channel = bot.get_channel()                           #頻道 ID
  await channel.send(f'{member}join!')

    
async def on_member_remove(member):
  channel = bot.get_channel()                           #頻道 ID
  await channel.send(f'{member}leave!')
 



"""   
@bot.command()
async def 梗圖(ctx):
   pic = discord.File() #主機圖片連結 \\轉譯                                                        #主機端圖片
   awiat ctx.send(file = pic)
"""

    
"""   
@bot.command()
async def 梗圖(ctx):
   pic = discord.File(jdata['pic']) #主機圖片連結 \\轉譯                                            #主機端圖片 簡略版
   awiat ctx.send(file = pic)
"""


   
              



bot.run(jdata['TOKEN'])         #"TOKEN" create 
#bot.run('MTA1NjkzNjEyNTM0NTg0NTM0OQ.G4JdL4.M65r3UKFbh71EbNT5N3nGY9R47uzWoiiEVnLaE')                



"""
{
    "TOKEN": "MTA1NjkzNjEyNTM0NTg0NTM0OQ.G4JdL4.M65r3UKFbh71EbNT5N3nGY9R47uzWoiiEVnLaE",           #金鑰
    "Welcome": ""                                                                                  #頻道 ID
    "Leave_channel": ""                                                                            #頻道 ID
    
    
    "pic": "   ,   "        #圖片路徑                                                              #主機端圖片 簡略版
                #2+以上圖片隨機取樣
    "url_pic": ["https://i0.wp.com/www.printmag.com/wp-content/uploads/2021/02/4cbe8d_f1ed2800a49649848102c68fc5a66e53mv2.gif?resize=476%2C280&ssl=1"]
                                                                                                  #url 圖
}
"""
