# bOte
Dis_bot
@bot.event
async def on_member_join(member):
  channel = bot.get_channel()
  await channel.send(f'{member}join!')

async def on_member_remove(member):
  channel = bot.get_channel()
  await channel.send(f'{member}leave!')
 
