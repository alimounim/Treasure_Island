print(r'''
       -=[ deserted on island ]=-  12/98
                    _
                   /_'. _
                 _   \ / '-.
                < ``-.;),--'`
                 '--. |__
      /-/-/|o|-|\-\\|\\   / | \
       '`  ` |-|   `` '               |") |_" (_" /"' | | |_" |"\
             |-|                      |"\ |__ ,_) \_, |_| |__ |_/  o  o  o
             |-|O
             |-(\,__
          ...|-|\--,\_....
      ,;;;;;;;;;;;;;;;;;;;;;;;;,.
~~,;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;,~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

''')

print('''You wake up on the shore of a mysterious island after your ship was wrecked in a storm.
The air smells of salt and danger. In the distance, you see palm trees swaying and hear 
faint drumming. A golden glint flashes at the top of a volcano — the Treasure of Eldoria.''')

print("Your mission is to find the treasure and escape alive.")

choice1 = input(
    'You walk along a sandy path until it splits in two. '
    'Where do you want to go? Type "left" or "right".\n'
).strip().lower()

# 🪶 Decision 1: Crossroads
if choice1 == "left":
    print("You walk into the jungle.")
    choice_jungle1 = input(
        '''You push through vines and thick trees. Suddenly, you hear a hiss — a giant snake guards the way forward!
You spot:
- A stick nearby that you could use as a weapon.
- A narrow trail leading around the snake.
Do you want to fight with the stick or take the narrow trail? Type "stick" or "trail".\n'''
    ).strip().lower()

    if choice_jungle1 == "stick":
        print("You swing the stick, but the snake is faster. You are bitten. Game Over. 😵")
    elif choice_jungle1 == "trail":
        print("You escape and find a mysterious old map nailed to a tree.")
        print("The map points to a waterfall where treasure might be hidden.")

        print("You follow rushing water. Behind the falls, a cave glows with crystals.")
        print("A chest lies in the center, but a stone statue moves — a guardian spirit.")
        print('''It says:
        “Only the pure of heart may claim the treasure. Choose: gold or wisdom.”''')

        jungle_waterfall_choice1 = input('Type "gold" or "wisdom".\n').strip().lower()
        if jungle_waterfall_choice1 == "gold":
            print("You grab the gold. The cave collapses — Game Over. 💰🪨")
        elif jungle_waterfall_choice1 == "wisdom":
            print("The spirit blesses you and reveals a secret tunnel out — You win! 🥳")
        else:
            print("Your answer echoes uselessly. The cave fades to darkness. Game Over.")
    else:
        print("You hesitate too long. The snake slithers closer… Game Over. 🐍")

elif choice1 == "right":
    print("You walk onto the beach.")
    print("You explore the shipwreck. Inside a broken crate, you find a bottle with a message — a map of the island!")
    print("It marks three locations: Volcano, Waterfall, and Old Temple.")
    print('''You can:
- Head to the Volcano (🔥 danger, but direct path).
- Go to the Waterfall (🌊 safer, hidden entrance).
- Search the Temple ruins (⛩️ traps but ancient clues).''')

    choice_beach1 = input(
        'Where do you want to go? Type "volcano" or "waterfall" or "temple".\n'
    ).strip().lower()

    if choice_beach1 == "volcano":
        print("You climb hot rocks. Smoke thickens. A tribal guardian blocks your way.")
        print('''He offers a riddle:
“I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?”''')
        volcano_answer = input("Type your answer: ").strip().lower()

        if volcano_answer in ("echo", "an echo"):
            print('''Correct! He lets you pass. You reach the top — the treasure glows,
but the volcano starts to rumble! Now you must decide:''')
            volcano_echo_answer = input(
                'Do you want to grab the treasure or run for your life? Type "grab" or "run".\n'
            ).strip().lower()

            if volcano_echo_answer == "grab":
                print("You grab the gold. The island collapses — Game Over. 🧨")
            elif volcano_echo_answer == "run":
                print("You save your life but leave empty-handed. Game Over. 🏃‍♂️")
            else:
                print("You freeze in indecision as the ground splits. Game Over.")
        else:
            print("Wrong answer. The guardian banishes you to the lava fields. Game Over. 😭")

    elif choice_beach1 == "waterfall":
        print("You follow rushing water. Behind the falls, a cave glows with crystals.")
        print("A chest lies in the center, but a stone statue moves — a guardian spirit.")
        print('''It says:
“Only the pure of heart may claim the treasure. Choose: gold or wisdom.”''')

        waterfall_choice1 = input('Type "gold" or "wisdom".\n').strip().lower()
        if waterfall_choice1 == "gold":
            print("You grab the gold. The cave collapses — Game Over. 💰🪨")
        elif waterfall_choice1 == "wisdom":
            print("The spirit blesses you and reveals a secret tunnel out — You win! 🥳")
        else:
            print("Your answer echoes uselessly. The cave fades to darkness. Game Over.")

    elif choice_beach1 == "temple":
        print("An ancient temple of traps. A tile clicks — arrows zip past.")
        print('''You reach two doors:
- ☀️  Sun
- 🌙  Moon''')
        print("One leads to treasure; the other, to a pit of snakes.")

        temple_choice1 = input('Type "sun" or "moon".\n').strip().lower()
        if temple_choice1 == "sun":
            print("You solve the final puzzles and escape with both gold and wisdom. Victory! 🏆")
        elif temple_choice1 == "moon":
            print("A trapdoor! You fall into a pit of serpents — Game Over. 🐍")
        else:
            print("You choose neither. The temple seals forever. Game Over.")
    else:
        print("You wander aimlessly on the beach until night falls. Game Over.")

else:
    print('You stand still, undecided, as the tide rises. Type "left" or "right" next time. Game Over.')
