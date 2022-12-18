import discord
from discord.ext import commands
import random

class Calculator(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value1 = "0"
    self.value2 = ""
    self.operation = ""
    self.selected = ""

  def emb(self):
    embed = discord.Embed(color = 0xFF5733)
    embed.add_field(name = "Calculator", value = F"{self.value1} {self.operation} {self.value2}")
    return embed

  def change_val(self):
    if self.selected.isdigit:
      if self.value1 == "0":
        self.value1 = self.selected
      elif self.operation == "":
        self.value1 += self.selected
      else:
        self.value2 += self.selected
    else:
      self.operation = self.selected
  
  @discord.ui.button(label = "C", row = 0, style = discord.ButtonStyle.blurple)
  async def clear(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.value1 = "0"
    self.value2 = ""
    self.operation = ""
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "1", row = 1, style = discord.ButtonStyle.blurple)
  async def one(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "1"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "2", row = 1, style = discord.ButtonStyle.blurple)
  async def two(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "2"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)