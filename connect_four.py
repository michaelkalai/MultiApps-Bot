import discord
from discord.ext import commands
import random

class Connect_Four():
  def __init__(self, bot, user1, user2):
    self.bot = bot
    self.user1 = user1
    self.user2 = user2
    self.rows = 6
    self.cols = 7
    self.board = [
      ['-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-'],
      ['-', '-', '-', '-', '-', '-', '-']
    ]

  def display_board(self):
    temp_board = []
    temp_board.append(self.board)
    temp_board[0].reverse()
    return temp_board[0]
  
  def insert_chip(self, chip, col):
    self.board.reverse()
    for row in self.board:
      if row[col] == '-':
        row[col] = chip
    self.board.reverse

  def has_space(self, col):
    for row in range(self.rows):
      if self.board[row][col] == '-':
        return True
    return False
  
  def check_cols(self, chip):
    for col in range(self.cols):
      count = 0
      for row in range(self.rows):
        if count == 4:
          return True
        elif self.board[row][col] == chip:
          count += 1
        else:
          count = 0

  def check_rows(self, chip):
    for row in range(self.rows):
      count = 0
      for col in range(self.cols):
        if count == 4:
          return True
        elif self.board[row][col] == chip:
          count += 1
        else:
          count = 0
          
  def check_diagnols(self, chip):
    for i in range(self.rows - 4):
      count = 0
      row = i
      col = 0
      for x in range(self.cols):
        if count == 4:
          return True
        elif self.board[row][col] == chip:
          count += 1
          row += 1
          col += 1
        else:
          break
    for i in range(4, self.rows):
      count = 0
      row = i
      col = 0
      for x in range(self.cols):
        if count == 4:
          return True
        elif self.board[row][col] == chip:
          count += 1
          row -= 1
          col += 1
        else:
          break

  def check_winner(self):
    if self.check_cols or self.check_rows or self.check_diagnols:
      return True
      
    