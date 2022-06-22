default nums = [2, 7, 11, 15]
default output1 = [0, 1]
default output2 = [1, 0]

label twosum:
    m "Let's take a look."
    show twosum at topleft
    ""
    m "Say nums = [nums] and target = 9, your output should be either [output1] or [output2]."
    m "Does it make sense to you?"

    if isJoe:
        j "Umm... yes, I think I get it."
        j "Well..."
        j "My thinking is that, um, I can loop over every number..."
        j "Then, umm..., loop again over every number after it..."
        j "And check if there's a pair that meets the criteria."
        
        m "Okay, so can you give me an implementation?"

        j "Sure... give me a minute."

        show joe focus close at left
        with dissolve

        "one minute passed..."
        "two minute passed..."

        show joe general close at left
        with dissolve

        j "Hmm, here it is."

        show twosum sol joe bf at topright
        with dissolve

        j "It's like a, umm..., very straight forward solution I think."

        menu:
            "Mark the solution right now":
                menu:
                    "Mark the solution :)"
                    "Very good":
                        $ twosumMarkJoe = 5
                    "Good":
                        $ twosumMarkJoe = 4
                    "Okay":
                        $ twosumMarkJoe = 3
                    "Poor":
                        $ twosumMarkJoe = 2
                    "Very poor":
                        $ twosumMarkJoe = 1
                
                jump postTwosum

            "Dig deeper into the solution":
                jump deeperWithJoe
        
        label deeperWithJoe:
            "deeper acszds"
        
        
        
        "two sum"