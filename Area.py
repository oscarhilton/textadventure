class Area:
  def __init__(self, name, hidingPlaces = []):
    self.name = name
    self.hidingPlaces = hidingPlaces

  def listHidingPlaces(self):
    for place in self.hidingPlaces:
      Print(place)
  