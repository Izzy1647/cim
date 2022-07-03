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
    # play music interview fadein 2.0

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
            call selfintro(candidate='Joe')
        "Bring on Fizzbuzz!":
            jump prefizzbuzz

label prefizzbuzz:
    m "Let's solve a coding problem really fast, okay?"
    if isJoe:
        show joe fear close at left
        with dissolve

        j "Ohh..."
        j "Okay..."
        j "Very stright forward..."
        j "What's it?"

        jump fizzbuzzcore
    
    if isEmily:
        e "Sure!"
        jump fizzbuzzcore
    

label postfizzbuzz(mark='good', candidate=''):
    if isJoe:
        show joe general close at left
        with dissolve

    menu:
        "End the interview right now" if mark == 'poor' or mark == 'very poor':
            m "Sorry.."
            jump ending
        "Continue with another coding challenge":
            m "You did [mark] on fizzbuzz, let's move on to the next question!"
            menu:
                "Two Sum":
                    jump twosum
                "Longest Palindromic Substring":
                    jump lps
    

label postTwosum:
    if isJoe:
        m "Nice job on two sum."
   
    if isEmily:
        m "Well done."
    
    menu:
        "Bring on another coding problem!":
            m "Let's keep doing this alright?"
            jump lps
        "End the interview now.":
            jump ending


label postLps:
    if isJoe:
        jump postJoe
    
    if isEmily:
        jump postEmily
       

label postJoe:
    m "And I think this is all for today. Thank you for your time."
        
    j "Okay... Thank you."

    hide joe general close
    with dissolve

    "Now it's your time to provide a detailed feedback on Joe's overall performance."

    python:
        joeFeedbackPositive = renpy.input("Write down what Joe did great:", length=100)  
        joeFeedbackPositive = joeFeedbackPositive.strip()

        joeFeedbackNegative = renpy.input("Write down what Joe did poorly:", length=100)  
        joeFeedbackNegative = joeFeedbackNegative.strip()
    
    $ isJoe = False
    
    "It's break time!"
    
    call bridge(candidate='joe')


label postEmily:
    m "You did nice. And it's all for today."
    e "Okay, thank you!"

    hide emily general close
    with dissolve

    "Now it's your time to provide a detailed feedback on Emily's overall performance."

    python:
        emilyFeedbackPositive = renpy.input("Write down what Emily did great:", length=100)  
        emilyFeedbackPositive = emilyFeedbackPositive.strip()

        emilyFeedbackNegative = renpy.input("Write down what Emily did poorly:", length=100)  
        emilyFeedbackNegative = emilyFeedbackNegative.strip()
    
    $ isEmily = False
    
    "It's break time!"
    
    call bridge(candidate='emily')
    

label bridge(candidate='joe'):
    show boss happy close
    with dissolve

    if candidate == 'joe':
        b "How's it going on? You feeling alright?"
        m "Yeah, I'm good."
        b "How's the last candidate? Good?"
        menu:
            "Good":
                m "Yes, he's good. But there are still two remaining."
                b "Yes, sure. The second candidate will be here soon."
                hide boss happy close
                with dissolve
            "Not so good":
                m "Hmm, can't say that."
                show boss surprise close
                with dissolve
                b "Okay, luckily we have two candidates remaining. Buckle up buddy!"
                hide boss surprise close
                with dissolve
        
        jump interviewEmily
    
    if candidate == 'emily':
        b "How's Emily?"
        menu:
            "Good":
                m "She's great."
                b "That's nice to hear."
                b "Adam will be here soon."
                m "Okay."

                hide boss happy close
                with dissolve

            "Not so good":
                m "Can't say she's good."

                show boss serious close
                with dissolve

                b "Hmm okay, just make sure to use your best judgment."
                m "Will do."

                hide boss serious close
                with dissolve

        jump interviewAdam
        


label interviewEmily:
    $ isEmily = True

    show emily general at left
    with dissolve

    e "Hi! I'm Emily."
    e "I'm here for the software engineer position!"

    m "Yes, yes, welcome. Take a seat please."
    
    show emily general close at left
    with dissolve

    menu:
        "Start with a brief self introduction":
            call selfintro(candidate='Emily')
        "Bring on Fizzbuzz!":
            jump prefizzbuzz


label interviewAdam:
    $ isAdam = True
    "pass"



label ending:
    "end pass"


