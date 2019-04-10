import random

dictionary = {
  "you picked up": ["you reached out and grabbed", "good eyes. You located", "nice, looks like you found"]
}

def lookup(toFind, array):
  return random.choice(array[toFind])