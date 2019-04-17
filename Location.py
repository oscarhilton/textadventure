class Location:
  def __init__(self, name, exploreText, areas = []):
    self.name = name
    self.areas = areas
    self.exploreText = exploreText

  def explore(self):
    areaAmount = len(self.areas)
    print(self.exploreText)
    print("There are {} places to look...".format(areaAmount))
    for area in self.areas:
      print("You can explore ", area.name)

  def leave(self):
    print("You left ", self.name)