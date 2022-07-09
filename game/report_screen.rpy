style centered_style:
    xalign 0.5
    yalign 0.5


screen report(candidate="Hi"):
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 20
        ypadding 20
        vbox:
            hbox:
                # style "centered_style"
                text "[candidate]'s Report: \n"
            if candidate == 'Joe':
                hbox:
                    text "Mark on Fizzbuzz: "
                    if fizzbuzzMarkJoe != -1:
                        text "[fizzbuzzMarkJoe]"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on Twosum: "
                    if twosumMarkJoe != -1:
                        text "[fizzbuzzMarkJoe]"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on longest palindromic substring: "
                    if lpsMarkJoe != -1:
                        text "[lpsMarkJoe]"
                    else:
                        text "Non-taken"
                vbox:
                    text "\nYour feedback on Joe:"
                    hbox:
                        text "Positive:"
                        text joeFeedbackPositive
                    hbox:
                        text "Negative:"
                        text joeFeedbackNegative


            if candidate == 'Emily':
                hbox:
                    text "Mark on Fizzbuzz: "
                    if fizzbuzzMarkEmily != -1:
                        text "[fizzbuzzMarkEmily]"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on Twosum: "
                    if twosumMarkEmily != -1:
                        text "[fizzbuzzMarkEmily]"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on longest palindromic substring: "
                    if lpsMarkEmily != -1:
                        text "[lpsMarkEmily]"
                    else:
                        text "Non-taken"
                vbox:
                    text "\nYour feedback on Emily:"
                    hbox:
                        text "Positive:"
                        text emilyFeedbackPositive
                    hbox:
                        text "Negative:"
                        text emilyFeedbackNegative

            

            if candidate == 'Adam':
                hbox:
                    text "Mark on Fizzbuzz: "
                    if fizzbuzzMarkAdam != -1:
                        text "[fizzbuzzMarkAdam]"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on Twosum: "
                    if twosumMarkAdam != -1:
                        text "[fizzbuzzMarkAdam]"
                    else:
                        text "Non-taken"
                hbox:
                    text "Mark on longest palindromic substring: "
                    if lpsMarkAdam != -1:
                        text "[lpsMarkAdam]"
                    else:
                        text "Non-taken"
                vbox:
                    text "\nYour feedback on Adam:"
                    hbox:
                        text "Positive:"
                        text adamFeedbackPositive
                    hbox:
                        text "Negative:"
                        text adamFeedbackNegative
                    
                    

        

    


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