label emilyStory:
    scene black
    with dissolve

    "Emily's story behind the interview..."

    scene bg campus
    with fadehold

    play music "/audio/emilyBgmPositive.mp3" 

    "Emily got her bachelor degree in mechanical engineering."

    scene bg emily coding
    with fadehold

    "Slightly before graduation, she decided to teach herself programming, as she heard that IT salaries are very decent."

    "But how?"

    scene bg academic
    with fadehold

    "Emily did some research."
    "One way is to go through every course that a CS student needs to take, based on the {a=http://catalog.mit.edu/degree-charts/computer-science-engineering-course-6-3/}CS undergraduate outline{/a} available on internet."
    "This includes courses like Fundamentals of Programming, Computer Systems Engineering (CI-M), Software Performance Engineering, Dynamic Computer Language Engineering, etc."
    "Looks pretty deep and time consuming..."

    "So emily chose the second way."

    scene bg coding interview uni at topleft
    with fadehold

    "She directly prepared for the interviews: created an account on Leetcode, solved these questions that are frequently asked in interviews, as many as possible."
    
    scene emily contribution graph at top 
    with fadehold

    "She worked very hard on interview coding questions. For these over complex for her, she even memorize the solution."

    scene bg code
    with fadehold

    "This is how she manage to write code so fast and so confident during the interview: an extremely well preparer."

    stop music fadeout 4.0

    return


label emilyInWork:
    play music '/audio/emilyWorkBgm.mp3'

    scene bg workplace
    with fadehold

    "Without taking traditional CS courses, Emily lacks understanding in both external and internal quality of software."
    "Emily doesn't have any idea on how to design and write unit test cases, so she always turn to you for help."
    "However, as you are not the author of the code, you have to first spend some time on understanding the logic, then design the unit tests."
    "It makes the whole process more time-consuming."

    scene bg emily code
    with fadehold

    "Also, Emily has a very weak sense of clean code, making her code heavy, repetitive, and hard to read or understand."
    "Emily always choose the easy way of implementing, but not the elegant way, introducing lots of technical debt into the codebase."
    "Huge amount of time are spent for reviewing and refactoring."

    "As a matter of fact, these abilities are very hard to evaluate in coding interviews."

    stop music fadeout 2.0

    return

    
