from Player import Player
from Item import Item
from Puzzle import Puzzle
from Story import Story
from Location import Location
from Area import Area
from HiddenItem import HiddenItem

mobile5 = Puzzle(
  "Mobile5",
  Player(),
  [ #locations
    Location(
      "kitchen",
      [
        Area(
          "fridge",
          [
            HiddenItem(
              "Butter dish",
              Item(
                "note",
                [
                  "Check the fridge",
                  "Look in the cool fridge bro"
                ]
              ),
            )
          ]
        ),
        Area(
          "cupboard",
          [
            HiddenItem(
              "shelf",
              Item(
                "scissors",
                [
                  "Snip snip",
                  "scissor scissor"
                ]
              )
            )
          ]
        )
      ]
    )
  ],
  [ #story
    Story("You find youself in an office."),
  ]
).play()
