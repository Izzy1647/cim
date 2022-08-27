style centered_style:
    xalign 0.5
    yalign 0.5


screen report(candidate="Hi"):
    frame:
        background Solid( "#aaaba6e0" )
        xalign 0.5
        yalign 0.3
        xpadding 20
        ypadding 20
        vbox:
            hbox:
                xalign 0.5
                text "[candidate]'s Overview\n" color "000000"

            if candidate == 'Joe':
                hbox:
                    text "Mark on fizzbuzz: " color "000000"
                    if fizzbuzzMarkJoe != -1:
                        text "[fizzbuzzMarkJoe]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                hbox:
                    text "Mark on two sum: " color "000000"
                    if twosumMarkJoe != -1:
                        text "[fizzbuzzMarkJoe]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                hbox:
                    text "Mark on longest palindromic substring: " color "000000"
                    if lpsMarkJoe != -1:
                        text "[lpsMarkJoe]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                vbox:
                    text "\nYour feedback on Joe" color "000000"
                    hbox:
                        text "Positive:" color "000000"
                        text joeFeedbackPositive color "000000"
                    hbox:
                        text "Negative:" color "000000"
                        text joeFeedbackNegative color "000000"


            if candidate == 'Emily':
                hbox:
                    text "Mark on fizzbuzz: " color "000000"
                    if fizzbuzzMarkEmily != -1:
                        text "[fizzbuzzMarkEmily]" color "000000"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on two sum: " color "000000"
                    if twosumMarkEmily != -1:
                        text "[fizzbuzzMarkEmily]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                hbox:
                    text "Mark on longest palindromic substring: " color "000000"
                    if lpsMarkEmily != -1:
                        text "[lpsMarkEmily]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                vbox:
                    text "\nYour feedback on Emily" color "000000"
                    hbox:
                        text "Positive:" color "000000"
                        text emilyFeedbackPositive color "000000"
                    hbox:
                        text "Negative:" color "000000"
                        text emilyFeedbackNegative color "000000"

        
            if candidate == 'Adam':
                hbox:
                    text "Mark on fizzbuzz: " color "000000"
                    if fizzbuzzMarkAdam != -1:
                        text "[fizzbuzzMarkAdam]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                hbox:
                    text "Mark on two sum: " color "000000"
                    if twosumMarkAdam != -1:
                        text "[fizzbuzzMarkAdam]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                hbox:
                    text "Mark on longest palindromic substring: " color "000000"
                    if lpsMarkAdam != -1:
                        text "[lpsMarkAdam]" color "000000"
                    else:
                        text "Non-taken" color "000000"
                vbox:
                    text "\nYour feedback on Adam" color "000000"
                    hbox:
                        text "Positive:" color "000000"
                        text adamFeedbackPositive color "000000"
                    hbox:
                        text "Negative:" color "000000"
                        text adamFeedbackNegative color "000000"        

            
            hbox:
                xalign 0.5
                spacing 40
                textbutton "Back to menu":
                    text_color "1C4596"
                    ypadding 20
                    action [Hide(screen='report'), Jump('candidates_menu')]
                textbutton "Make your choice":
                    text_color "1C4596"
                    ypadding 20
                    action [Hide(screen='report'), Jump('decision')]
                    

        

    


screen vbox_screen(buttons=["1", "2"], text_size=30):
    vbox:
        xalign 0.2
        yalign 0.2
        spacing 5
        for button in buttons:
            textbutton button:
                action NullAction
                text_size text_size


screen grid_screen(buttons=["1", "2", "3"], text_size=30):
    grid 2 len(buttons)/2+1:
        spacing 5
        xalign 0.8
        yalign 0.8

        for button in buttons:
            textbutton button:
                action NullAction
                text_size text_size