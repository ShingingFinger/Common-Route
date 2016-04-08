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
define mnews = Character('Male Broadcaster', color="#c8ffc8")
define lisa = Character('Lisa Lavender', color="#c8ffc8")
define unk = Character('???', color="#c8ffc8")
init :
$ gyndasname = "Who's That?"
$ gw = DynamicCharacter("glyndasname", color=(192, 64, 64, 255))

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
    "He whistles softly, pointing out a blonde wearing what indeed appear to be hotpants."
    "She's talking to a girl with black hair and grey eyes."
    c "I wouldn't mind being hunted by her, if you get my drift."
    h "You know if she hears you, you're getting the third-rate trip down, right?"
    c "Wow, do you literally have no sex drive?"
    c "Come on, man. If I do one thing for you this semester, it's get you a girlfriend."
    h "You couldn't get a girlfriend for yourself, much less for me."
    "He seems slightly hurt at this, which suprises me a bit- normally, it'd be considered fair game to poke fun at the fact that, well, we're both awful with women."
    "Something must be on his mind."
    "However, I don't get to think about it for more than a minute, as a news broadcast comes on."
    "It displays a red-headed man in a suspect photo."
    mnews "...The robbery was led by nefarious criminal Roman Torchwick, who continues to evade authorities."
    c "Wow, he looks like a total tool."
    c "Wait, if he's evading the authorities, how did they get a mugshot of the guy?"
    "Something about him strikes me as odd, though I can't put my finger on it."
    mnews "If you have any information on his whereabouts, please contact the Vale Police Department."
    h "Hold on, I think I know him from something."
    c "Really? How?"
    "I'm about to speak, but no words come out."
    "Do I really know him, or am I just overthinking things?"
    h "Just my imagination, I guess."
    mnews "Back to you, Lisa."
    lisa "Thank you, Cyril."
    lisa "In other news, this Saturday's Faunus Civil Rights Protest turned dark when members of the White Fang disrupted the ceremony."
    "As I look at their flag, I wonder why a group intent on proving Faunus equality would use such a Grimm-evoking symbol."
    lisa "The once peaceful organization has now disrupted..."
    "Suddenly, the broadcast is cut off, and Radcliff and I look back between each other for a second, confused."
    "The hologram gives off a dull loudspeaker blare, generated the image of a blond woman dressed professionally, likely one of our professors."
    gw "Hello, and welcome to Beacon!"
    "We lean in to get a better view, to make sure we don't miss something important."
    gw "My name is Glynda Goodwitch."
    $ gyndasname = "Glynda Goodwitch"
    gw "You are amoung a privileged few who have recieved the honor of being selected to attend this prestigious academy!"
    gw "Our world is experiencing an incredible time of peace, and as future Huntsman and Huntresses, it is your duty to uphold it."
    c "Wow, I'm floored."
    h "Shut UP, Cliff."
    gw "You have demonstrated the courage for such a task, and now, it is our turn to provide you with the knowledge and the training to protect our world."
    "At that, the message ends, and the students begin to mill around again."
    "One guy begins to throw up, likely due to vertigo."
    c "Pft. Weak. At least you won't be bottom of the class, Hugh."
    h "Of course, that honor belongs to you."
    
    "But before he can retort, we're interrupted by a short outburst."
    unk "Are you blind?"
    unk "I-I said I was sorry..."
    "A meek girl is cowering, clutching what appears to be a piece of luggage to her chest in order to place it between her and her interrogator."
    "In front of her, a glowering student-to-be has her arms crossed and her brows furrowed."
    "After a few tense seconds, the latter huffs and breaks off, sparing us a catfight."
    unk "'Sorry' doesn't un-break my luggage. I hope for YOUR sake nothing got damaged."
    "Seeing she's not in immediate danger, the girl holding the suitcase sighs before catching our eye."
    "She brushes a stary hair out of her face and waves shyly." 
    "If I look closely I can see the start of a blush on her face."
    "Of course, Radcliff takes the opportunity to nail me in the side with an elbow."
    c "What did I tell you, buddy? Girlfriend."
    h "That's a bit forward."
    "He lowers his head and whispers to me in complete seriousness."
    c "She's totally into you, dude. Just look at her."
    "Something tells me that's not it."
    "Call it intuition."
    h "I doubt it."
    c "Uh, what? She just gave you the look- full nine yards."
    c "Only thing she could have done more was wink at you."
    "The more I think about it, the more I'm sure."
    h "Dude, love at first sight isn't a thing."
    c "Not with that attitude, it isn't."
    h "You're hopeless."
    c "Says the guy that just dropped the opportunity to chat up a girl because he's not feeling it?"
    c "You need to get out of your comfort zone, for reals."
    
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
