import discord
from discord.ext import commands
import math

class Trivia(discord.ui.View):
  def __init__(self, user1, user2, topics, quest_ans):
    super().__init__()
    self.user1 = user1
    self.user2 = user2
    self.score1 = "0"
    self.score2 = "0"
    self.current_user = user1
    self.question = False
    self.quest_ans = quest_ans
    self.current_topic = None
    self.topics = topics
    self.answer = None
    self.points = None
    self.wrong_answer = False
    self.answered = 0
    
  # creates embed for use in message editing
  def emb(self, ques):
    embed = discord.Embed(color = 0xFF5733)
    embed.add_field(name = "Trivia", value = f"{self.user1}: {self.score1}\n{self.user2}: {self.score2}", inline = False)
    # displays a question and answer choices if a question has been selected
    if self.question:
      embed.add_field(name = self.current_topic, value = f"{ques[0]}\nA. {ques[1]}\nB. {ques[2]}\nC. {ques[3]}\nD. {ques[4]}", inline = False)
      embed.add_field(name = self.current_user, value = "Select an Answer", inline = False)
    # displays winner if all questions have been answered
    elif self.answered == 16:
      if int(self.score1) > int(self.score2):
        embed.add_field(name = "Winner", value = self.user1)
      elif int(self.score1) < int(self.score2):
        embed.add_field(name = "Winner", value = self.user2)
      else:
        embed.add_field(name = "Winner", value = "Tie game")
    # tells user if their answer was correct and displays topics
    else:
      if self.wrong_answer:
        embed.add_field(name = "Last Question", value = "Incorrect", inline = False)
      else:
        embed.add_field(name = "Last Question", value = "Correct", inline = False)
      embed.add_field(name = "Topics", value = f"{self.topics[0]}, {self.topics[1]}, {self.topics[2]}, {self.topics[3]}", inline = False)
      embed.add_field(name = self.current_user, value = "Select a Question", inline = False)
    return embed

  # checks the current user and adds points to their score
  def add_points(self):
    if self.current_user == self.user1:
      self.score1 = str(int(self.score1) + self.points)
    else:
      self.score2 = str(int(self.score2) + self.points)
  
  @discord.ui.button(label = "1000", row = 0, style = discord.ButtonStyle.blurple)
  async def col_one_one_thousand(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][0][5]
      self.points = 1000
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[0][0]), message_id=interaction.message.id)

  @discord.ui.button(label = "750", row = 1, style = discord.ButtonStyle.blurple)
  async def col_one_sevenfifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][1][5]
      self.points = 750
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[0][1]), message_id=interaction.message.id)

  @discord.ui.button(label = "500", row = 2, style = discord.ButtonStyle.blurple)
  async def col_one_five_hundred(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][2][5]
      self.points = 500
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[0][2]), message_id=interaction.message.id)

  @discord.ui.button(label = "250", row = 3, style = discord.ButtonStyle.blurple)
  async def col_one_twofifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][3][5]
      self.points = 250
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[0][3]), message_id=interaction.message.id)

  @discord.ui.button(label = "1000", row = 0, style = discord.ButtonStyle.blurple)
  async def col_two_one_thousand(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[1]
      self.answer = self.quest_ans[1][0][5]
      self.points = 1000
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[1][0]), message_id=interaction.message.id)

  @discord.ui.button(label = "750", row = 1, style = discord.ButtonStyle.blurple)
  async def col_two_sevenfifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[1]
      self.answer = self.quest_ans[1][1][5]
      self.points = 750
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[1][1]), message_id=interaction.message.id)

  @discord.ui.button(label = "500", row = 2, style = discord.ButtonStyle.blurple)
  async def col_two_five_hundred(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[1]
      self.answer = self.quest_ans[1][2][5]
      self.points = 500
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[1][2]), message_id=interaction.message.id)

  @discord.ui.button(label = "250", row = 3, style = discord.ButtonStyle.blurple)
  async def col_two_twofifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[1]
      self.answer = self.quest_ans[1][3][5]
      self.points = 250
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[1][3]), message_id=interaction.message.id)

  @discord.ui.button(label = "1000", row = 0, style = discord.ButtonStyle.blurple)
  async def col_three_one_thousand(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[2]
      self.answer = self.quest_ans[2][0][5]
      self.points = 1000
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[2][0]), message_id=interaction.message.id)

  @discord.ui.button(label = "750", row = 1, style = discord.ButtonStyle.blurple)
  async def col_three_sevenfifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[2]
      self.answer = self.quest_ans[2][1][5]
      self.points = 750
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[2][1]), message_id=interaction.message.id)

  @discord.ui.button(label = "500", row = 2, style = discord.ButtonStyle.blurple)
  async def col_three_five_hundred(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[2]
      self.answer = self.quest_ans[2][2][5]
      self.points = 500
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[2][2]), message_id=interaction.message.id)

  @discord.ui.button(label = "250", row = 3, style = discord.ButtonStyle.blurple)
  async def col_three_twofifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[2]
      self.answer = self.quest_ans[2][3][5]
      self.points = 250
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[2][3]), message_id=interaction.message.id)

  @discord.ui.button(label = "1000", row = 0, style = discord.ButtonStyle.blurple)
  async def col_four_one_thousand(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[3]
      self.answer = self.quest_ans[3][0][5]
      self.points = 1000
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[3][0]), message_id=interaction.message.id)

  @discord.ui.button(label = "750", row = 1, style = discord.ButtonStyle.blurple)
  async def col_four_sevenfifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[3]
      self.answer = self.quest_ans[3][1][5]
      self.points = 750
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[3][1]), message_id=interaction.message.id)

  @discord.ui.button(label = "500", row = 2, style = discord.ButtonStyle.blurple)
  async def col_four_five_hundred(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[3]
      self.answer = self.quest_ans[3][2][5]
      self.points = 500
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[3][2]), message_id=interaction.message.id)

  @discord.ui.button(label = "250", row = 3, style = discord.ButtonStyle.blurple)
  async def col_four_twofifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and not self.question:
      self.question = True
      self.current_topic = self.topics[3]
      self.answer = self.quest_ans[3][3][5]
      self.points = 250
      button.disabled = True
      await interaction.response.edit_message(view=self)
      await interaction.followup.edit_message(embed=self.emb(self.quest_ans[3][3]), message_id=interaction.message.id)
      
  @discord.ui.button(label = "A", row = 4, style = discord.ButtonStyle.blurple)
  async def a(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and self.question:
      self.question = False
      if self.answer == "A":
        self.add_points()
      else:
        self.wrong_answer = True
      self.answered += 1
      await interaction.response.edit_message(embed=self.emb([]))
      self.wrong_answer = False
      self.current_user = self.user2 if self.current_user == self.user1 else self.user1

  @discord.ui.button(label = "B", row = 4, style = discord.ButtonStyle.blurple)
  async def b(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and self.question:
      self.question = False
      if self.answer == "B":
        self.add_points()
      else:
        self.wrong_answer = True
      self.answered += 1
      await interaction.response.edit_message(embed=self.emb([]))
      self.wrong_answer = False
      self.current_user = self.user2 if self.current_user == self.user1 else self.user1

  @discord.ui.button(label = "C", row = 4, style = discord.ButtonStyle.blurple)
  async def c(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and self.question:
      self.question = False
      if self.answer == "C":
        self.add_points()
      else:
        self.wrong_answer = True
      self.answered += 1
      await interaction.response.edit_message(embed=self.emb([]))
      self.wrong_answer = False
      self.current_user = self.user2 if self.current_user == self.user1 else self.user1

  @discord.ui.button(label = "D", row = 4, style = discord.ButtonStyle.blurple)
  async def d(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if str(interaction.user) == str(self.current_user) and self.question:
      self.question = False
      if self.answer == "D":
        self.add_points()
      else:
        self.wrong_answer = True
      self.answered += 1
      await interaction.response.edit_message(embed=self.emb([]))
      self.wrong_answer = False
      self.current_user = self.user2 if self.current_user == self.user1 else self.user1