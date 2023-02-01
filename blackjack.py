import discord
from discord.ext import commands
import random

class Blackjack(discord.ui.View):
  def __init__(self, bet):
    super().__init__()
    self.bet = bet
    self.player_score = 0
    self.bot_score = random.randint(16, 22)
    self.card_types = [":clubs:", ":spades:", ":hearts:", ":diamonds:"]
    self.hand = []
    self.aces = []
    self.winner = None

  def emb(self):
    display = ""
    for card in self.hand:
      display += card
      if card != self.hand[-1]:
        display += "\n"
    
    embed = discord.Embed(color = 0xFF5733)
    embed.add_field(name = "Blackjack", value = "First to 21 wins")
    embed.add_field(name = "Your Hand", value = display)

    return embed
  
  def con_num_to_card(self, num):
    if num == 11:
      return "Jack"
    elif num == 12:
      return "Queen"
    elif num == 13:
      return "King"
    return num

  def check_ace(self):
    for ace in self.aces:
      if self.points > 21:
        if ace[1] == 11:
          self.points -= 10
          ace[1] = 1

  def add_points(self, num):
    if num == 11 or num == 12 or num == 13:
      self.player_score += 10
    elif num == 1:
      self.player_score += 11
    
  def deal_card(self):
    num = random.randint(1, 13)
    card_type = self.card_types[random.randint(0, 3)], 
    card_num = self.con_num_to_card(num)
    card = card_type + str(card_num)
    if card_num == 1:
      self.aces.append([card, 11])
    self.add_points(num)
    self.check_ace()
    self.hand.append(card)
    return card

  def end_game():
    pass

  @discord.ui.button(label="Send Message", style = discord.ButtonStyle.grey)
  async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
    print(interaction.user)
    await interaction.response.send_message("Hello You Clicked Me")