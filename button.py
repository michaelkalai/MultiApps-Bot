import discord
from discord.ext import commands
import random


class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = 0

    @discord.ui.button(label="Fold", style=discord.ButtonStyle.blurple)
    async def menu1(self, interaction: discord.Interaction,
                    button: discord.ui.Button):
        print(interaction.user)
        await interaction.response.send_message("Hello You Clicked Me")
