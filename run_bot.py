import discord
from discord.ext import commands
import random

def run_bot():
  intents = discord.Intents.all()
  # intents.message_content = True
  bot = commands.Bot(command_prefix='$', intents=intents)
  # client = discord.Client(intents=discord.Intents.default())
  
  
  @bot.event
  async def on_ready():
      print(f"{bot.user} is online")
  
  @bot.command()
  async def hello(ctx):
    await ctx.send('Hello there!')

    
  @bot.command()
  async def RandomNum(ctx, arg1, arg2):
    arg1 =  int(arg1)
    arg2 = int(arg2)
    nums = random.randint(arg1 ,arg2)
    await ctx.send(nums)

  
  @bot.command()
  async def flipCoin(ctx):
      num = random.randint(0,1)
      if num == 0:
        await ctx.send("Heads!")
      else:
        await ctx.send ("Tails!")
    '''
  @bot.command()
  async def rollDice(ctx, maxNum, )
    '''
  bot.run(
      "MTA0ODQyOTk3Mzg0MjcxMDU2OQ.GsvPCF.lJkEXWYh2sfM23dgYhnTjedwYrhZyII3Wx01Ks")
