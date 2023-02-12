import os
import mysql.connector

token = os.environ['token']
sqltoken = os.environ['sqltoken']
ip = os.environ['ip']

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

def add_user(cursor, user_name, user_id):
    query = ('INSERT INTO Users (name, userid, money) VALUES ("' + user_name + '", "' + str(user_id) + '", 1000);')
    cursor.execute(query)

def connectsql():
    cnx = mysql.connector.connection.MySQLConnection(
                user='root',
                password=sqltoken,
                host=ip,
                database='Myriad')
    cursor = cnx.cursor()
    return cnx, cursor

def disconnectsql(cnx, cursor):
    cnx.commit()
    cursor.close()
    cnx.close()

def check_for_user(cursor, id):
    bool = False
    cursor.execute("SELECT userid FROM Users;")
    for userid in cursor:
      if userid[0] == str(id):
        bool = True
    return bool

def get_money(cursor, id):
    cursor.execute(f"SELECT money FROM Users where userid = {id};")
    for money in cursor:
      return money[0]