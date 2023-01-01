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
from hangman import Hangman
from barber_finder import Barber_Finder
from command_list import comml
from trivia import Trivia
import trivia_variables

def run_bot():
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix='$', intents=intents)
    # Barber_Finder.echo()

    @bot.event
    async def on_ready():
        print(f"{bot.user} is online")

    @bot.command()
    async def hello(ctx):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.author.dm_channel

        await ctx.send('Hello there!')
        await ctx.author.send('Bro')
        msg = await bot.wait_for('message', check=check)
        print(msg.content)
        print(ctx.author)

    @bot.command()
    async def connect4(ctx, *args):
        # changes arg into an id if '@' was used
        arg = ' '.join(args).lower()
        if '@' in arg:
            arg = arg[2:-1]

        def check_1(msg):
            return msg.author == connect.user1 and msg.channel == ctx.channel

        def check_2(msg):
            return str(
                msg.author) == connect.user2 and msg.channel == ctx.channel

        # seraches through server member list and gets both players
        con = True
        guild_id = ctx.guild.id
        server = bot.get_guild(guild_id)
        members = server.members
        user1 = ctx.author
        user1_id = str(ctx.author.id)
        user2 = ''
        for member in members:
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

        # initializes game
        connect = Connect_Four(ctx, user1, user2, user1_id, user2_id)
        player = connect.user1
        chip = 'x'
        embed = connect.display_board(player)
        await ctx.send(embed=embed)

        while con == True:
            con_it = True
            if player == connect.user1:
                msg = await bot.wait_for("message",
                                         check=check_1,
                                         timeout=86400)
            elif player == connect.user2:
                msg = await bot.wait_for("message",
                                         check=check_2,
                                         timeout=86400)
            else:
                continue
            col = msg.content
            # determines column based or concession based on user input
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
            # checks for space in column and inserts chip before displaying board
            if con_it == True:
                if connect.has_space(col):
                    connect.insert_chip(chip, col)
                else:
                    await ctx.send('Column full')
                    continue
                embed = connect.display_board(player)
                await ctx.send(embed=embed)
                # checks for winner
                if connect.check_winner(chip):
                    id = connect.user1_id if player == connect.user1 else connect.user2_id
                    await ctx.send(f'<@{id}> has won! :tada:')
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
    async def commandlist(ctx):
      embed = discord.Embed(title="Myriad Command List",
                              url="",
                              description="",
                              color=0xFF5733)
      embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
      embed.add_field(
            name ="Command Categories:",
            value =
            "Games\n" + "" + "Math\n" + "Gym\n" + "VC Commands\n" + "Tools\n" + "Other\n" + "All Commands"
        )
      embed.set_footer(text="This is a footer for the embed.")
      await ctx.send(embed=embed)

      await ctx.send("Please select one of the categories listed above:")
      def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel
      while True:
        msg = await bot.wait_for("message", check=check)
        if msg.content == "Games":
          c = 0
          break
        if msg.content == "Math":
          c = 1
          break
        if msg.content == "Gym":
          c = 2
          break
        if msg.content == "VC Commands":
          c = 3
          break
        if msg.content == "Tools":
          c = 4
          break
        if msg.content == "Other":
          c = 5
          break
        if msg.content == "All Commands":
          c = 6
          break

      while True:
        if c == 0:
          embed = discord.Embed(title="Myriad: Games",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Commands:",
              value=comml[0],
              inline=False)
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break
        if c == 1:
          embed = discord.Embed(title="Myriad: Math",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Commands:",
              value=comml[1],
              inline=False)
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break
        if c == 2:
          embed = discord.Embed(title="Myriad: Gym",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Commands:",
              value=comml[2],
              inline=False)
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break
        if c == 3:
          embed = discord.Embed(title="Myriad: VC Commands",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Commands:",
              value=comml[3],
              inline=False)
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break
        if c == 4:
          embed = discord.Embed(title="Myriad: Tools",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Commands:",
              value=comml[4],
                inline=False)
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break
        if c == 5:
          embed = discord.Embed(title="Myriad: Other",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Commands:",
              value=comml[5],
                inline=False)
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break
        if c == 6:
          embed = discord.Embed(title="Myriad: All Commands",
                              url="",
                              description="",
                              color=0xFF5733)
          embed.set_author(name=ctx.author.display_name,
                         url="https://realdrewdata.medium.com/",
                         icon_url=ctx.author.avatar.url)
          embed.add_field(
              name="Games:",
              value=comml[0],
                inline=False)
          embed.add_field(
              name="Math:",
              value=comml[1],
                inline=False)
          embed.add_field(
              name="Gym:",
              value=comml[2],
                inline=False)
          embed.add_field(
              name="VC Commands:",
              value=comml[3],
                inline=False)
          embed.add_field(
              name="Tools:",
              value=comml[4],
                inline=False)
          embed.add_field(
              name="Other:",
              value=comml[5],
                inline=False)
          
          embed.set_footer(text="This is a footer for the embed.")
          await ctx.send(embed=embed)
          break

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
    async def gymtip(ctx):
        num = random.randint(0, len(variables.gymtips) - 1)
        await ctx.send(variables.gymtips[num])


