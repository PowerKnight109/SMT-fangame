import time
from UI import vision
from CharacterSheets import Rei, player, pixie, pixie1, preta, slime, daemon, oak, slime1
from Dialogue import pixiescript, slimescript, pretascript, daemonscript
from Dictionary import glossary, lookup
from CombatSystem import fight
from Formulas import lvformula
from Tutorial import torielbattle


def intro():
    print("ATTEMPTING TO RUN [DEMON_SUMMONING_PROGRAM.EXE]")
    for i in range(3):
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
    print("STARTUP COMPLETE")
    time.sleep(1)
    playername = input("PLEASE ENTER THE NAME OF THE NEW RULER:\n")
    player.name = playername
    print("PLEASE SELECT THE FORM THAT THEY MOST CLOSELY RESEMBLE")
    print(vision(oak))
    hrt = input("A) Left\nB) Right\n").lower()
    if hrt == "b" or hrt == "right":
        player.image = oak[1].image
        Rei.image = oak[0].image
    glossary[player.name.lower()] = player.image +"\nThe human destined to seize the throne of creation and rule over gods and demons alike.\nThe Demon Summoning Program on their phone grants them the ability to summon and do battle with demons"
    glossary[pixie.name.lower()] = pixie.image +"\nA small fairy found in southwestern Britain known for their cheerful nature and love of pranks.\nA common prank they like to pull is causing humans to wander in circles. However, they are also known to help farmers from time to time and are generally considered good natured"
    glossary[daemon.name.lower()] = daemon.image +'\nA low-ranking class of spirits.\nWhile the name may conjure up familiar images of "demons" due to'+ " Christianity's influence, daemons were not strictly associated with good or evil and simply thought to be lesser supernatural beings, sometimes acting as tutelary spirits that guided the souls of men.\nWhat might be considered a demon today would've been called a"+ ' "cacodaemon" in ancient Greece — that is, an evil spirit.\nIn contrast, their benevolent counterparts were known as "agathodaemons."'
    glossary[slime.name.lower()] = slime.image + "\nA gel-like monster. It is said to be the byproduct of a failed summoning.\nDevoid of its original powers, this demon is cursed to wander the earth trapped in an incomplete gel form."
    glossary[preta.name.lower()] = preta.image + '\nKnown as "gaki" in Japanese, they are ghoulish demons of Buddhist lore.\nGreedy humans cast into the preta realm become these. Their hunger is unrelenting and their suffering continues until they are reincarnated.'
    pixie.lines = pixiescript
    pixie1.lines = pixiescript
    slime.lines = slimescript
    slime1.lines = slimescript
    preta.lines = pretascript
    daemon.lines = daemonscript
    toriel = "c"
    print("THE THRONE AWAITS")
    time.sleep(2)
    toriel = input("Would you like to play through the tutorial?\n[WARNING:] Basic reading ability is required\nA) Yes\nB) Give me the short version\nC) No\n").lower()
    if toriel == "a":
        torielbattle()
    elif toriel != "c":
        know = input("Basics of SMT combat:\n- Gain turns based on the number of allies in your party\n- Demons can be recruited to your side by talking to them\n- Critical hits can only be gotten through strength-based attacks\n- Hitting an enemy with a critical hit or a move they are weak to will cause you to retain that turn\n- However, missing an attack or having it nullified will cause you to lose extra turns\n- These rules apply to both enemies and allies\n- Combat ends either when all fighters on a side are killed, or when the player is killed\n[IMPORTANT] If you do not know the meaning or effect of a word, simply type it in at any point during combat to receive an explanation of what it means.\nPress enter to continue\n")
        if know.lower() in glossary:
            print(glossary[know.lower()])
            input("\npress enter to continue")

    party = [player]
    ring = [[pixie], [preta, slime], [slime1, daemon, pixie1]]
    rounds = 0
    while len(party) > 0 and rounds < len(ring):
        print("[ROUND", str(rounds+1)+"]")
        label = ""
        for i in range(len(ring[rounds])):
            if i != 0:
                label += ", "
            label += ring[rounds][i].name
        print("VS", label)
        time.sleep(1)
        aftermath =  fight(party, ring[rounds])
        if len(aftermath[0]) < 1 or player not in aftermath[0]:
            break
        else:
            party = aftermath[0]
            lvformula(player, party, aftermath[1])
        rounds += 1
        con = input("Press enter to begin the next battle\n")

    print("GAME OVER")



