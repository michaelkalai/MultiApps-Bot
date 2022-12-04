import discord
from discord.ext import commands
import random
from connect_four import Connect_Four

def connect_four_test():
  connect = Connect_Four('bot', 'Aaron', 'Omar')
  player = connect.user1
  chip = 'x'
  while True:
    
    print(f'{player}\'s turn')
    col = int(input('What column?'))
    if connect.has_space(col):
      connect.insert_chip(chip, col)
    if connect.check_winner():
      print(f'{player} has won!')
      break
    player = connect.user1 if player == connect.user2 else connect.user2
    chip = 'x' if chip == 'o' else 'x'
    