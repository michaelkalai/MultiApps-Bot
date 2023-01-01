import discord
import copy




class Connect_Four():
  def __init__(self, ctx, user1, user2, user1_id, user2_id):
    self.ctx = ctx
    self.user1 = user1
    self.user2 = user2
    self.user1_id = user1_id
    self.user2_id = user2_id
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

  # converts chips from backend into emojis for frontend
  def chip_to_cir(self, chip):
    if chip == 'x':
      return ':red_circle:'
    elif chip == 'o':
      return ':yellow_circle:'
    else:
      return ':white_circle:'

  # temporarily joins board together to display to user
  def display_board(self, player):
    con_board = copy.deepcopy(self.board)
    for i in range(self.rows):
      con_board[i] = [self.chip_to_cir(value) for value in con_board[i]]
    temp_board = ['   '.join(row) for row in con_board]
    embed = discord.Embed(title="Connect 4",
                              url="",
                              description="",
                              color=0xFF5733)
    embed.add_field(name=":one: " + ":two: " + ":three: " + ":four: " + ":five: " + ":six: " + ":seven: ",
                        value=temp_board[0] + "\n" + temp_board[1] + "\n" + temp_board[2] + "\n" + temp_board[3] + "\n" + temp_board[4] + "\n" + temp_board[5],
                        inline=False)
    embed.add_field(name=f"{player}\'s turn", value="Type \'concede\' to surrender")
    return embed

  def display_loss(self):
    embed = discord.Embed(color = 0xFF5733, description = "")
    embed.set_image(url='https://media1.tenor.com/images/5cadbe1c0b073aae7bca19306cc14d3e/tenor.gif?itemid=18423674')
    return embed

  # searches for the first open slot in a column to add a chip
  def insert_chip(self, chip, col):
    self.board.reverse()
    for row in self.board:
      if row[col] == '-':
        row[col] = chip
        break
    self.board.reverse()

  # checks for available space in a selected column
  def has_space(self, col):
    for row in range(self.rows):
      if self.board[row][col] == '-':
        return True
    return False

  # checks vertically for a winner
  def check_cols(self, chip):
    for col in range(self.cols):
        count = 0
        for row in range(self.rows):
            if self.board[row][col] == chip:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
    return False

  # checks horizontally for a winner
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
      return False

  # checks diagonally for a winner
  def check_diagonals(self, chip):
      for k in range(0, self.cols - 3):
          for i in range(0, self.rows - 3):
              count = 0
              row = i
              col = k
              for x in range(0, self.cols - 3):
                  if self.board[row][col] == chip:
                      count += 1
                  else:
                      count = 0
                  if count == 4:
                      return True
                  row += 1
                  col += 1
          # each for looop checks in a different diagnol direction
          for i in range(3, self.rows):
              count = 0
              row = i
              col = k
              for x in range(3, self.cols):
                  if self.board[row][col] == chip:
                      count += 1
                  else:
                      count = 0
                  row -= 1
                  col += 1
                  if count == 4:
                      return True
      return False

  # checks previous functions to check for a winner
  def check_winner(self, chip):
    if self.check_cols(chip) or self.check_rows(chip) or self.check_diagonals(chip):
      return True

  # checks every row and column for an empty space
  def is_full(self):
    for row in self.board:
      for col in row:
        if col == '-':
          return False
    return True
    