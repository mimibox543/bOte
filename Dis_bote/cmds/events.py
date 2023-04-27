import discord
import random
import json

from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json','r',encoding='utf8')as jfile:  #chek the external
    jdata = json.load(jfile)                           #隻料庫

class Event(Cog_Extension):
    @commands.Cog.listener()                                              #member join
    async def on_member_join(self,member):
        channel = self.bot.get_channel(int[jdata['welcome_channel']])                           #頻道 ID
        await channel.send(f'{member}下來了')

    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = self.bot.get_channel(int[jdata['leave_channel']])                             #頻道 ID
        await channel.send(f'{member}上了西天')
@commands.Cog.listener()
async def on_message(self, msg):
    if msg.content == 'apple':
        await msg.channel.sen('hi')

def setup(bot):
    bot.add_cog(Event(bot))     