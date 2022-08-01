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

    python:
        interviews = ["interviewjoe", "interviewEmily", "interviewAdam"]
        renpy.random.shuffle(interviews)
        
    call expression interviews[0]

    return


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
            call selfintro(candidate='Joe') from _call_selfintro
        "Bring on Fizzbuzz!":
            jump prefizzbuzz
    
    return

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
    
    if isAdam:
        a "Okay."
        jump fizzbuzzcore
    

label postfizzbuzz(mark='good', candidate=''):
    if isJoe:
        show joe general close at left
        with dissolve

    menu:
        "End the interview right now" if mark == 'poor' or mark == 'very poor':
            m "Sorry.."
            if isJoe:
                jump postJoe
            if isEmily:
                jump postEmily
            if isAdam:
                jump postAdam

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
            if isJoe:
                jump postJoe
            if isEmily:
                jump postEmily
            if isAdam:
                jump postAdam


label postLps:

    # if more questions are enabled, insert here

    if isJoe:
        jump postJoe
    
    if isEmily:
        jump postEmily
    
    if isAdam:
        jump postAdam
       

label postJoe:
    m "I think this is all for today. Thank you for your time."
        
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
    

    python:
        idx = interviews.index('interviewjoe')

    if idx == 2:
        jump ending

    "It's break time!"

    call bridge(candidate='joe') from _call_bridge
    
    call expression interviews[idx + 1]

    return
    


label postEmily:
    m "It's all for today."
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

    python:
        idx = interviews.index('interviewEmily')

    if idx == 2:
        jump ending
    
    "It's break time!"

    call bridge(candidate='emily') from _call_bridge_1

    call expression interviews[idx + 1]

    return
    
    
    
label postAdam:
    m "It's all for today, thank you for your time."
    a "No big deal, thank you for your time."

    hide adam smile close
    with dissolve

    "Now it's your time to provide a detailed feedback on Adam's overall performance."

    python:
        adamFeedbackPositive = renpy.input("Write down what Adam did great:", length=100)  
        adamFeedbackPositive = adamFeedbackPositive.strip()

        adamFeedbackNegative= renpy.input("Write down what Adam did poorly:", length=100)  
        adamFeedbackNegative = adamFeedbackNegative.strip()
    
    $ isAdam = False

    python:
        idx = interviews.index('interviewAdam')

    if idx == 2:
        jump ending
    
    call bridge(candidate='adam')

    call expression interviews[idx + 1]

    return


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
            call selfintro(candidate='Emily') from _call_selfintro_1
        "Bring on Fizzbuzz!":
            jump prefizzbuzz
    
    return


label interviewAdam:
    $ isAdam = True

    show adam general at right
    with dissolve

    a "Hi I'm Adam."
    m "Hi, welcome... to the interview? Take a seat please."
    a "Haha, yes, thank you."

    show adam general close at left
    with dissolve

    m "So, huh, let's do it!"

    show adam smile close at left
    with dissolve

    menu:
        "Start with a brief self introduction":
            call selfintro(candidate='Adam') from _call_selfintro_2
        "Bring on Fizzbuzz!":
            jump prefizzbuzz
    
    return


label ending:
    "This is all three candidates for today."
    "Now you can check all marks and reviews you made on three candidates, and make your final decision on who to employ."

    show joe general at left
    with dissolve

    show emily general at center
    with dissolve

    show adam general at right
    with dissolve

    # call screen ending_menu

    
    label candidates_menu:
        menu:
            "Joe":
                show screen report(candidate='Joe') 
                ""
            "Emily":
                show screen report(candidate='Emily')
                ""
            "Adam":
                show screen report(candidate='Adam')
                ""


