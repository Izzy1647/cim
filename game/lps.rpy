label markJoeLps:
    menu:
        "Mark joe's performance on lps :)"
        "Very good":
            $ lpsMarkJoe = 5
        "Good":
            $ lpsMarkJoe = 4
        "Okay":
            $ lpsMarkJoe = 3
        "Poor":
            $ lpsMarkJoe = 2
        "Very poor":
            $ lpsMarkJoe = 1
    
    hide lps joe sol expand with dissolve
                
    jump postLps


label lpsJoeBfOptimization:
    m "What's the time complexity here?"

    j "Well...there are two loops, so..."
    j "O(n^2) I assume."

    show joe fear close at left
    with dissolve

    j "Oh wait..."
    j "In isPalindrom function, I need to loop over the string as well..." 
    j "so it is actually O(n^3)..."
    j "Sounds terrible..."

    m "Exactly. Do you think you can make it better?"

    show lps at topleft
    with dissolve

    show joe general close at left
    with dissolve

    j "Hmmm..."
    j "Let me think..."
    j "Hmmm..."

    show joe focus close at left
    with dissolve

    j "Well..."
    j "I think I have a vague idea here..."
    j "So in my last approach, I found every possible substring, and checked every one of them..."
    j "Which makes it super time-consuming."

    show joe excited close at left
    with dissolve

    j "Actually...if a substring is palindromic, I can check if it can expand to a longer palindromic string."
    j "Like if I got 'aba', I know that 'cabac' is palindromic as well."
    j "So there's no need to run it through isPalindrom method again."

    m "Bang! That's a good idea." 
    m "So in this case how fast can your algorithm be?"

    show joe focus close at left
    with dissolve

    j "O(n^2) I think."

    m "Cool, this is a big progress."
    m "Can you implement it?"

    show joe general close at left
    with dissolve

    j "Yes... I guess... I think it will be a completely different algorithm with the expanding idea."

    m "Yeah I think so. Take your time here."

    show joe focus close at left
    with dissolve

    "One minute passed..."
    "Two minutes passed..."
    "Three minutes passed..."

    show joe fear close at left
    with dissolve

    j "So first of all I have a function for expanding the string."

    show expand string joe at topright
    with dissolve
    
    m "Okay... returns a substring, looks fine."

    show joe focus close at left
    with dissolve

    j "Then I think I can loop over the given string..."
    j "And find the longest palindromic expanding from every character."

    m "Sounds nice."

    "One minute passed..."
    "Two minute passed..."
    "Three minute passed..."
    
    show joe excited close at left
    with dissolve

    hide expand string joe

    show lps sol joe expand at topright
    with dissolve

    j "Okay... I think this works."

    menu:
        "Ask for a even faster solution":
            m "Yes it works, good." 
            m "But do you think there is a even faster solution?"

            show joe fear close at left
            with dissolve

            j "Really?"
            m "I think so but it could be hard."

            show joe general close at left
            with dissolve

            j "Hmmmm..."
            "After a while..."
            j "Well I give up. I can't think of a faster solution, at least for now..."
            m "It's fine."
            jump markJoeLps


        "Mark Joe's performance":
            jump markJoeLps

label lps:
    show lps at topleft
    with dissolve

    m "This one is called longest palindromic substring."

    if isJoe:
        j "Yes...I think I understand the question."
        m "Great! So what do you think?"

        show joe struggling close at left
        with dissolve

        j "Hmmmm...."
        j "Need some time here again..."

        m "Sure don't worry."

        j "Again... I think I can do brutal force."
        j "Like... emmm..."
        j "Find all substring..." 
        j "And check if each of them is palindromic."

        m "Sure it works."

        show joe general close at left
        with dissolve

        menu:
            "Ask for an implementation":
                m "So could you implement it?"
                j "Yes, sure."
                j "So I think first of all..."
                j "I can create a function to check if a string is, um, palindromic."

                show joe focus close at left
                with dissolve
                
                "One minute passed..."
                "Two minutes passed..."

                show ispalindromic joe at topright
                with dissolve

                j "So it is the function, and it can be called in the main function."
                m "Sure, it looks fine."

                j "Then it's the main function..."
                j "So again the brutal force one is straight forward."

                show joe general close at left
                with dissolve

                "One minute passed..."
                "Two minutes passed..."

                show joe focus close at left
                with dissolve

                "Three minutes passed..."
                "Four minutes passed..."

                hide ispalindromic joe
                with dissolve

                show lps sol joe bf at topright
                with dissolve

                j "So it's just get all possible substrings and use isPalindrom function to check."

                menu:
                    "Fine, mark joe's solution now":
                        m "Yeah... looks fine."
                        jump markJoeLps
                    
                    "Dig deeper into the code":
                        m "Yes it works, definitely. But..."
                        jump lpsJoeBfOptimization


            "Ask for a faster solution":
                jump lpsJoeBfOptimization
                
    if isEmily:
        e "Yes."               