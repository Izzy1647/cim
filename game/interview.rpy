# the night before interview at bedroom
label bedroom:
    stop music fadeout 2.0

    scene bg bedroom
    with fadehold

    "Come on, it's just a coding interveiw...we've all been there!"
    "I can do this...bring Fizzbuzz in..."
    "Or is it too simple..."
    "Or not? Damn..."

    jump preInterview


label preInterview:
    play music interview fadein 2.0

    scene bg interview
    with fadehold
    "Next day, 1pm"

    jump interviewjoe


# joe: he seems nervous but he actually does well on these questions
label interviewjoe:
    $ isJoe = True

    # first interviewee character https://charactercreator.org/#skinColor=%23e5a073&irisColor=%23784421&hairColor=%231a1a1a&pupils=round&sex=m&body_head=square&ears=unplugged&nose=roman&emotion=surprise&shirt=kurta&shirtColor=%231F303F&pants=jeans_rolled&pantsColor=%23BAE0A8&vest=shawl_pointed&vestColor=%23BAE0A8&jacket=suit_open&jacketColor=%23BAE0A8&hair=buzzcut&facialhair=winnfield&earings=gold_rings
    show joe general at right
    with dissolve


    j "Hey I'm Joe..." 
    j "I'm here, um...," 
    j "for the software engineer position."
    j "Ummmm... is this the place?"
    
    m "Yes. Take a seat please."

    j "Thank you."

    show joe general close at left
    with dissolve

    j "So... Where do we begin?"

    menu:
        "Start with a brief self introduction":
            jump selfintro
        "Bring on Fizzbuzz!":
            jump prefizzbuzz

label prefizzbuzz:
    if isJoe:
        m "Let's solve a coding problem really fast, okay?"

        show joe fear close at left
        with dissolve

        j "Ohh..."
        j "Okay..."
        j "Very stright forward..."
        j "What's it?"

        jump fizzbuzzcore

label postfizzbuzz:
    menu:
        "Ask for a self introduction" if hasSelfIntroducedJoe == False:

            # here I use call which may cause some unexpected side effects
            call selfintro(candidate='Joe')

        "End the interview right now" if fizzbuzzMarkJoe <= 2:
            m "Sorry.."
            jump bridge
        "Continue with another coding challenge":
            m "You did good on fizzbuzz, let's move on to the next question!"
            jump nextquestion

label nextquestion:
    menu:
        "Two Sum":
            jump twosumcore
        "Longest Palindromic Substring":
            jump lpscore

label bridge:
    "bridge"
  

  
