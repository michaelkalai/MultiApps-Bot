import discord
from discord.ext import commands
import random
import pygame
import time
import datetime
import variables
from connect_four import Connect_Four


def run_bot():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='$', intents=intents)

    @bot.event
    async def on_ready():
        print(f"{bot.user} is online")

    @bot.command()
    async def hello(ctx):
        await ctx.send('Hello there!')
        print(ctx.author)

    @bot.command()
    async def connect4(ctx, *args):
        arg = ' '.join(args)
        def check_1(msg):
          return msg.author == connect.user1 and msg.channel == ctx.channel
        def check_2(msg):
          return str(msg.author) == connect.user2 and msg.channel == ctx.channel
        
        guild_id = ctx.guild.id
        server = bot.get_guild(guild_id)
        members = server.members
        user1 = ctx.author
        user2 = ''
        for member in members:
          if member.name in arg:
            user2 = member.name + '#' + member.discriminator
            break
        if len(user2) < 1:
          await ctx.send(f'{arg} not found')
          return
        
        connect = Connect_Four(ctx, user1, user2)
        player = connect.user1
        chip = 'x'
        embed = connect.display_board()
        await ctx.send(embed=embed)
        
        while True:
          con_it = True
          await ctx.send(f'{player}\'s turn')
          if player == connect.user1:
            msg = await bot.wait_for("message", check=check_1)
          elif player == connect.user2:
            msg = await bot.wait_for("message", check=check_2)
          else:
            continue
          col = msg.content
          try:
            if 0 < int(col) < 8:
              col = int(col)
              col -= 1
            else:
              con_it = False
          except:
            print('error')
            con_it = False
          if con_it == True:
            if connect.has_space(col):
              connect.insert_chip(chip, col)
            else:
              await ctx.send('Column full')
              continue
            embed = connect.display_board()
            await ctx.send(embed=embed)
            if connect.check_winner(chip):
              await ctx.send(f'{player} has won!')
              break
            elif connect.is_full():
              await ctx.send('Tie game!')
              break
            player = connect.user1 if player == connect.user2 else connect.user2
            chip = 'x' if chip == 'o' else 'o'

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
                    await ctx.send("You win! I chose " + comp_choice)
                if ans == "scissors":
                    await ctx.send("I win! I chose " + comp_choice)
            if comp_choice == "paper":
                if ans == "rock":
                    await ctx.send("I win! I chose " + comp_choice)
                if ans == "scissors":
                    await ctx.send("You win! I chose " + comp_choice)
            if comp_choice == "scissors":
                if ans == "paper":
                    await ctx.send("I win! I chose " + comp_choice)
                if ans == "rock":
                    await ctx.send("You win! I chose " + comp_choice)

    #Flag guesser
    @bot.command()
    async def Flag(ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        flags = [
            "au", "af", "ax", "ca", "aw", "vn", "al", "ky", "bj", "cf", "cn",
            "cx", "fo", "er", "us", "jp", "kr", "dk", "ic", "ge", "gl", "jm",
            "my", "xk", "fr", "nr", "no", "pw", "za", "lc", "tr", "bv", "mx",
            "br"
        ]
        emote = random.choice(flags)
        await ctx.send("What flag is this? Enter as a two letter abbreviation."
                       )
        await ctx.send(":flag_" + emote + ":")
        msg = await bot.wait_for("message", check=check)
        guess = msg.content
        if guess == emote:
            await ctx.send("Correct!")
        if guess != emote:
            await ctx.send("Incorrect! The correct abbreviation is ||" +
                           emote + "||")


#Random num gen

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

            #prints final results
            await ctx.send("Roll total with a " + str(rollMod) +
                           " modifier: " + str(finalNum) + "\n")
            await ctx.send("Your unmodified rolls: ")
            await ctx.send(str(rollList))

    #'''

    #Testing junk (iSpy)
    #comment the ''' below to turn on, uncomment to turn on
    '''
    @bot.event
    async def on_message(msg):
        #avoids infinite loop
        if msg.author == bot.user:
          return

        #gets message data
        username = str(msg.author)
        user_message = str(msg.content)
        channel = str(msg.channel)
        #assigns what channel the bot will send message to (i-spy ID is 1049110503236059186)
        tar_channel = bot.get_channel(1049110503236059186)
        #print(f"{username} said: {user_message} in {channel}")
        await tar_channel.send(f"{username} said: {user_message} in {channel}")

        #for guild in bot.guilds:
          #for text_ch in guild.text_channels:
            #print(text_ch.id)
        await bot.process_commands(msg)
    #'''
    #The bracket generator (currently version 1)
   
    # #Bracket generator
    @bot.command()
    async def genBracket(ctx, timer=60):

        #this is phase 1, where the bot will ask for input
        await ctx.send("Bracket created! React with :white_check_mark: to enter into the bracket!")
        #too lazy to convert to minutes hours and day
        await ctx.send("Entry will end in " + str(timer) + " seconds!")
        time.sleep(timer)
        
        #this is phase 2, where the bot will collect the inputs
        await ctx.send("Time's up, omar ugly as hell")

        def check(msg):
          print(msg)
        
    #     #async def on_message(msg):
    #       #print(msg)
    #       #print(msg.content)

        

    #  
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

    @bot.command()
    async def embed(ctx):
        embed = discord.Embed(title="Test",
                              url="",
                              description="No",
                              color=0xFF5733)
        embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://imgur.com/gallery/PJBNl")
        embed.add_field(name="Field 1 Test",
                        value="This is a testing field without inline." + "\n" + "bro",
                        inline=False)
        embed.add_field(name="Field 2 Test",
                        value="This is a testing field with inline.",
                        inline=True)
        embed.add_field(name="Field 2 Test",
                        value="This is a testing field with inline.",
                        inline=True)
        embed.set_footer(text="This is a footer for the embed.")
        await ctx.send(embed=embed)

    
    bot.run(variables.token)



