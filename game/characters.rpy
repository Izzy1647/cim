# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Boss")
define m = Character('Me', color="#c8c8ff")

# the first candidate Joe
define j = Character("Joe")

# the second candidate Emily
define e = Character("Emily")

# test customize character definition
define test = Character(
    None,
    window_background=None,
    what_color="#fff",
    what_xalign=0.5
)