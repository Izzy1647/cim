# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)

# Hold at black for a bit.
define fadehold = Fade(0.5, 0.5, 0.5)

# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

screen timer_test():
    vbox:
        textbutton "Yes." action Jump("yes")
        textbutton "No." action Jump("no")

    timer 3.0 action Jump("too_slow")

label yes:
    "yes"

label no:
    "no"

label too_slow:
    "too slow"