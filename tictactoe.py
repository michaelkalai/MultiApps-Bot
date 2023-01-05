import discord
from discord.ext import commands
import random

class Tictactoe(discord.ui.View):
  def __init__(self, user1, user2):
    super().__init__()
    self.user1 = user1
    self.user2 = user2
    self.board = [["-", "-", "-"],
                 ["-", "-", "-"],
                 ["-", "-", "-"]]
    self.game_over = False
    self.current_piece = "X"
    self.current_user = self.user1
    time_game = False

  def tie_game(self):
    for row in self.board:
      for value in row:
        if value == "-":
          return False
    return True

  def check_winner(self, piece):
    for row in self.board:
      if row.count(piece) == 3:
        return True
    for col in range(3):
      if piece == self.board[0][col] == self.board[1][col] == self.board[2][col]:
        return True
    if piece == self.board[0][0] == self.board[1][1] == self.board[2][2]:
      return True
    if piece == self.board[2][0] == self.board[1][1] == self.board[0][2]:
      return True
    return False

  def bot_check_col(self, col, piece):
    count = 0
    empty_space = False
    for row in self.board:
      if row[col] == piece:
        count += 1
      elif row[col] == "-":
        empty_space = True
    if count == 2 and empty_space:
      return True
    return False

  def bot_check_row(self, row, piece):
    count = 0
    empty_space = False
    for val in row:
      if val == piece:
        count += 1
      elif val == "-":
        empty_space = True
    if count == 2 and empty_space:
      return True
    return False

  def bot_check_diagonal1(self, piece):
    count = 0
    empty_space = False
    for i in range(3):
      if self.board[i][i] == piece:
        count += 1
      elif self.board[i][i] == "-":
        empty_space = True
    if count == 2 and empty_space:
      return True
    return False

  def bot_check_diagonal2(self, piece):
    count = 0
    empty_space = False
    if self.board[2][0] == piece:
      count += 1
    elif self.board[2][0] == "-":
      empty_space = True
    if self.board[1][1] == piece:
      count += 1
    elif self.board[1][1] == "-":
      empty_space = True
    if self.board[0][2] == piece:
      count += 1
    elif self.board[0][2] == "-":
      empty_space = True
    if count == 2 and empty_space:
      return True

  def insert_piece_row(self, row):
    for col in range(3):
      if self.board[row][col] == "-":
        return col

  def insert_piece_col(self, col):
    for row in range(3):
      if self.board[row][col] == "-":
        return row

  def insert_piece_diagonal1(self):
    for i in range(3):
      if self.board[i][i] == "-":
        return i, i

  def insert_piece_diagonal2(self):
    if self.board[2][0] == "-":
      return 2, 0
    elif self.board[1][1] == "-":
      return 1, 1
    else:
      return 0, 2

  def bot_turn(self):
    for i in range(3):
      if self.bot_check_row(i, "O"):
        return i, self.insert_piece_row(i)
      elif self.bot_check_col(i, "O"):
        return self.insert_piece_row(i), i

    if self.bot_check_diagonal1("O"):
      return self.insert_piece_diagonal1()
    elif self.bot_check_diagonal2("O"):
      return self.insert_piece_diagonal2()
    
    for i in range(3):
      if self.bot_check_row(i, "X"):
        return i, self.insert_piece_row(i)
      elif self.bot_check_col(i, "X"):
        return self.insert_piece_col(i), i
    
    if self.bot_check_diagonal1("X"):
      return self.insert_piece_diagonal1()
    elif self.bot_check_diagonal2("X"):
      return self.insert_piece_diagonal2()

    row, col = 1, 1
    while self.board[row][col] != "-":
      row = random.randint(0, 2)
      col = random.randint(0, 2)
    return row, col

  def insert_piece(self, row, col, piece):
    self.board[row][col] = piece
    button1 = [x for x in self.children if x.custom_id == str(row) + str(col)][0]
    button1.label = piece

  def emb(self):
    embed = discord.Embed(color = 0xFF5733)
    if self.game():
      embed.add_field(name = "TicTacToe", value = "Tie Game")
    else:
      embed.add_field(name = "TicTacToe", value = f"{self.current_user} has won!")

  @discord.ui.button(label = "-", row = 0, style = discord.ButtonStyle.blurple,  custom_id = "00")
  async def zerozero(self, interaction: discord.Interaction, button: discord.ui.Button):
    if not self.game_over:
      self.insert_piece(0, 0, self.current_piece)
      if self.check_winner(self.current_chip):
        await interaction.response.edit_message(view=self)
        await interaction.followup(embed=self.emb())
      elif self.user2 == "Myriad":
        self.current_user == self.user2
        self.current_piece == "O"
        row, col = self.bot_turn()
        self.insert_piece(row, col, self.current_piece)
        
        

    
      
      
      

  