# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
init:
    $ mcname1 = "MC"
    $ mcname2 = " "
    $ mcnamefull = " "
    $ m = DynamicCharacter("mcname1", color="#1B0087")
    $ best_girl = DynamicCharacter("Best Girl", color="#03F700")

define b = Character('BroC', color="#7F0020")

# The game starts here.
label start:
    #scene bg conflict
    #with dissolve
    #play music "noquarterbattle.mp3"

    #window show

    "Figured it would turn out this way."
    #show BroC scared
    b "Bro, you okay?"
    "Wasn't one for taking hits, that was Bro's job."
    "Did it anyways."
    extend"\nYou only live once, right?"
    b "Dammit, man, speak to me!"
    b "Say something, anything!"
    m "Thanks..."
    #show BroC angry
    b "No!"
    extend "\nNot yet, no!"
    m "Take care of her- if I can't..."
    #show BroC furious
    b "Shut the hell up!"
    extend "\nYou're talking like you're gonna die, and I WON'T let that happen!"
    #hide BroC
    "He picks me up like I'm a rag doll."
    "Too much blood."
    extend "\nCan't open my eyes, barely consious."
    #show BroC determined
    b "Ranger!\nTake care of that creep- hold him off until I get back!"
    #hide BroC
    "Can't hear the response. \nToo much static in my head."
    "After a few seconds, I pass out."
    
    #show bg darkness
    #with dissolve
    #play music "contemplation.mp3"
    "Something out of a book, right?"
    "Taking a blow meant for a true love."
    "But we're Hunters."
    extend "\nTrue love only comes in tragedy flavor around here."
    #stop music fadeout 1.0
    
    #$ renpy.movie_cutscene("INTRO_MOVIE.mpg")
    
    #show bg beacon_view
    #with dissolve
    #play music "contemplation.mp3"
    "This story begins at Beacon."
    extend "\nAcademy for Hunters and Huntresses, like me."
    #show BroC cheerful
    "And my friends, like Brock."
    "He's stuck with me through thick and thin."
    "Even though I'm technically a better student and arguably a better fighter, I don't know where I'd be without him."
    #hide BroC
    jump hospital
 
label hospital:
    #show bg hospital_room
    #with dissolve
    "But we're not at Beacon, not now."
    "Right now, I'm in a hospital."
    "Flat on my back, a drip in my arm, trying not to croak before my girlfriend shows up."
    "Some way to spend a day, huh?"
    #stop music fadeout 1.0
    "Someone enters, and my heart jumps."
    #show BroC determined
    b "Bro."
    "He's not happy."
    m "..."
    b "Don't give me the silent treatment, Bro."
    b "This is more than a bad scrape. \nTell me what's up."
    "It is, but I'm not about to tell him that."
    m "I'm fine."
    "He sees through it immediately."
    b "Bullshit."
    extend "\nThat's bullshit, and you know it."
    #show BroC angry
    b "Bro."
    b "I need you to be honest with me."
    #show BroC sad
    b "What's up with you?"
    extend "\nThis isn't like you."
    menu:
        "I'm just tired, Bro. Honestly.":
            $ mood1 = "exhausted" #For later flags
            m "I can barely lift my arm."
            jump exhausted
        "Some 'hero' I am, right?":
            $ mood1 = "noplaceforahero"
            m "Can't even protect one girl without getting half-killed."
            jump sulk
        "Bro... I know you want to help, but...":
            $ mood1 = "personalproblems"
            m "This is something I have to do myself."
            jump resolve

label exhausted:
    "My arm is killing me."
    "A good tenth of my blood likely hasn't been replaced yet."
    "I just can't talk to him right now."
    m "I want to talk to you, but I really can't."
    extend "\nI'm just too tired."
    "He looks at me, sadly."
    "Looking over me, he realizes just how grevious my wounds really are."
    m "Please, I want to get out there as much as you do- I just can't."
    "Soon, Bro gives me a nod of understanding."
    b "Okay, bro, I just want you to be honest with yourself."
    b "You know what happened to me when I wasn't."
    #show BroC happy
    b "You taught me one thing, at least."
    "I snicker."
    m "More than you think."
    #show BroC teasing
    b "Hey, I learned the alphabet all on my own, and I can count good."
    "Smiling feels good."
    "I would be laughing if I didn't think it would cave in my chest."
     #hide BroC
    jump guest

label sulk:
    "Fat lot of good I am as a meat shield."
    "Couldn't even take one good hit."
    m "At least she got out alright."
    #show BroC furious
    "Before I can say anything, Bro gives me a death glare like nothing I've seen before."
    b "W-What?"
    b "Bro, you put yourself on the line to save her LIFE. That's not something people just DO."
    "I shake my head in confusion."
    m "She's my girlfriend, of course it is."
    "His fists clench."
    b "God, you cannot be serious right now."
    #show BroC determined
    b "There's no way you're our leader- that you do the things you do, and you're not a hero."
    m "I'm just doing what I'm supposed to."
    b "Yeah, well, guess what?"
    extend "\nThat's what heroes do."
    b "The fact that it's not a big deal just proves my point."
    #show BroC teasing
    b "You know what, forget it."
    b "I'm going to beat some sense into you the second you get out."
     #hide BroC
    jump guest

label resolve:
    "I try to shake the weariness off."
    "There are some things a man's just gotta do."
    m "You know the feeling better than I do- this is my fight, in a way."
    #show BroC teasing
    "Bro rolls his eyes."
    b "Come on, man, we're a team."
    b "You know what happened when I tried to go full macho."
    "I sigh a bit and lie back."
    m "Yeah, well, you can't knit my bones any faster than they are already."
    "He puts his fist into the other palm."
    b "Wanna bet?"
    #show BroC determined
    b "For real though, you can't try to take everything on by yourself."
    m "I know, but it was my decision to get ragdolled, and now I have to deal with it."
    #show BroC teasing
    "That sours him just a bit."
    b "You weren't the one who dragged your limp ass back to safety, you know."
    m "Sorry, but at least I don't need to lose weight."
    b "I'm plenty in shape, I'll have you know."
    b "I'd prove it by flattening you if you weren't already, you know..."
    #hide BroC
    jump guest

label guest:
    #show bg best_girl_entrance
    #with dissolve
    "Of course, I wasn't expecting my next guest, even if I was happy to see her."
    $ best_girl = "Penny"
    #show Penny happy at right
    best_girl "Salutations!"
    #show BroC confused at left
    b "Huh?"
    best_girl "It means, 'Greetings!'"
    #show Penny disappointed at right
    extend "\nHonestly, even I know that much, and I was manufactured."
    b "No, I mean..."
    best_girl "...Yes?"
    b "Aren't you, you know, dead?"
    #show Penny thinking at right
    best_girl "That's a matter of interpretation."
    b "I'm sure."
    #show Penny determined at right
    best_girl "Anyways, I'm just here to test to see if the MC can be renamed."
    b "Who can what now?"
    #show Penny angry at left
    best_girl "Comic relief should stay silent during serious scenes."
    #show BroC angry at left
    b "Hey! I'm practically a deuterotagonist at this point!"
    #show Penny happy at right
    best_girl "Now, input your name, if you would?"
    $ mcname1 = renpy.input("What is your first name?")
    $ mcname2 = renpy.input("What is your last name?")
    $ mcnamefull = mcname1+" "+mcname2
    m "My name is %(mcname1)s. %(mcname1)s %(mcname2)s."
    best_girl "Excellent! this ends this segment!"
    b "Now wait just a minute-"
    return
