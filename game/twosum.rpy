default nums = [2, 7, 11, 15]
default output1 = [0, 1]
default output2 = [1, 0]

label markJoeTwoSum:
    menu:
        "Mark joe's performance :)"
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

        
label deeperWithJoe:
    m "What's the time complexity of your implementation?"
    j "Umm... so there are two loops..."
    j "I think it's O(n^2)."
    menu:
        "Ask for an optimization":
            m "Do you think you can lower the time complexity?"

            show joe struggling close at left
            with dissolve

            j "Hmm...."
            j "Well... I think I need some time here."
            m "It's fine. Take your time."
            j "OKay..."

            show joe general close at left
            with dissolve

            "one minute passed..."
            "two minutes passed..."

            show joe focus close at left
            with dissolve

            j "So..."
            j "I think maybe I can use a hash map."
            j "Well... how do I put this..."
            j "I think only one loop is needed with a hash map."
            j "Like, I can save the 'wanted' value for currrent value..."
            j "And... if later I find the 'wanted' value I can just return the pair."
            j "Is it clear... or can I just code it out and show you..."

            m "Yes, and yes, go ahead please."

            j "Sure."

            show joe general close at left
            with dissolve

            "one minute passed..."
            "two minutes passed..."
            "three minutes passed..."

            show joe excited close at left
            with dissolve

            j "I think I got it... Check it out."

            show twosum sol joe hashmap at topright
            with dissolve

            j "So the time complexity is..." 
            j "Ummm..."
            j "O(n), I think."

            show joe general close at left
            with dissolve

            "Now it's your time to mark Joe's performance."

            jump markJoeTwoSum

        "Mark Joe's performance now":
            jump markJoeTwoSum
       

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

        show joe general close at left
        with dissolve

        j "Hmm, here it is."

        show twosum sol joe bf at topright
        with dissolve

        j "It's like a, umm..., very straight forward solution I think."

        menu:
            "Mark the solution right now":
                jump markJoeTwoSum

            "Dig deeper into the solution":
                jump deeperWithJoe
