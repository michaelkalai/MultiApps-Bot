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

  # creates embed for use in message editing
  def emb(self, ques):
    embed = discord.Embed(color = 0xFF5733)
    embed.add_field(name = "Trivia", value = f"{self.user1}: {self.score1}\n{self.user2}: {self.score2}", inline = False)
    # displays a question and answer choices if a question has been selected
    if self.question:
      embed.add_field(name = self.current_topic, value = f"{ques[0]}\nA. {ques[1]}\nB. {ques[2]}\nC. {ques[3]}\nD. {ques[4]}", inline = False)
      embed.add_field(name = self.current_user, value = "Select an Answer", inline = False)
    else:
      embed.add_field(name = "Topics", value = f"{self.topics[0]}, {self.topics[1]}, {self.topics[2]}, {self.topics[3]}", inline = False)
    return embed
  
  @discord.ui.button(label = "1000", row = 0, style = discord.ButtonStyle.blurple)
  async def col_one_one_thousand(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if interaction.user == self.current_user and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][0][4]
      await interaction.response.edit_message(embed=self.emb(self.quest_ans[0][0]))
      button.disabled = True

  @discord.ui.button(label = "750", row = 1, style = discord.ButtonStyle.blurple)
  async def col_one_sevenfifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if interaction.user == self.current_user and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][1][4]
      await interaction.response.edit_message(embed=self.emb(self.quest_ans[0][1]))
      button.disabled = True

  @discord.ui.button(label = "500", row = 2, style = discord.ButtonStyle.blurple)
  async def col_one_five_hundred(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if interaction.user == self.current_user and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][2][4]
      await interaction.response.edit_message(embed=self.emb(self.quest_ans[0][2]))
      button.disabled = True

  @discord.ui.button(label = "250", row = 3, style = discord.ButtonStyle.blurple)
  async def col_one_twofifty(self, interaction: discord.Interaction, button: discord.ui.Button):
    # checks the user interacting with button
    # ensures no other question is already in progress
    if interaction.user == self.current_user and not self.question:
      self.question = True
      self.current_topic = self.topics[0]
      self.answer = self.quest_ans[0][3][4]
      await interaction.response.edit_message(embed=self.emb(self.quest_ans[0][3]))
      button.disabled = True