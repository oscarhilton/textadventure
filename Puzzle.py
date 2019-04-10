class Puzzle:
  def __init__(self, name, locations, items):
    self.name = name
    self.gameOver = True
    self.locations = locations
    self.items = items
  def play(self):
    if self.gameOver:
      self.gameOver = False
      print("Starting puzzle {}!".format(self.name))

    else:
       print("Game already started!")
  def restart(self):
    self.gameOver = False
  def finishPuzzle():
    self.gameOver = True
  def failedPuzzle():
    self.gameOver = True
