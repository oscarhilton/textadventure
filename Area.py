class Area:
  def __init__(self, name, exploreText, hiddenItems = []):
    self.name = name
    self.hiddenItems = hiddenItems
    self.exploreText = exploreText

  def listHidingPlaces(self):
    for place in self.hiddenItems:
      print "there is a {}.".format(place.name)

  def explore(self):
    print self.exploreText
    print self.listHidingPlaces()
    return
  