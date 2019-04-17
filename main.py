from Player import Player
from Item import Item
from Puzzle import Puzzle
from Story import Story
from Location import Location
from Area import Area
from HiddenItem import HiddenItem

mobile5 = Puzzle(
  "Old ship",
  Player(),
  [ #locations
    Location(
      "bow",
      "The front of the ship",
      [
        Area(
          "front",
          "front of the bow",
          [
            HiddenItem(
              "chest",
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
          "left",
          "left of the bow",
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
        ),
        Area(
          "right",
          "right of the bow",
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
      ],
    ),
    Location(
      "bathroom",
      "The ships bathroom",
      [
        Area(
          "bath",
          "there is a bathtub in front of you",
          [
            HiddenItem(
              "chest",
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
      ],
    )
  ],
  [ #story
    Story("You find youself in an office."),
  ]
).play()