# Jordan's protein intake calculator

    @bot.command()
    async def protein(ctx):
        await ctx.send("Please type in M or F if you're male or female:")
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel
        while True:
          msg = await bot.wait_for("message", check=check)
          g = msg. content
          if g == "M":
            proteindec = 0.75
            break
          if g == "m":
            proteindec = 0.75
            break
          if g == "F":
            proteindec = 0.83
            break
          if g == "f":
            proteindec = 0.83
            break
        
        await ctx.send("Please type in your body weight:")
        while True:
          msg = await bot.wait_for("message", check=check)
          body_weight = msg.content
  
          if float(body_weight) < 0:
              await ctx.send(
                  "Negatives numbers aren't applicable, please type in your body weight:"
              )
  
          elif float(body_weight) > 0:
            bodyweight = float(body_weight) * proteindec
            await ctx.send(
                f"Your daily intake should be {round(bodyweight)} grams of protein for muscle building")
            break

    @bot.command()
    async def hangman(ctx, args):
        def check(msg):
            return msg.author == ctx.author and msg.channel == ctx.author.dm_channel

        def check_player(msg):
            return str(
                msg.author
            ) == hangman.player and msg.channel == ctx.channel and len(
                msg.content) < 2 and msg.content.isalpha(
                ) and msg.content.lower() not in hangman.used_letters

        # Determines the player in the server being challenged to the game
        arg = ''.join(args).lower()
        if '@' in arg:
            arg = arg[2:-1]
        server = bot.get_guild(ctx.guild.id)
        members = server.members
        player = None
        for member in members:
            if arg in member.name.lower():
                player = member.name + '#' + member.discriminator
                playerid = member.id
            elif arg == str(member.id):
                player = member.name + '#' + member.discriminator
                playerid = member.id
        if player == None:
            return

        # Sends a dm to the command initiator to get the word for the game
        await ctx.author.send("Type your word or phrase here")
        while True:
            con = False
            msg = await bot.wait_for("message", check=check, timeout=30)
            word = msg.content
            if len(msg.content) > 40:
                await ctx.author.send(
                    "Words/phrases are limited to 40 characters")
            for chr in word:
                if not chr.isalpha() and not chr == " ":
                    con = True
            if not con:
                break
            else:
                await ctx.author.send("Please only use letters and spaces")
        await ctx.send(
            f"<@{ctx.author.id}> has challenged <@{playerid}> to hangman")

        # initiates hangman game and prompts for user input
        hangman = Hangman(word, player)
        hangman.setup_display()
        while True:
            await ctx.send(embed=hangman.embed())
            await ctx.send("type in your guess")
            msg = await bot.wait_for("message",
                                     check=check_player,
                                     timeout=86400)
            guess = msg.content.lower()
            if not hangman.check_letter(guess):
                hangman.lives -= 1
            elif hangman.check_completion():
                await ctx.send(embed=hangman.embed())
                await ctx.send(
                    f"Congratulations <@{playerid}>, You completed the word!")
                break
            if hangman.lives < 1:
                await ctx.send(
                    f"Out of lives! The correct word/phrase was \"{word}\"")
                break
        

              
    @bot.command()
    async def trivia(ctx, *args):
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
          elif arg == str(member.id):
              player = member.name + '#' + member.discriminator
      if player == None:
          return
        
      # gathers topics and associated questions to be used in game
      nums = []
      for _ in range(4):
        num = random.randint(0, len(trivia_variables.topics) - 1)
        while num in nums:
          num = random.randint(0, len(trivia_variables.topics) - 1)
        nums.append(num)
      topics = []
      ques_ans = []
      for sel in nums:
        topics.append(trivia_variables.topics[sel])
      for topic in topics:
        ques_ans.append(trivia_variables.ques_ans[topic])

      # displays buttons and embed text to discord
      view = Trivia(ctx.author, player, topics, ques_ans)
      await ctx.send(f"Topics are {topics[0]}, {topics[1]}, {topics[2]}, and {topics[3]}. {ctx.author} select your first question to begin.")
      await ctx.reply(view=view)

    bot.run(variables.token)
