def get_player(bot, args, ctx):
  player = None
  playerid = None
  arg = ''.join(args).lower()
  if len(arg) < 1:
    return player, playerid
  if '@' in arg:
      arg = arg[2:-1]
  server = bot.get_guild(ctx.guild.id)
  members = server.members
  
  
  # searches for challenged player in list of server members
  for member in members:
      if arg in member.name.lower():
          player = member.name + '#' + member.discriminator
          playerid = member.id
      elif arg == str(member.id):
          player = member.name + '#' + member.discriminator
          playerid = member.id
  return player, playerid

def add_user():
  return ("INSERT INTO Users "
         "(name, id, money)"
         "VALUES (%s, %d, %f)")