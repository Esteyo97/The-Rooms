from sys import exit

print("""Welcome to \"The Rooms.\"
The rules are simple:
1. Answer in numbers (unless told otherwise)
2. Nothing other than numbers (i.e. no spaces)
3. Memorize stuff cause I'm not bothering reminding you.\n \n""")

hammer = False
translation_book = False

def dead(reason, hammer, translation_book):
    print(reason)
    print("You are DEAD, congrats!")
    print("Type 'e' to exit or 'r' to restart.")
    
    key = input("> ")

    if key == "e":
        exit(0)
    elif key == "r":
        hammer = False
        translation_book = False 
        starting_room(hammer, translation_book)
    else:
        print("Come on 'e' or 'r.'")
        dead(reason, hammer, translation_book)

def room15 (hammer, translation_book):
    print(""" You enter the final room. It is empty. There is a door at the end. It is calling you. 
    You walk slowly, carefully, expecting a puzzle, expecting a beast. You put your hand on the door and 
    it is humming, an ancient power running through the dark wood. You open and the door and enter a dark room. 
    As you open the door you see the room before you contains two doors and two objects, a hammer and a book. 
    As you realize the horrible truth, you also feel your memories escape you. You feel faint.""")

    print("Type 'c' to see what happens next.")
    keyc = input("> ")
    if keyc == "c":
        hammer = False
        translation_book = False 
        starting_room(hammer, translation_book)
    else: 
        print("Don't say my instructions weren't here.")
        room15(hammer, translation_book)

def room13 (hammer, translation_book):
    print("""You enter the room. How you know it is the final room, you dont know, but you feel it nonetheless. 
    At the end of the room stands a mirror image of you, but darkened, a shadow of you, almost.""")
    print("""Give in to the fear?
    1. Fight your demon
    2. It's time to give in
    """)
    key13 = int(input("> "))

    if key13 == 1:
        print("It's. Now. Or. Never. You stand and fight.")
        if hammer == True:
            print("""You hold your hammer with the little strength you have left. Your foe does the same. When the hammers meet mid-strike, 
            a piercing, shrill ringing fills the room. The hammers shatter, the shadow disappears. You will miss your trusted tool, but it has 
            served its purpose. You move on.""")
            room15 (hammer, translation_book)
        elif translation_book == True:
            print("""You drop the book, it is of no use to you now. You rush to meet the shadow and fight it with your bare hands. It is a 
            long and tiring battle, but you overcome. Your destination awaits.""")
            room15 (hammer, translation_book)
        else:
            print("""You rush to meet the shadow and fight it with your bare hands. It is a 
            long and tiring battle, but you overcome. Your destination awaits.""")
            room15 (hammer, translation_book)

    elif key13 == 2:
        print("""You choose to give in, and the shadow overcomes you.""")
        died("You die screaming, as it engulfs you completely. Eventually the room grows quiet and the air is still.", hammer, translation_book)


def room12 (hammer, translation_book):
    print("""You walk into a room of mirrors. In the middle of the room there is a crystal prism lit by a ray 
    of light coming from the outside. Above the mirrors are inscriptions. """)
    print ("""What do you do?
    1. Take the challenge
    2. To hell with these puzzles!
    """)

    key12 = int(input("> "))

    if key12 == 1:
        print("You attempt to translate the inscriptions.")
        if translation_book == True:
            print("""You translate the inscriptions and figure out that certain mirrors hold power while others serve only as distraction. 
            You manipulate the prism and complete the puzzle. Light engulfs the room. A mirror slides aside to reveal the passage leading forward. 
            You move on.""")
            room15 (hammer, translation_book)
        else:
            print("""You attempt to figure out the puzzle but without the book of translation it is futile. You have nowhere to go and waste away,
           basking in the little warmth the ray of light provides.""")
            died ("You die with hope on your mind.", hammer, translation_book)
    
    elif key12 == 2:
        print("You express your frustration at the machinery.")
        if hammer == True:
            print("""Tired of these games, you shatter every mirror until you find the way out. Not your proudest moment, but there is no place 
            for pride in a place like this.""")
            room15 (hammer, translation_book)
        elif translation_book == True:
            print("""You translate the inscriptions to identify the only mirror that matters. You take the prism and use it to shatter the mirror.
           This reveals a passage, leading deeper into the dungeon.""")
            room15 (hammer, translation_book)
        else:
            print("You wander aimlessly so close to the end. Your end however takes several days.")
            died ("You die hopelessly staring into the mirrors", hammer, translation_book)

