import discord

from discord .ext import commands
from core.classes import Cog_Extension


class Main(Cog_Extension):
             # class 裡的功能都需放self

    @commands.command()                                                                      #ex A: HI (上文) [使用者, id, 所在伺服器, 所在頻道]
    async def ping(self,ctx):                                    # "ctx" context 上下文          B: HI (下文)
        await ctx.send(F'{round(self.bot.latency*1000)}ms')         #"ctx" 包含上述資訊 ⇧⇧⇧ 的變數
        #awit 送出                  #延遲

def setup(bot):
    bot.add_cog(Main(bot))
