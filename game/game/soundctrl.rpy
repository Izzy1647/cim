screen musicSwitchButton():
    fixed:
        # modal True
        imagebutton auto "music_off_%s.png":
            pos (10, 690)
            action PauseAudio("music", value="toggle")