label decision:
    "Now it's your time to make the final decision on who to hire."
    menu:
        "I'm ready":
            jump decision_menu
                
        "I want to revisit the overviews":
            jump candidates_menu
    
    label decision_menu:
        menu:
            "Choose from the menu above. Who will you pick?"
            "Joe":
                $ decision = 'joe'
            "Emily":
                $ decision = 'emily'
            "Adam":
                $ decision = 'adam'
        
        hide joe general with dissolve
        hide emily general with dissolve
        hide adam general with dissolve

        if isFirst:
            call send_data

        scene bg report
        with fadehold

        "Now let's get back to your selection. Why do you choose [decision]?"


        "Select the factor that you think matters the most in the menu."

        menu:
            "Appearence: he looks like a good engineer!" if decision == 'joe' or decision == 'adam':
                $ reason = 'appearance'
            "Appearence: she's really appealing!" if decision == 'emily':
                $ reason = 'appearance'
            "Coding ability: bug free code during the interview":
                $ reason = 'ability'
            "Vibe: I like how we interact":
                $ reason = 'vibe'
            "Gender: I need a female engineer in my group" if decision == 'emily':
                $ reason = 'gender'
            "Gender: male engineers are more capable" if decision == 'joe' or decision == 'adam':
                $ reason = 'gender'
        
        # post plots & educational chapter based on player's decision
        
        if decision == 'emily' and reason == 'ability':
            call emilyStory

            scene bg report
            with fadehold

            menu:
                "Now, knowing how Emily manage to perform well in the interview, will you change your mind?"
                "Yes":
                    jump decision_menu

                "No":
                    scene bg office
                    with fadehold

                    "It's always hard to give up a well-performing candidate like Emily."
                    "Let's take a look at how Emily performs in work."

                    call emilyInWork

                    menu:
                        "Would you like to make another pick on who to hire?"
                        "Yes":
                            $ isFirst = False
                            jump decision_menu
                        "No":
                            jump game_ending


        if reason == 'appearance':
            scene bg caution
            with fadehold

            "Careful, {b}Attractiveness Bias{/b} may have affected your judgment." 
            "Attractive bias during interview is widely researched."

            show attractiveness1 at topleft
            with dissolve

            ""

            show attractiveness2 at topright
            with dissolve

            ""

            show attractiveness3 at top
            with dissolve

            ""

            "And so many on..."

            hide attractiveness2 with dissolve
            hide attractiveness3 with dissolve

            "Take the article {a=https://www.researchgate.net/publication/247808468_Attractiveness_Bias_in_the_Interview_Exploring_the_Boundaries_of_an_Effect} Attractiveness Bias in the Interview: Exploring the Boundaries of an Effect{/a} as an example."
            
            show attractiveness conclusion at topright
            with dissolve

            "Attractive applicants in the study tended to be evaluated by interviewers as having higher qualifications than unattractive applicants."

            # hide attractiveness conclusion

            # show attractiveness conclusion2 at topright
            # with dissolve

            # "But in the final decision stage, attractiveness doesn't have a significant effect."

            # "However in a job intercie"
            
            scene bg nerd
            with fadehold

            "In IT industry sometimes it can even be the opposite: applicants with 'nerdy' appearance may be considered as better engineers."

            menu:
                "Would you like to make another pick on who to hire?"
                "Yes":
                    $ isFirst = False
                    jump decision_menu
                "No":
                    jump game_ending
                    
        
        if reason == 'gender':
            scene bg sex roles
            with fadehold

            "Careful, {b}Sex Role Stereotypes{/b} may have affected your judgment."
            "Lots of reaserches have discussed sex role stereotypes during interview."
            
            show sex1 at topleft
            with dissolve

            ""

            show sex2 at topright
            with dissolve

            ""

            show sex3 at top
            with dissolve

            ""

            "And so many other researches..."

            scene bg kin
            with fadehold

            "Traditionally people tend to believe that compared with men, women are more suitable for jobs like nurse, flight attendent, kindergartner, etc."

            scene bg se office
            with fadehold

            "Whereas in IT industry, software engineer is recogized as a male-dominant job."

            
            
            
        

        jump game_ending

        
        


label send_data:
    "Are you willing to share your in-game marks and decisions with us, 
    just for the use of research and discussion? 
    No personal data has been collected."

    menu:
        "Yes":
            jump send
        "No":
            return

    label send:
        init python:
            import requests

        show text "Please wait..."
        pause 0

        python:
            try:
                data = {
                    "joeMarkTwoSum": twosumMarkJoe,
                    "joeMarkLps": lpsMarkJoe,
                    "joeMarkFizzbuzz": fizzbuzzMarkJoe,
                    "emilyMarkFizzbuzz": fizzbuzzMarkEmily,
                    "emilyMarkTwoSum": twosumMarkEmily,
                    "emilyMarkLps": lpsMarkEmily,
                    "adamMarkFizzbuzz": fizzbuzzMarkAdam,
                    "adamMarkTwoSum": twosumMarkAdam,
                    "adamMarkLps": lpsMarkAdam,
                    "joeFeedbackPositive": joeFeedbackPositive,
                    "emilyFeedbackPositive": emilyFeedbackPositive,
                    "adamFeedbackPositive": adamFeedbackPositive,
                    "joeFeedbackNegative": joeFeedbackNegative,
                    "adamFeedbackNegative": adamFeedbackNegative,
                    "emilyFeedbackNegative": emilyFeedbackNegative,
                    "decision": decision
                }

                r = requests.post("https://cim-be.cyclic.app/records", json=data)
                
            except:
                r = None

        hide text

        "Thank you. You can visit {a=https://cim-analysis-fe.vercel.app}the website{/a} to check the statisitics."

        return
        


label post_interview:
    "pass"




label bridge(candidate='joe'):
    show boss happy close
    with dissolve

    if candidate == 'joe':
        b "How's it going on? You feeling alright?"
        m "Yeah, I'm good."
        b "How's Joe? Good?"
        menu:
            "Good":
                m "Yes, he's good."
                b "Nice. The next candidate will be here soon."
                hide boss happy close
                with dissolve
            "Not so good":
                m "Hmm, can't say that."
                show boss surprise close
                with dissolve
                b "Okay. The next candidate will be here soon."
                hide boss surprise close
                with dissolve
        
    
    if candidate == 'emily':
        b "How's Emily?"
        menu:
            "Good":
                m "She's great."
                b "That's nice to hear."
                b "Get prepared for the net candidate."

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

    if candidate == 'adam':
        b "How's Adam?"
        menu:
            "Good":
                m "Good."
                b "Not bad."
                b "The next candidate will be here in a minute."

                hide boss happy close
                with dissolve

            "Not so good":
                m "Not so good."

                show boss serious close
                with dissolve

                b "Okay, it's fine. Hope we have a better candidate very soon."
                m "Yes."

                hide boss serious close
                with dissolve
    
    return


# screen ending_menu():
#     # add "bg interview"
#     modal True

#     imagebutton auto "joe_general_%s":
#         # focus_mask True
#         hovered SetVariable("screen_tooltip", "Joe")
#         unhovered SetVariable("screen_tooltip", "")
#         action Jump("ending")


label game_ending:
    "Game ending"

    $ MainMenu(confirm=False)()
