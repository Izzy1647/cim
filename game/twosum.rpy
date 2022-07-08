default nums = [2, 7, 11, 15]
default output1 = [0, 1]
default output2 = [1, 0]

label markAdamTwosum:
    menu:
        "Mark Adam's performance on twosum"
        "Very good":
            $ twosumMarkAdam = 5
        "Good":
            $ twosumMarkAdam = 4
        "Okay":
            $ twosumMarkAdam = 3
        "Poor":
            $ twosumMarkAdam = 2
        "Very poor":
            $ twosumMarkAdam = 1

    hide twosum sol adam wrong js
    hide twosum sol adam wrong py
    hide twosum sol adam wrong pseudo

    with dissolve
                
    jump postTwosum

label markJoeTwoSum:
    menu:
        "Mark Joe's performance on twosum"
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

    hide twosum joe sol js
    hide twosum joe sol py
    hide twosum joe sol pseudo

    with dissolve
                
    jump postTwosum

label markEmilyTwosum:
    menu:
        "Mark emily's performance on twosum"
        "Very good":
            $ twosumMarkEmily = 5
        "Good":
            $ twosumMarkEmily = 4
        "Okay":
            $ twosumMarkEmily = 3
        "Poor":
            $ twosumMarkEmily = 2
        "Very poor":
            $ twosumMarkEmily = 1
    
    hide twosum sol emily js
    hide twosum sol emily py
    hide twosum sol emily pseudo

    jump postTwosum
        
label twosumDeeperWithJoe:
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

            play sound "/audio/joeTyping.mp3" loop

            "one minute passed..."
            "two minutes passed..."
            "three minutes passed..."

            stop sound

            show joe excited close at left
            with dissolve

            j "I think I got it... Check it out."

            if language == 'js':
                show twosum sol joe hashmap js at topright
                with dissolve
            
            if language == 'python':
                show twosum sol joe hashmap py at topright
                with dissolve

            if language == 'pseudo':
                show twosum sol joe hashmap pseudo at topright
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
       
label twosumDeeperWithEmily:
    m "Looks fine. So what's the time complexity here?"
    e "O(n)."
    m "Yeah, that's pretty much it. Good job."
    jump markEmilyTwosum


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

        play sound "/audio/joeTyping.mp3" loop

        "one minute passed..."

        show joe general close at left
        with dissolve

        stop sound

        j "Hmm, here it is."

        if language == 'js':
            show twosum sol joe bf js at topright
            with dissolve

        if language == 'python':
            show twosum sol joe bf py at topright
            with dissolve

        if language == 'pseudo':
            show twosum sol joe bf pseudo at topright
            with dissolve

        j "It's like a, umm..., very straight forward solution I think."

        menu:
            "Mark the solution right now":
                jump markJoeTwoSum

            "Dig deeper into the solution":
                jump twosumDeeperWithJoe

    if isEmily:
        show emily relief close at left
        with dissolve

        e "Yes!"
        m "Okay. So can you sort it out?"
        e "Yes!"
        m "Okay!"

        play sound "/audio/emilyTyping.mp3" loop

        "one minute passed..."
        "two minutes passed..."

        show emily eyes closed close at left
        with dissolve

        "three minutes passed..."

        show emily general close at left
        with dissolve

        stop sound

        e "Here, check it out!"

        if language == 'js':
            show twosum sol emily js at topright
            with dissolve

        if language == 'python':
            show twosum sol emily py at topright
            with dissolve

        if language == 'pseudo':
            show twosum sol emily pseudo at topright
            with dissolve

        ""

        menu:
            "Mark the solution right now":
                jump markEmilyTwosum

            "Dig deeper into the solution":
                jump twosumDeeperWithEmily
    
    if isAdam:
        a "Yes it does."
        a "Well give me some time to think through it."

        m "Sure."

        show adam worry close at left
        with dissolve

        "one minute passed..."
        "two minutes passed..."

        show adam general close at left
        with dissolve

        a "Okay, so I think one possible way is to brufal force it, which would be O(n^2) in time complexity."
        a "Another way is an O(n) solution with a hash map, a higher space complexity then brutal force."

        m "Yes, makes sense. Can you implement one of them?"

        a "Okay, I will do the hash map one."

        m "Thank you."

        show adam focus close at left
        with dissolve

        play sound "/audio/adamTyping.wav" loop

        "one minute passed..."
        "two minutes passed..."
        "three minutes passed..."
        "four minuted passed..."
        "five minutes passed..."

        stop sound

        show adam general close at left
        with dissolve

        a "Check it out."

        if language == 'js':
            show twosum sol adam wrong js at topright
            with dissolve

        if language == 'python':
            show twosum sol adam wrong py at topright
            with dissolve

        if language == 'pseudo':
            show twosum sol adam wrong pseudo at topright
            with dissolve
        
        menu:
            "Fine, mark Adam's solution on twosum":
                jump markAdamTwosum
            "Seems incorrect, dig deeper":
                m "Well, I think this works, but there, again, is a slight problem in it."

                show adam worry close at left
                with dissolve

                a "Let me look into it, sorry."
                m "Yeah, yeah, it's just that you need to return the index, not the number itself."

                show adam general close at left
                with dissolve
                
                a "Ah, yes. Then I will store the index instead of the value in the hash map."
                m "Cool."

                jump markAdamTwosum


        