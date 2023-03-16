import discord
import random
import json

with open('settin.json','r',encoding='utf8')as jfile:  #chek the external
    jdata = json.load(jfile)                           #隻料庫

from discord.ext import commands
from core.classes import Cog_Extension

class React(Cog_Extension):
    @commands.command()
    async def 梗圖(self,ctx):
        random_pic = random.choice(jdata['pic'])                                                        #主機端圖片 簡略版 隨機
        pic = discord.File(random_pic) 
        await ctx.send(file = pic)



    
    @commands.command()
    async def web(self,ctx):
        random_pic = random.choice(jdata['url_pic'])                                                        #主機端圖片 簡略版 隨機
        await ctx.send(random_pic)    

def setup(bot):
    bot.add_cog(React(bot))     