def room10 (hammer, translation_book):
    print("You enter another rather empty room.")
    print("Suddenly you hear a bloodcurdling thump as a gargantuan spider falls from the roof. Disgusting saliva drips from its fangs.")
    print ("""What do you do?
    1. Charge the Spider
    2. Translate the Spider
    """)

    key10 = int(input("> "))

    if key10 == 1:
        print("You charge the gargantuan Spider with all your courage.")
        if hammer == True:                     
            print("""Your hammer comes down in one swift strike, digging deep into the beast's face. 
            It falls at your feet. You can’t help but feel remorse. Are you any less beastly than these creatures? 
            Possibly, but you must move on. """)
            room13 (hammer, translation_book)
        else:
            print("""You charge at the unnatural beast, no weapon in hand. As courageous as this, it is also naive. """)
            died("The spider takes you down, mangling your body in unimaginable ways. You die with a prayer on your lips.", hammer, translation_book)
            
    elif key10 == 2:
        print("You attempt to translate the Spider.")
        if translation_book == True:
            print("""You open your dusty tome. You find what you’re looking for and translate the wicked sounds 
            coming from the beast. “I demand tribute, human”. You pick up a jagged stone and run it quickly across your 
            open palm. As blood falls from your hand to the floor, the spider’s demeanor quickly changes. 
            It climbs up a wall, retreating to its nest. You move into the next room.""")
            room13 (hammer, translation_book)
        else:
            print("""The spider is obviously trying to communicate something to you, but you have no way of understanding it. 
            You take its morbid speech as an invitation to pass safely. This was a mistake.""")
            died ("You don’t last long after it pounces on you. Your bones snap under its weight, its fangs do the rest.", hammer, translation_book)

def room9 (hammer, translation_book):
    print ("""" You enter and are amazed by what you see. An incredibly intricate system of stone levers, pistons, and 
    buttons cover every surface of the room. Engraved in the stone are ancient runes, covered in dust but still visible 
    in the dim light. The door leading out is blocked by bars as thick as your head, only movable by the contraptions all around you.""")
    print ("""What do you do?
    1. Try to solve it
    2. You hate puzzles, express your frustration
    """)

    key9 = int(input("> "))

    if key9 == 1:
        print("You attempt to translate the inscriptions.")
        if translation_book == True:
            print("""You decipher the writing on the stone and uncover its secrets. You pull levers, push buttons, and the door eventually opens.""")
            room12 (hammer, translation_book)
        else:
            print("You stumble around aimlessly unable to figure out the puzzle. Dehydration sets in.")
            died ("You died trying to solve the mystery of the lever room.", hammer, translation_book)
    
    elif key9 == 2:
        print("You express your frustration at the machinery.")
        if hammer == True:
            print("""When logic fails you, brute force is your only way out. You hammer relentlessly at the stone, hoping to stir the bars blocking 
            your way. You eventually break enough of the machinery to cause the bars to open. A tragic end to such ancient engineering. A small price 
            to pay for your life, you decide.""")
            room12 (hammer, translation_book)
        else:
            print("You stumble around aimlessly unable to figure out the puzzle. Dehydration sets in.")
            died ("You died trying to solve the mystery of the lever room.", hammer, translation_book)

def room8 (hammer, translation_book):
    print ("""You enter the room feel deep and instant pity. Past adventurers are all around you, pleading for your help. 
    They are stuck here, they say, slaves to this unholy place. They need you, they insist, or else they will perish like dogs.""")
    print ("""What do you do?
    1. Help them
    2. Move on
    """)

    key8 = int(input("> "))

    if key8 == 1:
        print("""The moment you stop to help them you realize your mistake, but it is too late. The poor souls crowd you, 
        seeking help but consuming you in the process. Perhaps you will join them once you face judgement.""")
        died("Stopped to help the unsaveable.", hammer, translation_book)
    
    elif key8 == 2:
        print("""You remind yourself that you must escape this wretched cesspool and your resolve is strengthened. 
        You march past the dead despite their cries for help. It goes against all of your morals but you know it is the right thing. 
        The door at the end of the room opens easily. You move on.""")
        room12(hammer, translation_book)

def room7 (hammer, translation_book):
    print("You enter a surprsingly empty room.")
    print("""Suddenly your ears are immediately invaded by a hypnotic hum. It slithers through your head...your mind drifts….
    your thoughts wander......""")
    print ("""What do you do?
    1. Cover your ears
    2. Give in to the nectar-like sound
    """)

    key7 = int(input("> "))

    if key7 == 1:         
        print("""You realize immediately that this room is a killer, and the hum is its weapon. You cover your ears and 
        the fog occupying your mind is lifted. You run through the room as quickly as your tired feet can take you.""")
        print("You make it to the next door, and walk through into the next room.")
        room10 (hammer, translation_book)
            
    elif key7 == 2:
        print("""The sound is unsettling...but comforting in a way...you lay down and let it consume you….your mind 
        goes blank...you feel blissful relaxation...you don't even notice the vines gripping your feet and dragging 
        you into the darkness.""")
        died("You gave in to the voice of THE ROOMS.", hammer, translation_book)
        

