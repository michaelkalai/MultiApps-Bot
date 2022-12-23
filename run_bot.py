import discord
from discord.ext import commands
import random
import pygame
import time
import datetime
import variables
from connect_four import Connect_Four
from button import Menu
from calculator import Calculator


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
        arg = ' '.join(args).lower()
        if '@' in arg:
            arg = arg[2:-1]

        def check_1(msg):
            return msg.author == connect.user1 and msg.channel == ctx.channel

        def check_2(msg):
            return str(
                msg.author) == connect.user2 and msg.channel == ctx.channel

        con = True
        guild_id = ctx.guild.id
        server = bot.get_guild(guild_id)
        members = server.members
        user1 = ctx.author
        user1_id = str(ctx.author.id)
        user2 = ''
        for member in members:
            # print(arg)
            # print(member.id)
            if arg in member.name.lower():
                user2 = member.name + '#' + member.discriminator
                user2_id = str(member.id)
                break
            elif arg == str(member.id):
                user2 = member.name + '#' + member.discriminator
                user2_id = str(member.id)
                break
        if len(user2) < 1:
            await ctx.send(f'{arg} not found')
            return

        connect = Connect_Four(ctx, user1, user2, user1_id, user2_id)
        player = connect.user1
        chip = 'x'
        embed = connect.display_board(player)
        await ctx.send(embed=embed)
        # await ctx.send(f'{player}\'s turn')
        # await ctx.send('Type concede to surrender')

        while con == True:
            con_it = True
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
                    await ctx.send('Please enter an integer between 1 and 7')
                    con_it = False
            except:
                if 'concede' in col:
                    id = connect.user1_id if player == connect.user1 else connect.user2_id
                    await ctx.send(f'<@{id}> surrendered! :pensive:')
                    player = connect.user1 if player == connect.user2 else connect.user2
                    await ctx.send(f'<@{id}> has won! :tada:')
                    con = False
                else:
                    print('error')
                con_it = False
            if con_it == True:
                if connect.has_space(col):
                    connect.insert_chip(chip, col)
                else:
                    await ctx.send('Column full')
                    continue
                embed = connect.display_board(player)
                await ctx.send(embed=embed)
                if connect.check_winner(chip):
                    id = connect.user1_id if player == connect.user1 else connect.user2_id
                    await ctx.send(f'<@{id}> has won! :tada:')
                    break
                elif connect.is_full():
                    await ctx.send('Tie game!')
                    break
                player = connect.user1 if player == connect.user2 else connect.user2
                chip = 'x' if chip == 'o' else 'o'
                # await ctx.send(f'{player}\'s turn')

    @bot.command()
    async def spin(ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        items = []
        x = False
        while True:
            embed = discord.Embed(
                title="Spin the Wheel",
                url="",
                description=
                "Type something to add it to the wheel \nType \"remove (item number)\" to remove an item \nType \"done\" to finalize wheel selections \nType \"cancel\" to cancel",
                color=0xFF5733)
            if len(items) > 0:
                string = ""
                for item in items:
                    string += str(items.index(item) + 1)
                    string += ". "
                    string += item
                    string += " \n "
                embed.add_field(name="Current Items:", value=string)
            await ctx.send(embed=embed)
            msg = await bot.wait_for("message", check=check)
            if check(msg):
                if 'done' in msg.content:
                    break
                elif 'cancel' in msg.content:
                    x = True
                    break
                elif 'remove' in msg.content:
                    try:
                        removal = msg.content.split(" ")
                        ind = int(removal[1]) - 1
                        items.pop(ind)
                    except:
                        pass
                else:
                    if msg.content in items:
                        await ctx.send("Item already added")
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
    #'''
    @bot.event
    async def on_message(msg):
        # print(msg)
        #avoids infinite loop
        if msg.author == bot.user:
            return

        #sets logging mode. 0 = off, 1 = repeat (wiretap), 2 = basic, 3 = meta, anything else gives debug
        log_mode = 0
        if log_mode == 0:
            pass
        elif log_mode == 1:
            tar_channel = bot.get_channel(1049110503236059186)
            await tar_channel.send(str(msg.content))
        elif log_mode == 2:
            #gets basic message data
            username = str(msg.author)
            user_message = str(msg.content)
            channel = str(msg.channel)
            #gets the UTC time and converts it to EST
            timestamp = datetime.datetime.now(
                datetime.timezone(datetime.timedelta(hours=19)))
            #converts the formatting so that it looks nicer
            pretty_time = timestamp.strftime(r"%I:%M %p")

            #assigns what channel the bot will send message to (i-spy ID is 1049110503236059186)
            tar_channel = bot.get_channel(1049110503236059186)
            #print(f"{username} said: {user_message} in {channel}") #This is to print to console
            await tar_channel.send(
                f"{username} said: {user_message} in {channel} at {pretty_time} EST"
            )
            #await tar_channel.send(f"{pretty_time}") #sends only the time

        elif log_mode == 3:
            #pass
            print(msg)  #prints raw metadata to console
            #data collection
            msg_id = msg.id
            ch_name = msg.channel
            ch_id = msg.channel.id
            user = msg.author
            user_id = msg.author.id
            user_message = msg.content

            tar_channel = bot.get_channel(1049110503236059186)
            await tar_channel.send(
                f"Message ID: {msg_id} \nChannel name: {ch_name} \nChannel ID: {ch_id}\nAuthor: {user} \nAuthor ID: {user_id}\nContent: {user_message} \n"
            )
            #await tar_channel.send(f"{}")
        else:
            print("No valid log_mode set for ISpy")

        #this makes it so it doesn't stop processing commands due to logging
        await bot.process_commands(msg)

    #'''
    #The bracket generator (currently version 1)

    # #Bracket generator
    '''
    @bot.command()
    async def genBracket(ctx, timer=60):

        #this is phase 1, where the bot will ask for input
        await ctx.send("Bracket created! React with :white_check_mark: to enter into the bracket!")
        #too lazy to convert to minutes hours and day
        await ctx.send("Entry will end in " + str(timer) + " seconds!")

        for x in range(timer):
          def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
          try:
            msg = await bot.wait_for("message", check=check, timeout=1)
            if msg.content == "Cancel":
              await ctx.send("yo stank ahh canceled")
              return
          except:
            pass
          #time.sleep(1)
        #
        #
        #
        #this is phase 2, where the bot will collect the inputs
        await ctx.send("Time's up, omar ugly as hell")
        
        #print(msg.content)
        
        
        

    #'''
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
    async def helpBot(ctx):
        embed = discord.Embed(title="Multi-App Bot Help",
                              url="",
                              description="",
                              color=0xFF5733)
        embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
        embed.set_thumbnail(url="https://imgur.com/gallery/PJBNl")
        embed.add_field(
            name="Commands",
            value=
            "$vcPicker <Channel Name> - Randomly picks someone from the specified voice channel.\n\n"
            +
            "$get_channel <Channel Name> - Returns the ID of the respective channel.\n\n"
            +
            "$rollDice <maxNum, rollAmt=1, rollMod=0> - Rolls a dice with the specified parameters.",
            inline=False)
        embed.set_footer(text="This is a footer for the embed.")
        await ctx.send(embed=embed)

    @bot.command()
    async def menu(ctx):
      view = Menu()
      await ctx.reply(view=view)

    @bot.command()
    async def calc(ctx):
      view = Calculator()
      await ctx.reply(view=view)
        
    # Jordan's random gym tips
    @bot.command()
    async def gymtips(ctx):
      num = random.randint(0, len(variables.gymtip) - 1)
      await ctx.send(variables.gymtip[num])
  
    bot.run(variables.token)
