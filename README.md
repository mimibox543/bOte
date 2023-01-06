# bOte
Dis_bot
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
