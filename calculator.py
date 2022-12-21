import discord
from discord.ext import commands
import math

class Calculator(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value1 = "0"
    self.value2 = ""
    self.operation = ""
    self.selected = ""
    self.type = "deg"
    self.answer = "0"

  def emb(self):
    dg_rd = "ᵈᵉᵍ" if self.type == "deg" else "ʳᵃᵈ"
    embed = discord.Embed(color = 0xFF5733)
    embed.add_field(name = "Calculator", value = F"{dg_rd}\n{self.value1} {self.operation} {self.value2}")
    return embed

  def change_val(self):
    if self.selected == "π":
      if self.operation == "" and "π" not in self.value1 and self.value1[-1] != ".":
        if self.value1 != "0":
          self.value1 += self.selected
        else:
          self.value1 = self.selected
      elif self.operation != "" and "π" not in self.value2 and self.value2[-1] != ".":
        self.value2 += self.selected
    elif self.selected.isdigit():
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
    elif self.selected == self.answer:
      if self.operation == "":
        self.value1 = self.selected
      else:
        self.value2 = self.selected
    else:
      self.operation = self.selected

  def pi_con(self, value):
    if self.type == "deg":
      if "π" in self.value1 and len(self.value1) > 1:
        new_value = math.radians(self.value1[:-1] * math.pi)
      elif "π" in self.value1:
        new_value = math.radians(math.pi)
      else:
        new_value = math.radians(float(self.value1))
    else:
      if "π" in self.value1 and len(self.value1) > 1:
        new_value = float(self.value1[:-1]) * math.pi
      elif "π" in self.value1:
        new_value = math.pi
      else:
        new_value = float(self.value1)
    return new_value

  def cor_sign(self):
    if float(self.answer) == 0 and "-" in self.answer:
      self.answer = self.answer[1:]

  def call_error(self):
    self.value1 = "Error"
    self.value2 = ""
    self.operation = ""
  
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
        if "-" in self.value2:
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
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "+", row = 0, style = discord.ButtonStyle.green)
  async def plus(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "+"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "-", row = 1, style = discord.ButtonStyle.green)
  async def minus(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "-"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "X", row = 2, style = discord.ButtonStyle.green)
  async def mult(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "X"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)
    
  @discord.ui.button(label = "/", row = 3, style = discord.ButtonStyle.green)
  async def div(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "/"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "ans", row = 4, style = discord.ButtonStyle.blurple)
  async def ans(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = self.answer
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "=", row = 4, style = discord.ButtonStyle.green)
  async def equal(self, interaction: discord.Interaction, button: discord.ui.Button):
    try:
      if "π" in self.value1:
        value1 = float(self.value1[:-1]) * math.pi
      else:
        value1 = float(self.value1)
      if "π" in self.value2:
        value2 = float(self.value2[:-1]) * math.pi
      else:
        value2 = float(self.value2)
      if self.operation == "+":
        self.answer = value1 + value2
      elif self.operation == "-":
        self.answer = value1 - value2
      elif self.operation == "X":
        self.answer = value1 * value2
      elif self.operation == "/":
        self.answer = value1 / value2
      self.answer = str(self.answer)
      self.cor_sign()
      self.value1 = self.answer
      self.value2 = ""
      self.operation = ""
    except:
      self.call_error()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "Sin", row = 0, style = discord.ButtonStyle.blurple)
  async def sin(self, interaction: discord.Interaction, button: discord.ui.Button):
    if self.operation == "" and self.value2 == "":
      self.answer = str(round(math.sin(self.pi_con(self.value1)), 10))
      self.cor_sign()
      self.selected = self.answer
      self.value1 = "0"
      self.value2 = ""
      self.operation = ""
      self.change_val()
    else:
      self.call_error()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "Cos", row = 1, style = discord.ButtonStyle.blurple)
  async def cos(self, interaction: discord.Interaction, button: discord.ui.Button):
    if self.operation == "" and self.value2 == "":
      self.answer = str(round(math.cos(self.pi_con(self.value1)), 10))
      self.cor_sign()
      self.selected = self.answer
      self.value1 = "0"
      self.value2 = ""
      self.operation = ""
      self.change_val()
    else:
      self.call_error()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "Tan", row = 2, style = discord.ButtonStyle.blurple)
  async def tan(self, interaction: discord.Interaction, button: discord.ui.Button):
    if self.operation == "" and self.value2 == "":
      self.answer = str(round(math.tan(self.pi_con(self.value1)), 10))
      self.cor_sign()
      self.selected = self.answer
      self.value1 = "0"
      self.value2 = ""
      self.operation = ""
      self.change_val()
    else:
      self.call_error()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)

  @discord.ui.button(label = "π", row = 3, style = discord.ButtonStyle.blurple)
  async def pi(self, interaction: discord.Interaction, button: discord.ui.Button):
    self.selected = "π"
    self.change_val()
    embed = self.emb()
    await interaction.response.edit_message(embed=embed)