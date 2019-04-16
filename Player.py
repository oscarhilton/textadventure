import language

class Player:
  def __init__(self):
    self.inventory = list()
  def pickUpItem(self, item):
    self.inventory.append(item)
    print("{} the {}".format(language.lookup("you picked up", language.dictionary), item.name))
  def hasItem(self, item):
    return True if item in self.inventory else False