# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character("Boss")
define m = Character('Me', color="#c8c8ff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    play music intro fadein 0.5

    scene bg boss office

    # "It's a sunny monday...Another week coding starts now."


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # boss character
    # https://charactercreator.org/#skinColor=%23dfb684&irisColor=%23552200&hairColor=%231a1a1a&pupils=round&sex=m&body_head=oval&ears=default&nose=pointed&emotion=eeww&shirt=colar&shirtColor=%23C5BBAF&pants=leather&pantsColor=%239D9D9D&jacket=suit&jacketColor=%239D9D9D&hair=wreckingball&glasses=hipster
    show boss serious at left
    with dissolve

    # These display lines of dialogue.

    b "Hey buddy we need to hire a new software engineer."

    # img size for close: 600 x 600
    show boss serious close
    with dissolve

    b "I want you to take good care of it and hire a really great coder for us."

    menu:
        m "Okay..."
        "I think I can handle it.":
            jump agree
        "Umm I don't know if I can handle this.":
            jump drop
            #block of code to run

label agree:
    # m "Umm... Well I think I can handle that. What do I need to do?"

    show boss happy close at left
    with dissolve

    b "We got three candidates already."

    b "Just conduct interviews with them respectively and pick the best one out of them."

    m "Okay... So when do we do these interviews?"

    b "I've put them all in one day, starting from 1pm tomorrow."

    m "Tomorrow?? I can't say who's more nervous now, them or me..."

    show boss surprise close at left
    with dissolve

    b "Get yourself prepared."

    jump bedroom

    # scene black

    # "damn"

    return

label drop:
    b "wtf you are sacked"

    # This ends the game.

    return
