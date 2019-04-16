class HiddenItem:
  def __init__(self, name, item, key = False):
    self.name = name
    self.item = item
    self.key = key
    self.unlocked = False if key else True
    self.found = False

  def useKey(self, key):
    if not self.key:
      return
    if key == self.key:
      self.unlocked = True
    else:
      print("{} did not open {}".format(key, self.name))
      self.unlocked = False 