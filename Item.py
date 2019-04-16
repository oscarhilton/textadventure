class Item:
  def __init__(self, name, clues):
    self.name = name
    self.used = False
    self.clues = clues
    self.clueIndex = -1

  def useItem(self):
    self.used = True

  def useClue(self):
    if self.clues:
      if self.clueIndex < (len(self.clues) - 1):
        self.clueIndex = self.clueIndex + 1
      else:
        self.clueIndex = 0
      print(self.clues[self.clueIndex], self.clueIndex)