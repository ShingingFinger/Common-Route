# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define h = Character('Hugh', color="#c8ffc8")
define c = Character('Radcliff', color="#c8ffc8") #cliff
define r = Character('Ruby', color="#c8ffc8")
define w = Character('Weiss', color="#c8ffc8")
define b = Character('Blake', color="#c8ffc8")
define y = Character('Yang', color="#c8ffc8")

# The game starts here.
label rubyrose:
#A bit of introspection, introduction to the MC
#A bit of talking with Bro
#Glimpses at others
#Seems too early, impressions at most

    "It's funny how, even though this is the first time I've ever been on an airship, I'm not interested in the scenery."
    "Too many things have been running through my mind- it's just not happening."
    "I can't focus."
    "It's just, I'm wondering, am I ready for this?"
    "Beacon is supposed to be an academy for the best of the best, right?"
    "But... I'm not."
    "Not by a long shot."
    "Not after my big mistake."
    "Everyone has at least one, that screw-up itching at the back of your mind, never leaving."
    "For me, it nearly cost me my life- and the lives of my whole village."
    "I thought I was being cool- but I was just being a glory hound."
    "One of the village's kids had lost his puppy, and he was in a real mood about it."
    "Trying to play hero, I went out to hunt it down, despite not being able to handle any Grimm I ran into."
    "But I was too caught up in what everyone would think when I got back."
    "Stupid, stupid, STUPID."
    "I somehow managed to track the dog down- just a little late."
    "Beowolves, the archetypical Grimm."
    "People always ask me how many of them there were. My answer?"
    "Too many. Just... Too many."
    "The dog wouldn't have brought them home- but my presence was almost guarenteed to lead them to where I lived."
    "-After they had finished me off, that is."
    "No escape plan, no weapons, outnumbered to the point to where if I had them they would have just delayed the inevitable."
    "In the short time I had left, I came to accept my death and the doom of my family."
    "How could I even have thought to call myself a Hunter?"
    "Hunters were supposed to save lives, not throw them away."
    "I even crawled up in a ball, for maximum pathetic points."
    "But before I could get clawed in half, I heard the glorious sound of a gunshot blowing the Grimm's head off."
    "I looked up to see Grimm- the harvengers of death- in a panic."
    "To be honest, that moment is probably what made me insist on a firearm expansion to my tonfas,when I got them."
    "Enter my master, who proceeded to save my sorry tailbone by butchering about a quarter of the Grimm and leading away the rest."
    "To be honest, I didn't believe anyone could have survived until Master came back- and promptly dragged me back home."
    "I didn't get out of my room for a month, but whe I did, sure enough, I was approached with the offer to become a Hunter."
    "The rest, as they say-"
    $ renpy.play('punch.wav')
            with hpunch
    h "-OW!"
    "My back suddenly begins to sting, as a cheerful figure slides up next to me with a smirk."
    c "Come on, Hugh. You can take more than a lovetap, can't ya?"
    c "Otherwise, you can't be here. Manly men only."
    h "Thanks, Radcliff. You sure know how to make a guy feel worse."
    "He rolls his eyes as I try to correct my spine's alignment."
    c "Oh, boo hoo. Come on, Mister Constant Raincloud. Just look outside!"
    "I take a second to admire the view, and he throws an arm over my shoulder."
    c "We're going to Beacon! THE Beacon. You and me!"
    h "Had to sneak aboard, did you?"
    c "I'll have you know I graduated top member of our class. Not hard, given the only other one was you."
    "I place a hand over my heart and pretend to slump back slightly."
    h "Oh, no, however shall I recover from such a grevious wound?"
    c "I beeseech thee to surrender, else I strike thee down!"
    "We laugh for a bit, enjoying each other's company."
    "Radcliff- he's been my most constant friend."
    "Some would call us rivals, but we're so different in style it's pretty hard to compare us, much less make us compete."
    "I had been studying under Master a little while before he joined up with us, but he took like a fish to water."
    "You name it, he's good at it- tracking, book-work, fighting, feats of strength..."
    "...Well, so long as 'it' has to do with Hunting."
    "Two years and he still can't pitch a tent or cook a meal that actually fits the definition."
    "That and he claims to be good at flirting while putting his foot so deep in his mouth it takes two people to pull it out."
    "We really became friends after that time we defended the camp from a Grimm horde for nearly an hour while Master was gone."
    "Of course, given that Grimm dissolve on destruction, we couldn't ACTUALLY prove jack, but he knows, and I know."

    "We end up taking a glance around the room, and someone catches Radcliff's eye."
    c "Dude, check out hotpants over there. I mean, DAMN."
    "He whistles softly."
    c "I wouldn't mind being hunted by her, if you get my drift."
    h "You know if she hears you, you're getting the third-rate trip down, right?"
    c "Wow, do you literally have no sex drive?"
    c "Come on, man. If I do one thing for you this semester, it's get you a girlfriend."
    h "You couldn't get a girlfriend for yourself, much less for me."
    "He seems slightly hurt at this, which suprises me a bit- normally, it'd be considered "
    
    "Radcliff and Hugh look around at the other future hunters present."
    
    c "I take a good long look at Yang, who I point out to Hugh and refer to as 'hotpants chick'."
    
    h "I point out that Radcliff's behavior will likely be rebuffed if noticed."
    
    c "I grumble that Hugh has no sex drive and will never get a girlfriend in a fashion ironic given the nature of the game."
    
    h "I admit that it is true I've never had a girlfriend, but this is because of my reserved nature rather than personal capability to do so."
    h "Also, Radcliff is a jackass for breaking the fourth wall."
    
    "Faunus civil rights protest TV broadcast here. The situation presented makes both young men very uncomfortable and stop talking."
    "Soon, however, it is interrupted by Gynda Goodwitch's announcement."
    
    c "After the announcement ends, I imitate Glynda's serious tone in a mocking fashion. Insert Spider-Man reference here."
   
    h "I make a cynical but joking comment about the nature of Beacon, before informing Radcliff of the incredible view."
    
    "A CG sky view of Beacon appears, staying on the screen for the next few comments."
    
    c "I wonder out loud about how the school will actually be, and confess to Hugh that I'm personally nervous."
    c "This helps display my honest but blunt nature."
    
    h "I nod, but don't respond verbally, internalizing my fears and signalling that confronting my hesitant nature is part of my future character development."
    
    "A brief interaction between the timid Nixie and strict Edna catches the boys' attentions."
    "After Nixie apologizes, she fixes her hair and smiles when she sees Radcliff."
    
    c "Being as dense as the stone I'm named after, I assume she's acting based on Hugh's attention rather than mine."
    
    h "I have my suspicions that Radcliff is wrong, but keep them to myself."
    
    "The scene ends with the airship reaching its destination and both boys passing by Jaune as he upheaves whatever personal dignity he has left into the trash can outside the airship."
    
    jump shiningbeacon

