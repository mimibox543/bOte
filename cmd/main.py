import discord

from discord .ext import commands



class Main(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @bot.command()                                                                      #ex A: HI (上文) [使用者, id, 所在伺服器, 所在頻道]
    async def ping(ctx):                                    # "ctx" context 上下文          B: HI (下文)
        await ctx.send(F'{round(bot.latency*1000)}ms')         #"ctx" 包含上述資訊 ⇧⇧⇧ 的變數
    #awit 送出                  #延遲
