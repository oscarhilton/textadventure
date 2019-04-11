import time

class Puzzle:
  def __init__(self, name, locations, items, story):
    self.name = name
    self.gameOver = True
    self.locations = locations
    self.items = items
    self.story = story
    self.storyIndex = 0
  def play(self):
    if self.gameOver:
      self.gameOver = False
      print("Starting puzzle {}!".format(self.name))
      self.progressStory()
    else:
       print("Game already started!")
  def progressStory(self):
    time.sleep(0.2)
    if self.storyIndex <= (len(self.story) - 1):
      print(self.story[self.storyIndex].text)
      self.storyIndex = self.storyIndex + 1
      while True:
        if self.story[self.storyIndex - 1].completed == True:
          self.progressStory()
          break
    else:
      self.finishPuzzle()
  def restart(self):
    self.gameOver = False
  def finishPuzzle(self):
    self.gameOver = True
    print("You completed {}!".format(self.name))