def room6 (hammer, translation_book):
    print("You enter a rather empty room.")
    print("Suddenly a Spectre appears through the floor and starts floating towards you.")
    print ("""What do you do?
    1. Charge the Spectre
    2. Translate the Spectre
    """)

    key6 = int(input("> "))

    if key6 == 1:
        print("You charge the Spectre with all your courage.")           
        print("""You charge at the ghost, bringing glory on you and yours. You pass right through the evil being, 
        as it is not of this dimension. Quickly, you move on into the next room.""")
        room10 (hammer, translation_book)
            
    elif key6 == 2:
        print("You attempt to translate the ghost.")
        if translation_book == True:
            print("""With your handy translation book you hear the Spectre say:
                'Mortal, please pass through. You do not belong here.'
                You quickly pass through and walk through the door.""")
            room10 (hammer, translation_book)
        else:
            print("Well you don't know know ghost so... you just walk on through. You make it to the next room.")
            room10 (hammer, translation_book)

def room5 (hammer, translation_book):
    print ("As you enter you immediately notice a towering Sphinx blocking your way.")
    print ("""It says:
        'Et ut magis et magis relinqueret. Quld?'""")
    print ("""What do you do?
    1. Hit the damn Sphinx
    2. Translate the quote
    """)

    key5 = int(input("> "))

    if key5 == 1:
        print("You take a step forward preparing to attack.")
        print("The Sphinx looks at you and allows you to pass for some strange reason.")
        print(""""Where do you go?
        1. Left Door
        2. Right Door
        """)        
        decide5 = int(input("> "))
        if decide5 == 1:
            room8(hammer, translation_book)
        elif decide5 == 2:
            room9(hammer, translation_book)
        else:
            died("Your indecision angers the Sphinx, who eats you.", hammer, translation_book)


    elif key5 == 2:
        print("Uhh... oh man let's see.")
        if translation_book == True:
            print("""You translate the sly Sphinx's riddle: 
            'The more you take, the more you leave behind. What am I?'
            Type in the answer (nocaps)""")
            
            riddle5 = input(">")

            if riddle5==("footsteps"):
                print("the Sphinx bows in respect and steps aside")
                print(""""Where do you go?
        1. Left Door
        2. Right Door
        """)        
                decide5 = int(input("> "))
                if decide5 == 1:
                    room8(hammer, translation_book)
                elif decide5 == 2:
                    room9(hammer, translation_book)
                else:
                    died("Your indecision angers the Sphinx, who eats you.", hammer, translation_book)
            else:
                died("You answered wrong and the Sphinx eats you.", hammer, translation_book)

        else:
            print("Well you don't know how to translate it so guess the answer? (type in a word)")
            riddle5b = input(">")

            if riddle5b==("footsteps"):
                print("the Sphinx bows in respect and steps aside")
                print(""""Where do you go?
        1. Left Door
        2. Right Door
        """)        
                decide5b = int(input("> "))
                if decide5b == 1:
                    room8(hammer, translation_book)
                elif decide5b == 2:
                    room9(hammer, translation_book)
                else:
                    died("Your indecision angers the Sphinx, who eats you.", hammer, translation_book)
            else:
                died("You answered wrong and the Sphinx eats you.", hammer, translation_book)


def room3 (hammer, translation_book):    
    print ("As you enter you hear the sounds of dogs. These however have foam pouring out their mouths.")
    print("""What do you do?
    1. Beat the mutts. (Hey thay have rabies!)
    2. Attempt to translate the dogs
    """)
    key3 = int(input("> "))

    if key3 == 1:
        print("You charge at the dogs with all your might.")
        if hammer == True:            
            print("You beat them all aside as you rush to the next doors")
            print(""""Where do you go?
        1. Left Door
        2. Right Door
        """)        
            decide3 = int(input("> "))
            if decide3 == 1:
                room6(hammer, translation_book)
            elif decide3 == 2:
                room7(hammer, translation_book)
            else:
                died("Your indecision causes the dogs to catch up to you. They eat you.", hammer, translation_book)
        else:
            died("You just tried fighting rabid dogs with your bare hands. You dead.", hammer, translation_book)
    elif key3 == 2:
        print("You attempt to translate the dogs.")
        if translation_book == True:
            print("""With your handy translation book you see the dogs say:
                'Human, we just want to be loved! We cannot stop salivating.'
                This touches your heart and causes you to spend an entire hour giving these dogs the love they deserve.
                Grateful they let you through.""")
            print(""""Where do you go?
        1. Left Door
        2. Right Door
        """)    
            decide3 = int(input("> "))
            if decide3 == 1:
                 room6(hammer, translation_book)
            elif decide3 == 2:
                room7(hammer, translation_book)
            else:
                died("Your indecision causes you to stay with the dogs, where you eventually die of starvation.", hammer, translation_book)
        else:
            print("Well you don't know how to translate dogs.")
            print ("'TBH I don't know where to go with this one.' - Writer ")
            died("'TBH I don't know where to go with this one.' - Writer ", hammer, translation_book)

