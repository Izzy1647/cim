default mark = 'good'
label fizzbuzzcore:
    show fizzbuzz at topleft
    
    if isJoe:
        m "Check it out"

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

        show fizzbuzz sol joe at topright
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
        hide fizzbuzz sol joe
    
    call postfizzbuzz(mark=mark)
