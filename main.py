from CharacterSheets import player, pixie, pixie1, daemon
from Dictionary import glossary
from CombatSystem import fight
import time
playername = input("What is your name?\n")
player.name = playername
glossary[(playername).lower()] = "The human destined to seize the throne empyrean and rule over gods and demons alike.\nThe Demon Summoning Program on their phone grants them the ability to summon and do battle with demons"
toriel = input("Is this your first time playing a Shin Megami Tensei game?\nA) Yes\nB) No\n").lower()
if toriel == "a":
    input("Basics of SMT combat:\n- Gain turns based on the number of allies in your party\n- Demons can be recruited to your side by talking to them (not implemented)\n- Critical hits can only be gotten through strength-based attacks\n- Hitting an enemy with a critical hit or a move they are weak to will cause you to retain that turn\n- However, missing an attack or having it nullified will cause you to lose extra turns\n- These rules apply to both enemies and allies\n- Combat ends either when all fighters on a side are killed, or when the player is killed\n[IMPORTANT] If you do not know the meaning or effect of a word, simply type it in at any point during combat to receive an explanation of what it means.\nPress enter to continue\n")
print("[ROUND 1]\nPlayer vs Pixie")
time.sleep(1)
if fight([player], [pixie]):
    time.sleep(1)
    print("[ROUND 2]\nPlayer, allied Pixie vs Daemon, Pixie")
    time.sleep(1)
    if fight([player, pixie], [daemon, pixie1]):
        print("You Win!")

print("GAME OVER")

#