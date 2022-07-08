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
    
    hide lps joe sol expand js with dissolve
    hide lps joe sol expand py with dissolve
    hide lps joe sol expand pseudo with dissolve


    jump postLps

label markEmilyLps:
    menu:
        "Mark Emily's performance on lps :)"
        "Very good":
            $ lpsMarkEmily = 5
        "Good":
            $ lpsMarkEmily = 4
        "Okay":
            $ lpsMarkEmily = 3
        "Poor":
            $ lpsMarkEmily = 2
        "Very poor":
            $ lpsMarkEmily = 1
    
    hide lps emily sol expand js with dissolve
    hide lps emily sol expand py with dissolve
    hide lps emily sol expand pseudo with dissolve

                
    jump postLps

label markAdamLps:
    menu:
        "Mark Adam's performance on lps :)"
        "Very good":
            $ lpsMarkAdam = 5
        "Good":
            $ lpsMarkAdam = 4
        "Okay":
            $ lpsMarkAdam = 3
        "Poor":
            $ lpsMarkAdam = 2
        "Very poor":
            $ lpsMarkAdam = 1
    
    hide lps adam sol js with dissolve
    hide lps adam sol py with dissolve
    hide lps adam sol pseudo with dissolve
                    
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

    play sound "/audio/joeTyping.mp3" loop

    "One minute passed..."
    "Two minutes passed..."
    "Three minutes passed..."

    show joe fear close at left
    with dissolve

    stop sound

    j "So first of all I have a function for expanding the string."

    if language == 'js':
        show expand string joe js at topright
        with dissolve

    if language == 'python':
        show expand string joe py at topright
        with dissolve
    
    if language == 'pseudo':
        show expand string joe pseudo at topright
        with dissolve
    
    
    m "Okay... returns a substring, looks fine."

    show joe focus close at left
    with dissolve

    j "Then I think I can loop over the given string..."
    j "And find the longest palindromic expanding from every character."

    m "Sounds nice."

    play sound "/audio/joeTyping.mp3" loop

    "One minute passed..."
    "Two minute passed..."
    "Three minute passed..."
    
    show joe excited close at left
    with dissolve

    hide expand string joe js
    hide expand string joe py
    hide expand string joe pseudo


    if language == 'js':
        show lps sol joe expand js at topright
        with dissolve
    
    if language == 'python':
        show lps sol joe expand py at topright
        with dissolve
    
    if language == 'pseudo':
        show lps sol joe expand pseudo at topright
        with dissolve
    
    stop sound
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

                play sound "/audio/joeTyping.mp3" loop
                
                "One minute passed..."
                "Two minutes passed..."

                stop sound

                if language == 'js':
                    show ispalindromic joe js at topright
                    with dissolve
                
                if language == 'python':
                    show ispalindromic joe py at topright
                    with dissolve
                
                if language == 'pseudo':
                    show ispalindromic joe pseudo at topright
                    with dissolve

                j "So it is the function, and it can be called in the main function."
                m "Sure, it looks fine."

                j "Then it's the main function..."
                j "So again the brutal force one is straight forward."

                show joe general close at left
                with dissolve

                play sound "/audio/joeTyping.mp3" loop

                "One minute passed..."
                "Two minutes passed..."

                show joe focus close at left
                with dissolve

                "Three minutes passed..."
                "Four minutes passed..."

                stop sound

                hide ispalindromic joe js with dissolve
                hide ispalindromic joe py with dissolve
                hide ispalindromic joe pseudo with dissolve


                if language == 'js':
                    show lps sol joe bf js at topright
                    with dissolve
                
                if language == 'python':
                    show lps sol joe bf py at topright
                    with dissolve
                
                if language == 'pseudo':
                    show lps sol joe bf pseudo at topright
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
        m "So are you clear with what you need to do?"

        show emily concentrate close at left
        with dissolve

        e "Yes, give me some time."
        m "Sure."

        play sound "/audio/emilyTyping.mp3" loop

        "one minute passed..."
        "two minutes passed..."

        show emily general close at left
        with dissolve

        stop sound

        e "I think I got it, look."

        if language == 'js':
            show lps sol emily expand js at topright
            with dissolve
        
        if language == 'python':
            show lps sol emily expand py at topright
            with dissolve
        
        if language == 'pseudo':
            show lps sol emily expand pseudo at topright
            with dissolve

        m "Wow this is fast."
        e "Haha. I type fast."
        
        menu:
            "Mark the solution now":
                jump markEmilyLps
            "Dig deeper into the solution":
                m "So what's the time compexity here?"
                e "O(n^2)."
                m "Okay. Nice."
                menu:
                    "Ask for a faster solution":
                        m "Do you think you can make it faster? O(n^2) could be good, it could be slow as well."
                        
                        show emily concentrate close at left
                        with dissolve

                        e "I can't."
                        m "Oh, that's pretty clear cut."
                        
                        show emily general close at left
                        with dissolve

                        jump markEmilyLps
                    "Mark the current solution":
                        jump markEmilyLps
    

    if isAdam:
        a "Hmm, again, okay, I see."
        a "Give me some time to think it through."

        m "Sure."

        show adam worry close at left
        with dissolve

        "one minute passed..."
        "two minutes passed..."
        "three minutes passed..."

        show adam smile close at left
        with dissolve

        a "Okay, I got two ideas."
        a "First one is using dynamic programming, with a time complexity of O(n^2)."
        a "The second one is an algorithm called Manacher's Algorithm, with a time complexity of O(n)."
        a "However, I don't think I can implement the Manacher's algorithm now. If you want I can show you a reference."

        m "Oh, it's okay, could you just implement the dynamic programming one?"

        show adam general close at left
        with dissolve

        a "Hmm, okay."

        play sound "/audio/adamTyping.wav" loop

        "one minute passed..."
        "two minutes passed..."
        "three minutes passed..."
        "four minutes passed..."

        show adam focus close at left
        with dissolve

        "five minutes passed..."
        "six minutes passed..."

        show adam general close at left
        with dissolve

        stop sound

        a "Okay, finally, check it out."

        if language == 'js':
            show lps sol adam js at topright
            with dissolve
        
        if language == 'python':
            show lps sol adam py at topright
            with dissolve
        
        if language == 'pseudo':
            show lps sol adam pseudo at topright
            with dissolve

        a "I think this works. Though it can't be executed on the white board."
        m "Yes, haha, true. What's the time complexity again?"
        a "O(n^2)."
        m "Okay."

        show adam smile close at left
        with dissolve

        jump markAdamLps


