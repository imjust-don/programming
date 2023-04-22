import time

print('----------------------------------')
print('''Welcome to Brandons Choose Your
own Adventure Game''')
print('----------------------------------')

print('')

print('''You find yourself at the entrance of a dark and mysterious cave.
And as far as you can tell you have two options. You can go LEFT or Right.''')

choice = input('What will you choose?: ')

if choice.upper() == 'LEFT':
# 1
    print('')
    print("""After choosing to go left you're led down a long dark path
    until the dark hallway opens up into a large bright cavern with an
    underground watterfall. 'Awesome' You think to yourself. You notice
    the wall of rocks leading up the falls. Would you like to CLIMB? Or
    you can continue SEARCHING.""")

    print('')

    choice = input('What will you choose?: ')

    if choice.upper() == 'CLIMB':
    #3
        print('')
        print("""You bein the treacherous climb up the waterfall. Its a long and incredibly hard
        climb but after almost falling twice you find yourself at the top. once you do you find 
        yourself face to face with a snake pit. As you can see it you see only two options either
        RUN through the snakes or you can try and CHARM them with the trusty flute you carry with
        you at all times.""")
        choice = input('What will you choose?: ')
        if choice.upper() == "RUN":
            # 7
            print('')
            print("""You make a foolish attempt to run through the snakes. You recieve many snake bites and
            unfortunate for you the venom is deadly. This is where you die alone in a cave forever forgotten""")
            time.sleep(500)
        elif choice.upper() == 'CHARM':
            # 8
            print('')
            print("""You have whip out your trusty flute and begin to play a joyful tune. As you do you begin to 
            see a shift in the snakes bahavoir. You keep playing intently willing the snakes to follow your commands
            and on cue they begin to shift and move revealing a path. You being walking down the path still 
            playing your flute. Once through the snakes you find yourself in a chamber full of treasure. This will 
            definately solidify your name in glory""")
            time.sleep(500)
        else:
            print('')
            print('Invalid option')
            time.sleep(500)

    elif choice.upper() == 'SEARCHING':
    # 4
        print('')

        print('''After deciding to search you soon discover a cavern beind the waterfall. You look around and
        are astonished to see a caver full of treasure. Its like nothing you've ever seen before but you cant
        see the caverns end it appears to go on for an unfathonable distance. That means you have another 
        choice. Will you STAY and gather the treasure? Or will you CONTINUE?''') 
        choice = input('What will you choose?: ')
        if choice.upper() == "STAY":
            # 9
            print('')
            print("""You decided to make the safe choice and enjoy the treasure you found. You begin to gather
            it all up so that you can take it home and have your name go down in glory.""")
            tiem.sleep(500)
        elif choice.upper() == "CONTINUE":
            # 10
            print('')
            print("""You made the risky choice to continue on. And congradulations it payed off as you walk 
            deeper into the cave you discover that the treasure at the begining was only a taste of what lies
            in the rest of the cave. Riches beyond your wildest dreams you immediatly beggin packing it up 
            and making preperations to have it all escavated. You will be famous for this!""")
            time.sleep(500)
        else:
            print('')
            print('Invalid option')
            time.sleep(500)
    else:
            print('')
            print('Invalid option')
            time.sleep(500)

elif choice.upper() == 'RIGHT':
# 2
    print('')
    print("""After choosing to go left you're led down a long dark path
    until the dark hallway is filled with the a peculure sound. Like
    tiny little feet scuttling accossed the ground. Its not until the
    light of a nearby torch dimly illuminates what you believe to be 
    a giant pit of spiders. Terrified to move on you notice a vine
    dangling at perfect swinging distance. Theres not much time
    Will you SWING or pick up the TORCH?""")

    print('')
    choice = input('What will you choose?: ')
    if choice.upper() == "SWING":
    # 5
        print('')
        print("""You chose to swing on the vine. You grab it and jump
        you barely make it half way accross before the vine snaps and you
        begin to free fall straight into the spider pit. They immediatly 
        begin crawling all over you they beggin to bite and you scream in
        pain. You can either RUN or CLIMB""")
        choice = input('What will you choose?: ')
        if choice.upper() == 'RUN':
        # 11 
            print('')
            print("""You try to run but it becomes to much. They crawl all over
            you and begin to bite you. You can feel the venom running through 
            your viens it burns and then you die.""")
            time.sleep(500)
        elif choice.upper() == "CLIMB":
        # 12
            print('')
            print("""Your try to climb the wall to escape the spiders but they're 
            faster than you crawling even faster. All over you they begin to weigh
            you down and you fall hitting the ground hard. Between that and the 
            venom you stand no chance. You die there on the cave floor.""")
            time.sleep(500)
        else:
            print('')
            print('Invalid option')
            time.sleep(500)

    elif choice.upper() == "TORCH":
    # 6
        print('')
        print("""You pick up a torch and in the reflections of the cave wall you can see
        another cave entrance off to the side. But you're also really nervous you can RUN
        go to the CAVE or try and go INTO the spiders""")
        choice = input('What will you choose?: ')
        if choice.upper() == "CAVE":
        # 13
            print('')
            print("""You enter the new cave entrance and you can see that you made the wise choice
            because you can now see that there is more treasure than you could ever imagine. Your 
            name will go down in glory.""")
            time.sleep(500)
        elif choice.upper() == "INTO":
        # 14
            print('')
            print("""You decide to ignore your fear and the cave entrance and brave the spiders you start
            waving the torch scaring them off forcing them to run away from you. You eventually make it 
            through the spiders and find yourself at the cave exit. Vowing to never return to the cave
            you leave in tacked and unscathed.""")
            time.sleep(500)
        elif choice.upper() == "RUN":
        # 15
            print('')
            print("""You were to scared and chickened out running back the way to came forsacing adventuring 
            forever. Because clearly its not for you""")
            time.sleep(500)
        else:
            print('')
            print('Invalid option')
            time.sleep(500)
    
    else:
        print('')
        print('Invalid option')
        time.sleep(500)

else:
    print('')
    print('Invalid option')
    time.sleep(500)

# nice
