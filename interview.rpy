# the night before interview at bedroom
label bedroom:
    stop music fadeout 2.0

    scene bg bedroom
    with fadehold

    "Come on, I can do this. Bring Fizzbuzz in..."
    "Or is it too simple..."
    "Or not? Damn..."

label interview1:
    play music interview fadein 2.0

    scene bg interview
    with fadehold
    "Next day, 1pm"

    # first interviewee character https://charactercreator.org/#skinColor=%23e5a073&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&sex=m&body_head=square&ears=unplugged&nose=roman&emotion=surprise&shirt=kurta&shirtColor=%231F303F&pants=jeans_rolled&pantsColor=%23BAE0A8&vest=shawl_pointed&vestColor=%23BAE0A8&jacket=suit_open&jacketColor=%23BAE0A8&hair=buzzcut&facialhair=winnfield&earings=gold_rings
    show joe general at right
    with dissolve

    j "Hey I'm Joe... I'm here for the software engineer position."
    j "I assume I'm not at the wrong place??"
    
    m "No, you are not. Take a seat please."

    j "Thank you."

    show joe general close at left
    with dissolve

    j "So... Where do we begin?"

    menu:
        "Start with a brief self introduction":
            jump introduction
        "Bring on Fizzbuzz!":
            jump fizzbuzz

label fizzbuzz:
    m "Let's solve a coding problem really fast, okay?"
    show joe fear close at left
    with dissolve
    j "Ohh..."
    j "Okay..."
    j "Very stright forward though."

label introduction:
    "introduction"
  

  
