@bot.command('join')
async def on_join_community(ctx: Context):
  msg = ctx.msg.content
  comu = re.search("http://aminoapps.com/c/", msg)
  cmd = ' '.join(ctx.msg.content.split()[1:])
  
  if comu:
      ide = await ctx.get_info_link(cmd)
      idlink = ide.community.ndcId
      with ctx.set_ndc(idlink):
        await ctx.join_community(https://aminoapps.com/c/anime-es/page/chat-thread/el-rincon-de-cebollin-anime/Z6xT_DsgMJBvJRZGY3G8JVVXkB80WEv)
      await ctx.reply('Me he unido. :3')
