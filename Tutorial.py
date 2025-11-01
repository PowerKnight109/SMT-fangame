import time
from CharacterSheets import player, Rei, daemon
from Dictionary import glossary
from UI import namedisplay
from Formulas import dmgformula

def torialsearch(word, phrase):
    word = word.lower()
    if word in glossary:
        print(glossary[word])
        while word in glossary:
            word = input("\npress enter to continue or type another word for an explanation\n").lower()
            if word in glossary:
                print(glossary[word])
    else:
        print("REI:\n"+phrase)
        time.sleep(1)

def torielbattle():
    print("A demon appeared!")
    namedisplay([daemon], False)
    time.sleep(1)
    print("REI:\n'Crap! What's a demon doing here of all places?'\n'Don't worry", player.name+", lets stay calm and try to beat it together'\n'let's see... first I think we should view the STATUS menu to see what we're dealing with'\n'This should allow us to view all the information on a single unit in battle, without using a turn'")
    while True:
        an = input("\n\n\nC) Status\n").lower()
        if an == "c":
            observee = daemon
            print(observee.image, "\n" + observee.name, "(lv 7) \nspecies: Brute", "\nHP:", str(observee.hp) + "/" + str(observee.mxhp) + "\nMP:", str(observee.mp) + "/" + str(observee.mxmp), "\n\nskill affinities:")
            for i in range(11):
                print(list(observee.element)[i] + ":", observee.element[list(observee.element)[i]]["aff"])
            print("\nweaknesses and resistances:")
            for i in list(range(7)) + list(range(11, 16)):
                if observee.element[list(observee.element)[i]]["res"] != 0:
                    if observee.element[list(observee.element)[i]]["res"] < 0:
                        print(list(observee.element)[i] + ":", "WEAK")
                    elif observee.element[list(observee.element)[i]]["res"] < 1:
                        print(list(observee.element)[i] + ":", "RESIST")
                    elif observee.element[list(observee.element)[i]]["res"] == 1:
                        print(list(observee.element)[i] + ":", "NULL")
                    elif observee.element[list(observee.element)[i]]["res"] == 2:
                        print(list(observee.element)[i] + ":", "DRAIN")
                    elif observee.element[list(observee.element)[i]]["res"] == 3:
                        print(list(observee.element)[i] + ":", "REPEL")
            print("\nstats:\nSTR:", observee.str, "\nVIT:", observee.vit, "\nMAG:", observee.mag, "\nAGL:", observee.agl, "\nLCK:", observee.luck, "\n\nskills:\nCritical Aura\nStrike")
            while True:
                print("\nREI:\n'You don't need to worry about what most of this means for now.'\n'The main thing to focus on is the demon's moves, as well as weaknesses and resistances'")
                end = input("'Once you're ready, press ENTER to return to battle'\n").lower()
                if end.lower() in glossary:
                    print(glossary[end.lower()])
                else:
                    break
            namedisplay([daemon], False)
            print("REI:\n'Now that we have some more information on the enemy, let's try fighting it.'\n'Let's use the FIGHT command to enter the combat menu for each party member'\n")
            while True:
                fight = input("A) Fight\n\nC) Analyse\n").lower()
                if fight == "a":
                    namedisplay([player], True)
                    print("Turns:", 2, "                         Half Turns:", 0)
                    print("REI:\n'This is the unit menu. This determines the combat actions individual members of your party will take'\n'Your party can keep taking actions until both your turns and half-turns run out, and the current party member who you are controlling is displayed as the 'active demon''\n'Right now, it seems like you're up. Let's try taking the STRIKE action to use a basic physical attack.'\n")
                    while True:
                        bhit = input("A) Strike\n").lower()
                        if bhit == "a":
                            damage = dmgformula(player, daemon, "Physical", 100, -999)
                            print(player.name, "used Strike!")
                            print(daemon.name, "took", damage[0], "points of damage!")
                            daemon.hp -= damage[0]
                            time.sleep(1)
                            namedisplay([Rei], True)
                            print("Turns:", 1, "                         Half Turns:", 0)
                            print("REI:\n'Great job! Now if I remember correctly, we saw that demon was weak to the LIGHT element.'\n'I think a skill of mine does damage of that element, so let's try entering the SKILL menu and having me cast HAMA'")
                            while True:
                                sk = input("\nA) Strike\nB) Skill\n").lower()
                                x = sk
                                if sk == "b":
                                    x = input("A) Hama\n").lower()
                                    if x == "a":
                                        print("Rei used Hama on Daemon!")
                                        Rei.mp -= 10
                                        damage = dmgformula(player, daemon, "Light", 130, -999)
                                        print("Daemon took", damage[0], "points of damage!")
                                        time.sleep(1)
                                        namedisplay([player], True)
                                        print("Turns:", 0, "                         Half Turns:", 1)
                                        print("REI:\n'Awesome! Because the demon was WEAK to that attack, we got an extra half-turn for you to use!'\n'While skills can be more versatile and deal more damage than your basic strike, they also cost MP to use'\n'Fortunately, we can use Chakra Drops to restore our MP'\n'Let's use your extra turn to go to the ITEMS menu and restore my MP with a CHAKRA DROP'")
                                        while True:
                                            help = input("\nA) Strike\nB) Skill\nC) Item\n").lower()
                                            if help == "c":
                                                inv = input("A) Life Stone: 5\nB) Chakra Drop: 4\nC) Revival Bead: 1\n").lower()
                                                if inv == "b":
                                                    while True:
                                                        print("Who will you use it on?\nA)", player.name, "\nB)", Rei.name)
                                                        t = input().lower()
                                                        if t == "b":
                                                            print(player.name, "used Chakra Drop on Rei!")
                                                            print("Rei had their MP restored by 50!")
                                                            time.sleep(1)
                                                            print("[ENEMY TURN]")
                                                            print("Daemon used Critical Aura\nTheir next attack is guaranteed to be CRITICAL!")
                                                            time.sleep(1)
                                                            namedisplay([daemon], False)
                                                            print("REI:\n'Crap, that's bad! But don't worry, I have an idea.'\n'First, let's enter the combat menu again by selecting FIGHT'")
                                                            while True:
                                                                p = input("\nA) Fight\n\nC) Status\n").lower()
                                                                if p == "a":
                                                                    namedisplay([player], True)
                                                                    print("Turns:", 2,"                         Half Turns:", 0)

                                                                    print("REI:\n'Hitting weaknesses isn't the only way to generate half-turns. They can also be generated by critical hits or taking the PASS action'\n'Selecting PASS will consume your current turn in order to create a half-turn, allowing the next person in your party to act sooner'\n'Let's try taking the PASS action to generate a half-turn and switch to me!'\n")
                                                                    while True:
                                                                        p1 = input("A) Strike\nB) Skill\nC) Item\n\nE) Pass\n").lower()
                                                                        if p1 == "e":
                                                                            namedisplay([Rei], True)
                                                                            print("Turns:", 1, "                         Half Turns:", 1)
                                                                            print("REI:\n'Great job! Now, let's convert our final turn into a half-turn by having me cast HAMA again!'")
                                                                            while True:
                                                                                x = input("\nA) Strike\nB) Skill\nC) Item\n\nE) Pass\n").lower()
                                                                                if x == "b":
                                                                                    x = input("A) Hama\n").lower()
                                                                                    if x == "a":
                                                                                        print("Rei used Hama on Daemon!")
                                                                                        Rei.mp -= 10
                                                                                        damage = dmgformula(player, daemon, "Light",130, -999)
                                                                                        print("Daemon took", damage[0],"points of damage!")
                                                                                        time.sleep(1)
                                                                                        namedisplay([player], True)
                                                                                        print("Turns:", 0, "                         Half Turns:", 2)
                                                                                        print("REI:\n'Not only would a critical hit from the enemy demon do extra damage, it'd also generate a half-turn allowing it to act again!'\n'However, we can prevent this by taking the GUARD action.'\n'Not only does guarding halve any damage received, it also prevents attacks received from being critical!'\n'Let's both GUARD against the enemy demon's attack'")
                                                                                        while True:
                                                                                            p = input("\nA) Strike\nB) Skill\nC) Item\nD) Guard\nE) Pass\n").lower()
                                                                                            if p == "d":
                                                                                                print(player.name, "took a defensive stance!")
                                                                                                time.sleep(1)
                                                                                                player.guard = True
                                                                                                namedisplay([Rei], True)
                                                                                                print("Turns:", 0,"                         Half Turns:", 1)
                                                                                                while True:
                                                                                                    p = input("A) Strike\nB) Skill\nC) Item\nD) Guard\nE) Pass\n").lower()
                                                                                                    if p == "d":
                                                                                                        print("Rei took a defensive stance!")
                                                                                                        time.sleep(1)
                                                                                                        Rei.guard = True
                                                                                                        print("[ENEMY TURN]")
                                                                                                        print("Daemon used Strike on Rei!")
                                                                                                        d = dmgformula(daemon, Rei, "Physical", 100, -999)
                                                                                                        print("Rei took", d[0], "points of damage!")
                                                                                                        Rei.hp -= d[0]
                                                                                                        time.sleep(1)
                                                                                                        namedisplay([daemon], False)
                                                                                                        print("REI:\n'Ouch that hurt... but don't worry- I'm ok'\n'Though I've realised, this demon may make a valuable ally to us if we were to befriend it'\n'Instead of fighting, why don't we issue the TALK command to our party?'\n'Though be warned- if things go sour, the demon may get a free turn on us'")
                                                                                                        while True:
                                                                                                            t = input("\nA) Fight\nB) Talk\nC) Analyse\n").lower()
                                                                                                            if t == "b":
                                                                                                                print("You struck up a conversation with the Daemon")
                                                                                                                time.sleep(1)
                                                                                                                print("DAEMON:\n'You WAnt tO REcruIT ME?'\n'Well surE if YOU gIVe mE SOME itEms!'")
                                                                                                                time.sleep(1)
                                                                                                                print("'lETs See heRe...'")
                                                                                                                time.sleep(1)
                                                                                                                print("'I'LL tAkE onE LifE STONe!'")
                                                                                                                while True:
                                                                                                                    x = input("\nA) Comply\nB) Ask for something else\nC) You don't need that\n").lower()
                                                                                                                    if x == "a":
                                                                                                                        print("DAEMON:\n'hAhA NIce!'")
                                                                                                                        print("'GiMme anOTHer lIFe stONe!'\n")
                                                                                                                        while True:
                                                                                                                            x = input("A) Comply\nB) Ask for something else\nC) You don't need that\n").lower()
                                                                                                                            if x == "a":
                                                                                                                                print("DAEMON:\n'Boy, you RealLy aRE a DUmbASS, AReN'T YOu?'")
                                                                                                                                print("The daemon left")
                                                                                                                                time.sleep(1)
                                                                                                                                print("\nREI:\n'Unfortunately that is another outcome which can arise from talking with demons'\n'Some may ask for more than they actually need, so it's up to you to put your foot down when you think they've had enough'\n")
                                                                                                                                time.sleep(1)
                                                                                                                                print("'You'll be on your own from now on, but I trust you'll be able to handle yourself.'\n'Just in case you're ever stuck though, take this'\n")
                                                                                                                                print("(Rei handed you the GLOSSARY)")
                                                                                                                                print("'This is a glossary filled with everything I've learnt about this world.'\n'If you ever don't know what something means or what it does, type it into any menu in the game, and you're likely to receive an explanation'")
                                                                                                                                time.sleep(2)
                                                                                                                                print("'Sayonara,", player.name+". May our paths cross again sometime'")
                                                                                                                                time.sleep(1)
                                                                                                                                print("[Rei left the party]")
                                                                                                                                time.sleep(2)
                                                                                                                                input("press enter to start the true game")
                                                                                                                                return
                                                                                                                            else:
                                                                                                                                torialsearch(x,"'Let's just give him what he wants for now.'")
                                                                                                                    else:
                                                                                                                        torialsearch(x,"'Let's just give him what he wants for now.'")



                                                                                                            torialsearch(x, "'I don't want more meaningless bloodshed'\n'Let's see if we can't end this a more peaceful way'" )
                                                                                                    else:
                                                                                                        torialsearch(p, "'If I do that I'll be left unprotected! I think it's better for me to take the GUARD action'")
                                                                                            else:
                                                                                                torialsearch(p, "'The demon's next attack looks rough! I think it's better to take the GUARD action here'")
                                                                                torialsearch(x, "'I don't think that's the best thing to do here. Try going to the SKILL menu and having me use HAMA instead.'")
                                                                        else:
                                                                            torialsearch(p1, "'If you have no half-turns or ways to generate them, sometimes it's better to PASS to another ally than waste a whole turn on your action.'\n'Please type 'E' to take the PASS action'")
                                                                else:
                                                                    torialsearch(p, "'For my plan to work you need to do exactly what I say.'\n'Type 'A' to enter the combat menu'")
                                                        else:
                                                            torialsearch(t, "'I think that Chakra Drop would be better used on me, don't you think?'")
                                            inv = help
                                            torialsearch(inv, "'I know you want to do your own thing, but for now please listen to me and use a CHAKRA DROP by going to the ITEM menu'")

                                torialsearch(x, "'HAMA is a skill of mine which deals light damage, so let's go to the SKILL menu and get me to cast it!'")
                        else:
                            torialsearch(bhit, "'For now, let's just try using a basic attack with the STRIKE action'")
                else:
                    torialsearch(fight, "'We've already viewed the enemy's status, now let's try FIGHTing it!'")
        else:
            torialsearch(an, "'First, view the enemy's STATUS by typing in 'C' and hitting enter'")





#analyse > strike > hama > chakra pot > (enemy crit aura) > pass to ren > hama > double guard > enemy attack > talk