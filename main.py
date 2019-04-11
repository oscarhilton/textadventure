from Player import Player
from Item import Item
from Puzzle import Puzzle
from Story import Story

player = Player()

note = Item("note", "fridge", ["Check the fridge", "Look in the cool fridge bro"])
scissors = Item("scissors", "table", ["Snip snip"])

# player.pickUpItem(note)

mobile5 = Puzzle(
  "Mobile5",
  [ #locations
    "living room",
    "kitchen"
  ],
  [ #items
    note,
    scissors
  ],
  [ #story
    Story("You find youself in an office."),
    Story("It is a nice office"),
    Story("Look at all the things in the office"),
    Story("You need a note to continue", player.hasItem(note))
  ]
)

mobile5.play()


# note.useItem()
# player.pickUpItem(scissors)
# scissors.useItem()

# for x in player.inventory:
#   print(x.useClue())
