import time
import language

class Puzzle:
  def __init__(self, name, player, locations, story):
    self.name = name
    self.player = player
    self.gameOver = True
    self.locations = locations
    self.story = story
    self.storyIndex = 0

    self.currentLocation = locations[0]

  def play(self):
    if self.gameOver:
      self.gameOver = False
      print("Starting puzzle {}!".format(self.name))
      while not self.gameOver:
        instruction = raw_input("Enter an instruction: ")
        self.handleInstruction(instruction)
    else:
       print("Game already started!")

  def getNames(self, array):
    def returnName(item):
      return item.name
    return map(returnName, array)

  def progressStory(self):
    time.sleep(0.5)
    if self.storyIndex <= (len(self.story) - 1):
      print(self.story[self.storyIndex].text)
      if self.story[self.storyIndex].completed == True:
        self.storyIndex += 1
    else:
      self.finishPuzzle()

  def restart(self):
    self.gameOver = False

  def finishPuzzle(self):
    self.gameOver = True
    print("You completed {}!".format(self.name))

  def goToLocation(self, location):
    print("You moved to ", location)

  def handleInstruction(self, instruction):
    def getIndexByName(list, toFind):
      for x in list:
        if x.name == toFind:
          return list.index(x)

    if not isinstance(instruction, list):
      instruction = [instruction]

    for inst in instruction:
      instructionWords = inst.split()
      if "and" in instructionWords:
        instructionSplit = inst.split("and")
        self.handleInstruction(instructionSplit)
        return

    locationNames = self.getNames(self.locations)
    areaNames = self.getNames(self.currentLocation.areas)


    def common_data(list1, list2): 
      result = False
      for x in list1:
          for y in list2:
              if x == y:
                  result = x
                  return result            
      return result

    
    for inst in instruction:
      instructionWords = inst.split()

      commonLocation = common_data(locationNames, instructionWords)
      commonArea = common_data(areaNames, instructionWords)
      commonItem = None #Item
      commonAdvance = common_data(language.dictionary["go"], instructionWords)
      commonExplore = common_data(language.dictionary["explore"], instructionWords)

      if commonAdvance:
        if commonLocation:
          if commonLocation == self.currentLocation:
            self.currentLocation = self.locations[getIndexByName(self.locations, commonLocation)]
            print("you are already in ", commonLocation)
          else:
            self.currentLocation.leave()
            self.currentLocation = self.locations[getIndexByName(self.locations, commonLocation)]
            self.goToLocation(commonLocation)
        else:
          print("I couldn't understand where you want to go.")
      if commonExplore:
        if commonArea:
          self.currentLocation.areas[getIndexByName(self.currentLocation.areas, commonArea)].explore()
        else: 
          self.currentLocation.explore()
      if commonItem:
        print("Common item!")
