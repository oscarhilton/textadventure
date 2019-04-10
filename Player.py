import language

class Player:
  def __init__(self):
    self.alive = True
    self.inventory = list()
  def pickUpItem(self, item):
    self.inventory.append(item)
    print("{} the {}".format(language.lookup("you picked up", language.dictionary), item.name))
  def die(self):
    self.alive = False