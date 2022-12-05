import random

@bot.command()
async def flipCoin(ctx):
    num = random.randint(0, 1)
    if num == 0:
        await ctx.send("Heads!")
    else:
        await ctx.send("Tails!")