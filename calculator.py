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
    self.type = "deg"

  def emb(self):
    embed = discord.Embed(color = 0xFF5733)
    embed.add_field(name = "Calculator", value = F"{self.value1} {self.operation} {self.value2}")
    return embed

  def change_val(self):
    if self.selected.isdigit():
      if self.value1 == "0":
        self.value1 = self.selected
      elif self.operation == "":
        self.value1 += self.selected
      else:
        self.value2 += self.selected
    elif self.selected == ".":
      if self.operation == "" and "." not in self.value1:
        self.value1 += "."
      elif len(self.value2) > 0 and "." not in self.value2:
        self.value2 += "."
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

  @discord.ui.button(label = "3", row = 1, style = discord.ButtonStyle.blurple)
  async def three(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "3"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "4", row = 2, style = discord.ButtonStyle.blurple)
  async def four(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "4"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "5", row = 2, style = discord.ButtonStyle.blurple)
  async def five(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "5"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "6", row = 2, style = discord.ButtonStyle.blurple)
  async def six(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "6"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "7", row = 3, style = discord.ButtonStyle.blurple)
  async def seven(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "7"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "8", row = 3, style = discord.ButtonStyle.blurple)
  async def eight(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "8"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "9", row = 3, style = discord.ButtonStyle.blurple)
  async def nine(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "9"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "-/+", row = 0, style = discord.ButtonStyle.blurple)
  async def neg_pos(self, interaction: discord.Interaction, button: discord.ui.Button):
    if self.operation == "":
      if float(self.value1) > 0 or float(self.value1) < 0:
        if "-" in self.value1:
          self.value1 = self.value1[1:]
        else:
          self.value1 = "-" + self.value1
    elif len(self.value2) > 0:
      if float(self.value2) > 0 or float(self.value2) < 0:
        if "-" in self.value1:
          self.value2 = self.value2[1:]
        else:
          self.value2 = "-" + self.value2
    else:
      return
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = ".", row = 4, style = discord.ButtonStyle.blurple)
  async def dec(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "."
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "0", row = 4, style = discord.ButtonStyle.blurple)
  async def zero(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "0"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "dg/rd", row = 0, style = discord.ButtonStyle.red)
  async def deg_rad(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.type = "deg" if self.type == "rad" else "rad"