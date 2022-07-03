default mark = 'good'
label fizzbuzzcore:
    show fizzbuzz at topleft
    m "Check it out."

    if isJoe:

        ""

        j "Hmmmmm... yes, fizzbuzz..."
        j "Give me a minute..."

        "one minute passed..."
        "two minutes passed..."

        show joe struggling close at left
        with dissolve

        "three minutes passed..."

        j "Hmmmmm..."

        "four minutes passed..."
        "five minutes passed..."

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

        "one minute passed..."

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
