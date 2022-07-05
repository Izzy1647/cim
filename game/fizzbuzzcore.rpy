default mark = 'good'
label fizzbuzzcore:
    show fizzbuzz at topleft
    m "Check it out."

    if isJoe:

        ""

        j "Hmmmmm... yes, fizzbuzz..."
        j "Give me a minute..."

        show joe focus close at left
        with dissolve

        play sound "/audio/joeTyping.mp3" loop

        "one minute passed..."
        "two minutes passed..."

        show joe struggling close at left
        with dissolve

        "three minutes passed..."

        j "Hmmmmm..."

        "four minutes passed..."
        "five minutes passed..."

        stop sound

        show joe excited close at left
        with dissolve

        j "Yes! I got it! Check it out..."

        if language == 'js':
            show fizzbuzz sol joe js at topright
            with dissolve

        j "I assume it's a correct solution."

        "Now it's your time to mark Joe's solution."

        menu:
            "Mark Joe's solution :)"

            "Very good":
                $ fizzbuzzMarkJoe = 5
                $ mark = 'very good'
            "Good":
                $ fizzbuzzMarkJoe = 4
                $ mark = 'good'
            "Okay":
                $ fizzbuzzMarkJoe = 3
                $ mark = 'okay'
            "Poor":
                $ fizzbuzzMarkJoe = 2
                $ mark = 'poor'
            "Very poor":
                $ fizzbuzzMarkJoe = 1
                $ mark = 'very poor'
        
        # hide fizzbuzz
        hide fizzbuzz sol joe js
        call postfizzbuzz(mark=mark, candidate='Joe')

    
    if isEmily:
        show emily easy close at left
        with dissolve

        e "Okay, gimme one minute."

        play sound "/audio/emilyTyping.mp3" loop

        "one minute passed..."

        stop sound

        if language == 'js':
            show fizzbuzz sol emily js at topright
            with dissolve

        e "Here it is."

        show emily general close at left
        with dissolve

        menu:
            "Mark Emily's solution on fizzbuzz"

            "Very good":
                $ fizzbuzzMarkEmily = 5
                $ mark = 'very good'
            "Good":
                $ fizzbuzzMarkEmily = 4
                $ mark = 'good'
            "Okay":
                $ fizzbuzzMarkEmily = 3
                $ mark = 'okay'
            "Poor":
                $ fizzbuzzMarkEmily = 2
                $ mark = 'poor'
            "Very poor":
                $ fizzbuzzMarkEmily = 1
                $ mark = 'very poor'
        
        hide fizzbuzz sol emily js

        call postfizzbuzz(mark=mark, candidate='Emily')

    if isAdam:
        show adam focus close at left
        with dissolve
        a "Okay, I got it. Seems pretty straight forward with one loop, with a linear time complexity."
        m "Yes, yes."
        a "So do I write down the code now?"
        m "Yes, please."
        a "Okay."

        show adam worry close at left
        with dissolve

        play sound "/audio/adamTyping.wav" loop
        
        "one minute passed..."
        "two minutes passed..."
        "three minutes passed..."

        stop sound

        show adam general close at left
        with dissolve

        a "Okay, this is what I got, so far."
        
        if language == 'js':
            show fizzbuzz sol adam wrong js at topright
            with dissolve

        ""
        menu:
            "Fine, mark the solution now":
                m "Okay."
                jump markAdamFizzbuzz
                

            "Seems wrong":
                m "Hmm, do you think there's something wrong with your code?"

                show adam worry close at left
                with dissolve

                a "Let me check."

                "one minute passed..."

                a "Oh, I see, mod 15 should be the first. Sorry."

                m "Yes, don't worry. It's just a tiny mistake."

                show adam general close at left
                with dissolve

                ""
                
                jump markAdamFizzbuzz

label markAdamFizzbuzz:
    menu:
        "Mark Adam's solution on fizzbuzz:"

        "Very good":
            $ fizzbuzzMarkAdam = 5
            $ mark = 'very good'
        "Good":
            $ fizzbuzzMarkAdam = 4
            $ mark = 'good'
        "Okay":
            $ fizzbuzzMarkAdam = 3
            $ mark = 'okay'
        "Poor":
            $ fizzbuzzMarkAdam = 2
            $ mark = 'poor'
        "Very poor":
            $ fizzbuzzMarkAdam = 1
            $ mark = 'very poor'
    
    hide fizzbuzz sol adam wrong js
    hide fizzbuzz sol adam wrong py
    hide fizzbuzz sol adam wrong pseudo


    call postfizzbuzz(mark=mark, candidate='Adam')
