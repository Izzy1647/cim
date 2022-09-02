label selfintro(candidate=''):
    m 'Why not do a self introduction of yourself, [candidate]?'

    if candidate == "Joe":
        return 

    if candidate == "Emily":
        e "Sure."

        play music "/audio/emily-intro.mp3"
        "Emily speaking... Make sure you are not muted."
        "Press space if you want to skip. But don't."
        stop music
    
    if candidate == "Adam":
        a "Okay."

        play music "/audio/adam-intro.mp3"
        "Adam speaking... Make sure you are not muted."
        "Press space if you want to skip. But don't."
        stop music


    return
