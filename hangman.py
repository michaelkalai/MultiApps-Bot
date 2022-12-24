import discord
from discord.ext import commands

class Hangman():
  def __init__(self, word, player):
    self.word = word
    self.display = ""
    self.completion = []
    self.player = player
    self.lives = 6
    self.used_letters = []

  def setup_display(self):
    for chr in self.word:
      if chr.isalpha():
        self.display += ":black_square_button:"
        self.completion.append(":black_square_button:")
      else:
        self.display += ":black_medium_square:"
        self.completion.append(":black_medium_square:")

  def check_letter(self, letter):
    correct_letter = False
    for i in range(len(self.word)):
      if self.word[i].lower() == letter:
        self.completion[i] = self.word[i]
        correct_letter = True
    self.display = "".join(self.completion)
    self.used_letters.append(letter)
    self.used_letters.sort()
    return correct_letter

  def check_completion(self):
    for i in range(len(self.word)):
      if self.word[i] != self.completion[i] and self.word[i] != " ":
        return False
    return True
      
  def embed(self):
    embed = discord.Embed(title="Hangman", description=f"Lives: {self.lives}\nLetters used: {', '.join(self.used_letters)}")
    embed.add_field(name = "Word", value = self.display)
    return embed