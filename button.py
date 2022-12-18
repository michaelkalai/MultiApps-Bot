import discord
from discord.ext import commands
import random

class Menu(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None

  @discord.ui.button(label="Send Message", style = discord.ButtonStyle.grey)
  async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
    await interaction.response.send_message("Hello You Clicked Me")

# Testing a basic button