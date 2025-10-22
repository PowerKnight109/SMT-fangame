import time
from CharacterSheets import player, pixie, pixie1, daemon
from Dictionary import glossary
from CombatSystem import fight

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
    glossary[playername.lower()] = player.image +"\nThe human destined to seize the throne of creation and rule over gods and demons alike.\nThe Demon Summoning Program on their phone grants them the ability to summon and do battle with demons"
    glossary[pixie.name.lower()] = pixie.image +"\nA small fairy found in southwestern Britain known for their cheerful nature and love of pranks.\nA common prank they like to pull is causing humans to wander in circles. However, they are also known to help farmers from time to time and are generally considered good fairies"
    glossary[daemon.name.lower()] = daemon.image +'\nA low-ranking class of spirits.\nWhile the name may conjure up familiar images of "demons" due to'+ " Christianity's influence, daemons were not strictly associated with good or evil and simply thought to be lesser supernatural beings, sometimes acting as tutelary spirits that guided the souls of men.\nWhat might be considered a demon today would've been called a"+ ' "cacodaemon" in ancient Greece — that is, an evil spirit.\nIn contrast, their benevolent counterparts were known as "agathodaemons."'

    print("THE THRONE AWAITS")
    time.sleep(2)
    toriel = input("Is this your first time playing a Shin Megami Tensei game?\nA) Yes\nB) No\n").lower()
    if toriel == "a":
        know = input("Basics of SMT combat:\n- Gain turns based on the number of allies in your party\n- Demons can be recruited to your side by talking to them (not implemented)\n- Critical hits can only be gotten through strength-based attacks\n- Hitting an enemy with a critical hit or a move they are weak to will cause you to retain that turn\n- However, missing an attack or having it nullified will cause you to lose extra turns\n- These rules apply to both enemies and allies\n- Combat ends either when all fighters on a side are killed, or when the player is killed\n[IMPORTANT] If you do not know the meaning or effect of a word, simply type it in at any point during combat to receive an explanation of what it means.\nPress enter to continue\n")
        if know.lower() in glossary:
            print(glossary[know.lower()])
            input("Press enter to continue\n")
    print("[ROUND 1]\nPlayer vs Pixie")
    time.sleep(1)
    if fight([player], [pixie]):
        time.sleep(1)
        print("[ROUND 2]\nPlayer, allied Pixie vs Daemon, Pixie")
        time.sleep(1)
        if fight([player, pixie], [daemon, pixie1]):
            print("You Win!")

    print("GAME OVER")