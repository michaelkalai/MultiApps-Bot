import discord
from discord.ext import commands
import random
import time


def run_bot():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is online")

    # @bot.event
    # async def on_message(message):
    #     if message.author != bot.user:
    #         objects.append(message)
    #         print(message.content)
    #     # elif message.author in objects:
    #     #     objects[message.author].append(message)
    #     if message.content == "hello":
    #         await message.channel.send(
    #             "pies are better than cakes. change my mind.")
    #     await bot.process_commands(message)
    #     print(message.author)

    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello there!')
        print(ctx.author)

    @bot.command()
    async def spin(ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        items = []
        x = False
        while True:
            await ctx.send('Add item to wheel')
            msg = await bot.wait_for("message", check=check)
            if check(msg):
                if 'done' in msg.content:
                    break
                elif 'cancel' in msg.content:
                    x = True
                else:
                    items.append(msg.content)
        if x:
            await ctx.send('Spin cancelled')
        else:
            selection = random.randint(0, len(items) - 1)
            await ctx.send('Spinning...')
            time.sleep(2)
            await ctx.send(f"{items[selection]}!")

    #Rock paper scissors
    @bot.command()
    async def RPS(ctx, msg):
        ans = msg.lower()
        choices = ["rock", "paper", "scissors"]
        comp_choice = random.choice(choices)
        if ans not in choices:
            await ctx.send("Choose a valid option: rock, paper, scissors")
            return
        else:
            if comp_choice == msg:
                await ctx.send("Tie!")
            if comp_choice == "rock":
                if ans == "paper":
                    await ctx.send("You win!")
                if ans == "scissors":
                    await ctx.send("I win!")
            if comp_choice == "paper":
                if ans == "rock":
                    await ctx.send("I win!")
                if ans == "scissors":
                    await ctx.send("You win!")
            if comp_choice == "scissors":
                if ans == "paper":
                    await ctx.send("I win!")
                if ans == "rock":
                    await ctx.send("You win!")

    @bot.command()
    async def RandomNum(ctx):
        await ctx.send("Please type the Minimum Number")

        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        msg = await bot.wait_for("message", check=check)
        arg_1 = msg.content

        await ctx.send("Please type the Maximum Number")
        msg = await bot.wait_for("message", check=check)
        arg_2 = msg.content

        nums = random.randint(int(arg_1), int(arg_2))
        await ctx.send("Your random number is: " + str(nums))

    #Command to flip a coin
    @bot.command()
    async def flipCoin(ctx):
        num = random.randint(0, 1)
        if num == 0:
            await ctx.send("Heads!")
        else:
            await ctx.send("Tails!")

    #command to roll dice
    #'''
    @bot.command()
    async def rollDice(ctx, maxNum, rollAmt=1, rollMod=0):
        #Checks if maxNum is valid (above 1)
        if int(maxNum) < 1:
            await ctx.send("Dice must have at least 2 sides")
            return
        #splits the command into 3 modes, no roll, single roll, and multi-roll
        if int(rollAmt) < 1:
            await ctx.send(
                "you rolled nothing dumbass (rolled amount set to >1)")
        elif rollAmt == 1:
            rolledNum = random.randint(1, int(maxNum))

            await ctx.send("you rolled a " + rolledNum + " from a " + maxNum +
                           " sided die!")
            if rollMod != 0:
                finalNum = rolledNum + int(rollMod)
                await ctx.send("With modifiers, you rolled a " + str(finalNum))
        else:
            rolledNum = random.randint(1, int(maxNum))
            finalNum = rolledNum
            rollList = [rolledNum]
            for x in range(int(rollAmt) - 1):
                roll = random.randint(1, int(maxNum)) + int(rollMod)
                if roll > 0:
                    finalNum = finalNum + roll
                    rollList.append(roll)
                else:
                    rollList.append(0)

            #this is not it
            #finalNum = (rolledNum * rollAmt) + rollMod
            await ctx.send("Roll total with a " + str(rollMod) +
                           " modifier: " + str(finalNum) + "\n")
            await ctx.send("Your unmodified rolls: ")
            await ctx.send(str(rollList))
            #await ctx.send(str(finalNum))

    #'''

    #VC Person Picker
    @bot.command()
    async def vcPicker(ctx, *, given_name=None):
        for channel in ctx.guild.channels:
            if channel.name == given_name:
                wanted_channel_id = channel.id

        # Loops Names in Channel
        voice_channel = bot.get_channel(wanted_channel_id)
        member_ids = list(voice_channel.voice_states.keys())

        # Chooses Random Name
        vcPicked = random.choice(member_ids)
      
        # Prints Name to Chat
        await ctx.send("You have bee selected from: " + given_name + "! " +
                       "<@" + str(vcPicked) + ">")

    @bot.command()
    async def get_channel(ctx, *, given_name=None):
        for channel in ctx.guild.channels:
            if channel.name == given_name:
                wanted_channel_id = channel.id

        await ctx.send(wanted_channel_id)

    bot.run(
        "MTA0ODQyOTk3Mzg0MjcxMDU2OQ.GsvPCF.lJkEXWYh2sfM23dgYhnTjedwYrhZyII3Wx01Ks"
    )
