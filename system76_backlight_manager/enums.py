from enum import Enum


class Position(Enum):
    LEFT = 1
    CENTER = 2
    RIGHT = 3
    EXTRA = 4


class Mode(Enum):
    BREATHE = "breathe"
    STATIC = "static"
