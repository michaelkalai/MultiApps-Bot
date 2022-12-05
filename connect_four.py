import discord

class Connect_Four():
  def __init__(self, ctx, user1, user2):
    self.ctx = ctx
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
    # for row in self.board:
    #   print(row)
    pass
  
  def insert_chip(self, chip, col):
    self.board.reverse()
    for row in self.board:
      if row[col] == '-':
        row[col] = chip
        break
    self.board.reverse()

  def has_space(self, col):
    for row in range(self.rows):
      if self.board[row][col] == '-':
        print(row, col)
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
    return False

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
                      print('check_diag_2')
                      return True
      return False

  def check_winner(self, chip):
    if self.check_cols(chip) or self.check_rows(chip) or self.check_diagonals(chip):
      return True
    