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

    self.state = {
      "location": "start",
      "item": "none"
    }

  def play(self):
    if self.gameOver:
      self.gameOver = False
      self.getLocationNames()
      print("Starting puzzle {}!".format(self.name))
      while not self.gameOver:
        instruction = raw_input("Enter an instruction: ")
        self.handleInstruction(instruction)
    else:
       print("Game already started!")

  def getLocationNames(self):
    def getNames(location):
      return location.name
    return map(getNames, self.locations)

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
    self.state["location"] = location

  def handleInstruction(self, instruction):
    if not isinstance(instruction, list):
      instruction = [instruction]

    for inst in instruction:
      instructionWords = inst.split()
      if "and" in instructionWords:
        instructionSplit = inst.split("and")
        self.handleInstruction(instructionSplit)
        return

    locationNames = self.getLocationNames()

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
      commonAdvance = common_data(language.dictionary["go"], instructionWords)

      if commonAdvance:
        if commonLocation:
          print(commonAdvance, commonLocation)
          if commonLocation == self.state["location"]:
            print("you are already in ", commonLocation)
          else:
            print("You are moving to ", commonLocation)
            self.goToLocation(commonLocation)
        else:
          print("I couldn't understand where you want to go.")
      else:
        print("Sorry I don't understand")