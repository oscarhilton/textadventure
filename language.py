import random

dictionary = {
  "you picked up": ["you reached out and grabbed", "good eyes. You located", "nice, looks like you found"],
  "go": ["explore", "go", "advance", "enter", "move"],
  "goBack": ["leave", "exit", "evacuate"],
  "explore": ["explore", "look", "around", "investigate", "search", "seek", "gaze"]
}

def lookup(toFind, array):
  return random.choice(array[toFind])