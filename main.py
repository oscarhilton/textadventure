from Player import Player
from Item import Item
from Puzzle import Puzzle

player = Player()

note = Item("note", "fridge", ["Check the fridge", "Look in the cool fridge bro"])
scissors = Item("scissors", "table", ["Snip snip"])
mobile5 = Puzzle("Mobile5", ["living room", "kitchen"], [note, scissors])

mobile5.play()

player.pickUpItem(note)
note.useItem()
player.pickUpItem(scissors)
scissors.useItem()

for x in player.inventory:
  print(x.useClue())