label shiningbeacon:
    
    "The two boys view Beacon in earnest while trying to ignore Ruby's sperging out about weapons."
    "However, they are soon knocked out of their wonder by the explosion produced by Ruby."
    
    h "Surprise and alarm!"
    
    c "Excuse to engage weapon!"

    "Radcliff displays his signature maul, a huge, simplistic weapon designed to deal tons of damage and reave through Grimm."
    
    r "Excuse to fangirl about the axe!"
    
    c "Confused request that she leave me and my weapon alone!"
    
    r "Pressing questions about the make, design, and name of the maul, expressed with a lack of regard for personal space or self-restraint!"
    
    b "Display of knowledge about the SDC..."
    
    w "Expression of gratefulness for recognition!"
    
    b "...Followed by comment about it being a Snidley-Whiplash-level evil corporation."
    
    w "Indignation, followed by demand that Hugh state an opinion on the matter!"
    
    h "Flat reaction of stunned disbelief."
    
    r "Continued harassment of Radcliff~!"
    
    c "Accusation of actions amounting to molestation!"
    
    $ best_girl = "Penny"
    $ weiss_points = 0
    $ blake_points = 0
    $ ruby_points = 0
    $ yang_points = 0
    
    menu:
        "Pick best girl. Choose wisely."
        
        "Blake.":
            best_girl = "Blake"
            blake_points += 1
            weiss_points -=1
            jump sb_Blake
            
        "Weiss.":
            best_girl = "Weiss"
            weiss_points += 1
            blake_points -= 1
            jump sb_Weiss
        
        "For the love of Dust, help Radcliff before he gets legitimately raped by a fourteen-year-old girl.":
            best_girl = "Radcliff"
            jump sb_It_snotrapeifwe_rebothscreaming
        
        "Pussy out of a decision like the bitch you are. Bitch.":
            best_girl = "Right Hand"
            jump sb_Bitch
            
label sb_Blake:
    
    b "Positive response, including a soft smile."
    
    w "Ballistic reaction and a pointer finger in the face before walking off in a huff claiming you both as humanoid garbage."
    
    h "Dismayed reaction at such harsh treatment."
    
    b "Calm, happy re-assurance of your choice."
    
    c "Support of Hugh's choice while prying Ruby off of my weapon."
    
    r "Claim that I will always love your maul!"
    
    b "Suggestion that you walk together."
    
    c "Expression of thanks to Blake before apology, accidentally cockblocking Hugh while fleeing from Ruby."
    
    h "Attempted protest before being rushed off by Radcliff."
    
    jump shiningbeaconpt_2

label sb_Weiss:

    w "Positive response, including a smug look at Blake."
    
    b "Cold glare, followed by walking off without speaking."
    
    h "Dismayed reaction at such harsh treatment."
    
    b "Happy re-assurance of your choice and notation of Hugh's intelligence."
    
    c "Support of Hugh's choice while prying Ruby off of my weapon."
    
    r "Claim that I will always love your maul!"
    
    w "Suggestion that you speak at a later time about studying and/or networking."
    
    c "Expression of thanks to Weiss before apology, accidentally cockblocking Hugh while fleeing from Ruby."
    
    h "Attempted protest before being rushed off by Radcliff."

    jump shiningbeaconpt_2

label sb_It_snotrapeifwe_rebothscreaming:
    
    c "Expressed thanks as you remove Radcliff from direct contact with the Rube."
    
    r "Claim that you're repressing weaponsexuals!"
    
    "The two of you flee from Ruby."
    
    jump shiningbeaconpt_2

label sb_Bitch:
    
    "You die alone and unloved, due to picking the one definitely bad choice."
    return
    
label shiningbeaconpt_2:
    
     "Currently unfinished."
    
    return
