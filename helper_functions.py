def get_player(bot, args, ctx):
  arg = ''.join(args).lower()
  if '@' in arg:
      arg = arg[2:-1]
  server = bot.get_guild(ctx.guild.id)
  members = server.members
  player = None
  
  # searches for challenged player in list of server members
  for member in members:
      if arg in member.name.lower():
          player = member.name + '#' + member.discriminator
          playerid = member.id
      elif arg == str(member.id):
          player = member.name + '#' + member.discriminator
          playerid = member.id
  return player, playerid