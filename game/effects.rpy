# Fade to black and back.
define fade = Fade(0.5, 0.0, 0.5)

# Hold at black for a bit.
define fadehold = Fade(0.5, 0.5, 0.5)

# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")



init:
    python:
        # This function will run a countdown of the given length. It will
        # be white until 5 seconds are left, and then red until 0 seconds are
        # left, and then will blink 0.0 when time is up.
        def countdown(st, at, length=0.0):

            remaining = length - st

            if remaining > 2.0:
                return Text("%.1f" % remaining, color="#fff", size=72), .1
            elif remaining > 0.0:
                return Text("%.1f" % remaining, color="#f00", size=72), .1
            else:
                return anim.Blink(Text("0.0", color="#f00", size=72)), None

image countdown = DynamicDisplayable(countdown, length=120.0)