def right_room(hammer, translation_book):
    print("As you enter, you see a lock in a foreign language blocking the next door.")
    print("""What do you do?
    1. Hit the lock
    2. Attempt to translate the lock
    """)
    key = int(input("> "))

    if key == 1:
        print("Well that's uh, one way to get through puzzles.")
        if hammer == True:            
            print("You smash through the lock with your hammer.")
            print("You open the door and walk through.")
            room5(hammer, translation_book)
        else:
            print("Well that didn't work, and now your hand hurts like hell.")
            print("Let's try something else.")
            right_room(hammer, translation_book)
    elif key == 2:
        print("Keeping it smart? Nice!")
        if translation_book == True:
            print("""With your handy translation book you see it says:
                'A tickle makes a fickle door blissful.'
                Uhhh... ok. You tickle the door. You hear a faint chuckle.""")
            print("The door opens and you walk through.")
            room5(hammer, translation_book)
        else:
            print("Well you don't know how to translate it so uhh, pick a number from 1 to 10.")
            guess2 = int(input(">"))
            if guess2 == 7:
                print("Well you decide to tickle the door and well it opens...")
                print("You hear a faint chuckle as you pass on through.")
                room5(hammer, translation_book)
            else:
                print("You stumble around and don't do anything. Try again.")
                right_room(hammer, translation_book)


    #something about hitting the lock with a hammer or without one (and dying)
    #translate the lock, without the book you die as you pretend to be smart
    #guess at the lock

def left_room(hammer, translation_book):
    print("As you enter, you see a foreign looking goblin blocking the door.")
    print("He grunts something rather angrily at you.")
    print("""What do you do?
    1. Hit the goblin
    2. Attempt to translate the goblin's grunts
    """)

    key1 = int(input("> "))

    if key1 == 1:
        print("Well that's uh, rude.")
        if hammer == True:            
            print("But effective, you knock him down.")
            print("You open the door and march through like the psycho you are.")
            room3(hammer, translation_book)
        else:
            print("Your hand does nothing against his thick build, you just made him angry.")
            print("He wacks your face and well.")
            dead ("You died cause the smack kills you.", hammer, translation_book)
    elif key1 == 2:
        print("Apparently those grunts might mean something.")
        if translation_book == True:
            print("""With your handy translation book you understand it:
                'A hug makes a lonely goblin happy.'
                You're overcome with empathy. You give the goblin a hug""")
            print("The happy goblin lets you through.")
            room3(hammer, translation_book)
        else:
            print("Well you don't know how to translate it so uhh, pick a number from 1 to 10.")
            guess2 = int(input(">"))
            if guess2 == 3:
                print("You decide to give him a hug ...")
                print("That made him happy for some reason he let's you through.")
                room3(hammer, translation_book)
            else:
                print("He gets angry at your strange actions (to be honest they were kind of insensitive.")
                dead ("The goblin smacks and kills you.", hammer, translation_book)
    #kill the goblin, or he kills you
    #translate the goblin, or pretend and he gets mad and kills you
    #guess at the goblin


def starting_room(hammer, translation_book):
    print("Here you are. Here we are.")
    print("""You wake up in a room --
    *I mean where else right?*
    -- So you stand in a room.
    You look around and inspect the room.
    In front of you is a:
    1. Hammer
    2. Translation Book
    Which one do you pick up?""")
    
    item_selection = input("> ")
    item_selection_int = int(item_selection)

    if item_selection_int == 1:
        print("You pick up the hammer. It's a heavy one.")
        hammer = True
    elif item_selection_int == 2:
        print("You pick up the Translation Book. Playing it smart eh?.")
        translation_book = True
    else:
        print("Wow")
        print("Looks like you're too good for any tools.")
        print("Hey guys look! We got a try-hard here!")
        print("Suit yourself.")

    print("""As you look around more you notice two doors:
    1. Right 
    2. Left
    Through which one do you go through?""")

    door_selection_int = int(input("> "))

    if door_selection_int == 1:
        print("You pick the Right door, and go through it.")
        right_room(hammer, translation_book)
    elif door_selection_int == 2:
        print("You pick the Left door, and go through it.")
        left_room(hammer, translation_book)
    else:
        print("""We're not playing games anymore! HAHA!""")
        dead("You stumble around like the idiot you are and eventually die of dehydration.", hammer, translation_book)
    


    
starting_room(hammer, translation_book)

