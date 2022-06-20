label fizzbuzzcore:
    if isJoe:
        m "Check it out"

        show fizzbuzz at topleft

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
            "Good":
                $ fizzbuzzMarkJoe = 4
            "Okay":
                $ fizzbuzzMarkJoe = 3
            "Poor":
                $ fizzbuzzMarkJoe = 2
            "Very poor":
                $ fizzbuzzMarkJoe = 1
        
        # hide fizzbuzz
        hide fizzbuzz sol joe
    
    jump postfizzbuzz
