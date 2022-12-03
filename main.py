# This code is based on the following example:
# https://discordpy.readthedocs.io/en/stable/quickstart.html#a-minimal-bot

import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    print(message)


client.run(
    "MTA0ODQyOTk3Mzg0MjcxMDU2OQ.GsvPCF.lJkEXWYh2sfM23dgYhnTjedwYrhZyII3Wx01Ks")

# except discord.HTTPException as e:
#     if e.status == 429:
#         print(
#             "The Discord servers denied the connection for making too many requests"
#         )
#         print(
#             "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-solve-the-error-for-toomanyrequests"
#         )
#     else:
#         raise e
#
#import discord
#from discord.ext import commands
#
#from apikeys import *
#
#client = commands.Bot(command_prefix - "$")
#
#@client.event
#async def on_ready():
#  print("The bot is now ready for use!")
#  print("------------------------------")
#
#@client.command
#  async def hello(ctx):
#    await ctx.send("Hello, I am the bot!")
#
#client.run(
#   "MTA0ODQyOTk3Mzg0MjcxMDU2OQ.GsvPCF.lJkEXWYh2sfM23dgYhnTjedwYrhZyII3Wx01Ks")
