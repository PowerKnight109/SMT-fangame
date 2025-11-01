
# input("What is your name?\n")
from Skills import strike, lunge, bestial_bite, gram_slice, agi, zio, bufu, zan, mudo, hama, dia, patra, dormina, dustoma, marin_karin, pulinpa, makajama, tarukaja, sukukaja, rakunda, hellish_slash
from Dictionary import lookup
import time
import random



class sex:
    def __init__(self, image):
        self.image = image

male = sex("                       #+-+#            \n                     #####+++           \n                    ######++#           \n                      ##+..##           \n                    ####+-++            \n                     ##++-++++++        \n                    ###.--#+#+-++       \n                    #+-.-+####+#++      \n                   ##++--#### ####++    \n              ##+++##+--.+###   +++#    \n           #######+##-----####+####     \n          #+# ######--...-+#+###        \n                 ##--++++++#+##+#       \n                ++#+#++#+-+-++###       \n              ++#########..##++##       \n               +##########.-# ##        \n              ++#+#+##########          \n            +++ +# -#### ##+++          \n           --      +####  #+++#         \n         +--       +###    #+++#        \n       --+         ####     #++#        \n      .-           +###     ##+##       \n    ..+            +###      #####      \n   .+              +###       +####     \n ++                 ###        #####    \n+#                  ###         ####    \n                   ####          ####   \n                   ####           #+#   \n                   ####           ##++  \n                   ####            ##++ \n                  ####+             ### \n                #####               ##+#\n                                     ##+\n")
female = sex("                   ++++++               \n                  #+---+##              \n                  ++++-+++              \n                  ##....##              \n                  ++#++#+++             \n               #+++++######+##          \n                ++#++-+++##+.+          \n               #++-+###+-.+#-#          \n              ++##+##+##++##--#         \n             ++-###+++-.+##+++++#       \n            -+++#+#+#-+..#++++#+--      \n           --.+#+++++-..##+-++++.-+     \n           +.+++-++++.#++#+--.-++       \n          ++-#+--+++++.+--++#+ -+       \n          +---+++#+#++++++#++++--+      \n          ++#+++#######+++#++++++#      \n         -#+#++++#######---++++++#      \n         ..-+++++++## ##--+.+++++       \n        ...++++#++##  +++++.-##++       \n       -..+++++#++## --+#++..++++       \n       ..++++ ##++#  ++++#+..++++       \n      -.+#++  #++##  ++####+..+ #+++#   \n     -.-#### ##++#    ++###+-.++  ##### \n    -..  #++#####      ++####-#+#       \n    -.+    +#####         +####++###    \n   -.-     ###+#            ##+####     \n  +--      ++###            ####+###    \n  --       #+##               ##+##+##  \n --+    ###++-                +--+   ###\n+--        --                  #+-      \n--        --#                   --+     \n+         +-+                   +++     \n         -#-#                   #+#-    \n         ..-                    +..-    \n         ##                       +#    \n")
oak = [male, female]

class chara:
    def __init__(self, name, race, lv, mxhp, hp, mxmp, mp, xp, str, vit, agl, mag, luck, loyal, coward, play, element, skills, lvskills, macca, buffs, guard, lines, image):
        self.name = name
        self.race = race
        self.lv = lv
        self.mxhp = mxhp
        self.hp = hp
        self.mxmp = mxmp
        self.mp = mp
        self.xp = xp
        self.str = str
        self.vit = vit
        self.agl = agl
        self.mag = mag
        self.luck = luck
        self.loyal = loyal
        self.coward = coward
        self.play = play
        self.element = element
        self.skills = skills
        self.lvskills = lvskills
        self.macca = macca
        self.buffs = buffs
        self.guard = guard
        self.lines = lines
        self.image = image

#taru = impacts attack, raku = impacts defence, suku = impacts evasion/accuracy


player = chara("You", "Human", 5, 58, 58, 73, 73, 0, 6, 6, 6, 6, 7, 0, 0, 0, {
      #"aff" = affinity, "res" = resistance, "dur" = duration "inflict" = times inflicted
       "Physical":{"aff": 0, "res":0},
       "Fire":{"aff": 0, "res":0},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 0, "res": 0},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": 0},
       "Almighty": {"aff": 0, "res": 0},
       "Support": {"aff": 0},
       "Heal": {"aff": 0},
       "Ailment": {"aff": 0},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": 0, "dur": 0, "inflict": 0},
       "Confusion": {"res": 0, "dur": 0, "inflict": 0},
       "Charm": {"res": 0, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
        }, [agi, zio], [hama, gram_slice, dia, makajama], 100, {"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "", oak[0].image)

Rei = chara("Rei", "Human", 10, 58, 58, 73, 73, 999, 10, 10, 10, 10, 10, 70, 0, 10, {"Physical":{"aff": 0, "res":0},
       "Fire":{"aff": 0, "res":0},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 0, "res": 0},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": 0},
       "Almighty": {"aff": 0, "res": 0},
       "Support": {"aff": 0},
       "Heal": {"aff": 0},
       "Ailment": {"aff": 0},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": 0, "dur": 0, "inflict": 0},
       "Confusion": {"res": 0, "dur": 0, "inflict": 0},
       "Charm": {"res": 0, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0}}, [hama], [], 999, {"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "",  oak[1].image)

daemon = chara("Daemon", "Brute", 7, 78, 78, 73, 73, 0, 11, 9, 9, 8, 7, -10, -20, 0, {
       "Physical":{"aff": 2, "res":0},
       "Fire":{"aff": 2, "res":0.5},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":-0.25},
       "Force": {"aff": 0, "res": 0},
       "Light": {"aff":-4, "res": -0.25},
       "Dark": {"aff": 2, "res": 1},
       "Almighty": {"aff":0, "res": 0},
       "Support": {"aff": 0},
       "Heal": {"aff": 0, "inflict": 0},
       "Ailment": {"aff": 0},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": -0.25, "dur": 0, "inflict": 0},
       "Confusion": {"res": 0, "dur": 0, "inflict": 0},
       "Charm": {"res": 0, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
}, [strike, hellish_slash, agi, mudo, tarukaja, rakunda], [],0,{"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "", "          ▓▓▓▓▓▓███████                 \n       █▓▓█████████     █ ███████       \n    ███████████▓██▓     █ █   ████▓█    \n  ███ ███  ██   █▓█▓▓▓▒ ▓▓▓▓▓ ▓██████   \n ██  ██    █      ▓▓██▒▓▓▓▒▓▓▓▓█▓█████  \n██   █            ▓▓▓▓█▓▓▓▓▓▓▓██▓▓▓████ \n                 ▓███▓▓██▓█████ ██ █████\n                ▓████▓▓██▓▓███▓     ████\n                ▓████▓▓██▓█▓█▓▓     █  █\n               ▒▓████▓▓█   ▓▓█▓        █\n            ▒▓ █▓▓████▓▓█  ▓███▓█      █\n          ▓███ ▓▓█████▓▓█████▓▓         \n         ██    ▓▓██  ▒▓█▓▓███           \n         ██▓▓███▓▓▓   ███▓█             \n           █   ▓▓██   ▓████             \n               ████  ▓████              \n                ███▓▓▓███               \n                 ▓▓███▓█                \n            ▒▒▒▒▓▓▓█████                \n           ▒▒▒▒▒▒ ██████                \n           ░▒▓▓▒  ███ █                 \n                  ███                   \n")

pixie = chara("Pixie", "Fairy", 2, 55, 55, 82, 82, 0, 2, 4, 7, 8, 6, 5, 0, 30,  {
       "Physical":{"aff": -2, "res":0},
       "Fire":{"aff": 0, "res":-0.25},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 1, "res": 0.5},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": -0.25},
       "Almighty": {"aff":0, "res": 0},
       "Support": {"aff": 1},
       "Heal": {"aff": 1, "inflict": 1},
       "Ailment": {"aff": 1},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": -0.25, "dur": 0, "inflict": 0},
       "Confusion": {"res": -0.25, "dur": 0, "inflict": 0},
       "Charm": {"res": 0.5, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
        }, [strike, zio, zan, patra, dia, sukukaja], [marin_karin, dustoma, pulinpa, dormina],0,{"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "", "                                        ▒\n                                     ░░░ \n        ░                          ░░░░  \n        ░░                       ░░░░░   \n         ░░                     ░░░░░░   \n          ░░  ▒               ░░░░░░░    \n           ░░ ░              ░░░░░░░     \n           ░░░░▓           ░░░░░░░░      \n           ▓░░░░         ▒░░░░░░░        \n         ▓▓▓█▓█▓█       ░░░░░░░    ░░░   \n        ▓▓███▒▒█▒     ░░░░░░░  ░░░░░░    \n        ███▒░░▒▓███ ░░░░░░░░░░░░░░░      \n         █▓▒░░░▓███░░░▒░░░░░░░░░         \n           █▒░▒░░░▒▓▒░░▒▒                \n        ▓▓▓▒▒▓▓░▒▒░▓█                    \n      ▓▓▓▓▓▓▓▓▓▓▒▒░▒█                    \n   ▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓                    \n  ▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓                    \n ▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓░░▒                    \n ▓▓█ ▓▓▓▓▓▓▓▓▓▓░▒░░░▓                    \n     ▓▓▓▓ █▒▓▒▒░░░░░                     \n    ▓▓▓▓▓   ▒▓▒▒▒▒░▒                     \n   ▓▓▓  ▓▓                               \n  ▓▓▓    ▓▓▓                             \n ▓▓▓▓    ▓▓█                             \n▓▓▓       ▓▓                             \n▓          ▓                             \n")

pixie1 = chara("Pixie(1)", "Fairy", 2, 55, 55, 82, 82, 0, 2, 4, 7, 8, 6, 5, 0, 30,  {
       "Physical":{"aff": -2, "res":0},
       "Fire":{"aff": 0, "res":-0.25},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 1, "res": 0.5},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": -0.25},
       "Almighty": {"aff":0, "res": 0},
       "Support": {"aff": 1},
       "Heal": {"aff": 1, "inflict": 0},
       "Ailment": {"aff": 1},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": -0.25, "dur": 0, "inflict": 0},
       "Confusion": {"res": -0.25, "dur": 0, "inflict": 0},
       "Charm": {"res": 0.5, "dur": 0, "inflict": 5},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
        }, [strike, zio, zan, marin_karin, patra, dia, sukukaja], [],0,{"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "", "                        ░░░░░      ░░░  \n                      ░░░      ░░░░░░░░░\n                     ░░░░   ░░░░░░   ░░░\n                    ░░░░░ ░░░░░░░░      \n                   ░░░░░░░░░░░░░░       \n                   ░░░░░░░░░░░░░        \n                  ░░░░░░░░░░░░░         \n            ▓▓▓███░░░░░░░░░░░░░░░░      \n           ▒▒▒▓▓▓▒▓░░░░░░░░░░ ░░  ░     \n           ▒▒▓▒░▒▒▓░░░░░░░░░     ░░     \n           ██▒░░░▓▓░░░░░░░░             \n               ░░▓▓▒░░░▒ ░░             \n                 ▒▒▒▓▒░▓   ░            \n                  ▒▒▓▓▓▓▓ ░░            \n                   ▓▓▓▓▓▓▓              \n                  ▓▒▒▓▓▓▒▓▓             \n           ▒▒▒▒▒▒▒░░░░▒█▓▒▓▓            \n          ▒▓▓▓▓▓██░░░░▓▓█▓▒▓▓▓▓         \n        ▓▒▒▓█████▒░░▒▓▓▓   ▓▓▓▓         \n       ▒▒▓▓███                          \n     ▒▒▓▓▓▓▓▓▓▓                         \n   ▒▒▓▓▓    ▓▓▓▓                        \n ▒▒▓▓█       ▓▓▓▓                       \n▒▓▓█          ▒▒▓█                      \n█              ▒▓█                      \n                ▓█                      \n")


def pclv():
    hpmin = [58, 62, 66, 70, 74, 78]
    mpmin = [73, 75, 78, 80, 83, 86]
    strmin = [6, 6, 7, 8, 8, 9]
    magmin = [6, 7, 8, 8, 9, 9]
    vitmin = [6, 6, 7, 8, 8, 9]
    aglmin = [6, 7, 7, 8, 9, 9]
    luckmin = [7, 8, 8, 8, 9, 10]
    # 0 = name, 1 = current value, 2 = min value
    if player.mxhp < hpmin[player.lv - 5]:
        print("HP increased by", str(hpmin[player.lv - 5] - player.mxhp))
        player.mxhp = hpmin[player.lv - 5]
    if player.mxmp < mpmin[player.lv - 5]:
        print("MP increased by", str(mpmin[player.lv - 5] - player.mxmp))
        player.mxmp = mpmin[player.lv - 5]
    if player.str < strmin[player.lv - 5]:
        print("Strength increased by", str(strmin[player.lv - 5] - player.str))
        player.str = strmin[player.lv - 5]
    if player.mag < magmin[player.lv - 5]:
        print("Magic increased by", str(magmin[player.lv - 5] - player.mag))
        player.mag = magmin[player.lv - 5]
    if player.vit < vitmin[player.lv - 5]:
        print("Vitality increased by", str(vitmin[player.lv - 5] - player.vit))
        player.vit = vitmin[player.lv - 5]
    if player.agl < aglmin[player.lv - 5]:
        print("Agility increased by", str(aglmin[player.lv - 5] - player.agl))
        player.agl = aglmin[player.lv - 5]
    if player.luck < luckmin[player.lv - 5]:
        print("Luck increased by", str(luckmin[player.lv - 5] - player.luck))
        player.luck = luckmin[player.lv - 5]
    time.sleep(1.5)

    sp = 3
    while sp > 0:
        print("\n\nA) Strength:", player.str, "\nB) Vitality:", player.vit, "\nC) Magic:", player.mag, "\nD) Agility:", player.agl, "\nE) Luck:", player.luck, "\nPlease select the stat you wish to improve", "\nYou have", sp, "skill points remaining")
        x = input().lower()
        if x == "a":
            player.str += 1
        elif x == "b":
            player.vit += 1
        elif x == "c":
            player.mag += 1
        elif x == "d":
            player.agl += 1
        elif x == "e":
            player.luck += 1
        else:
            lookup(x)
            continue
        sp -= 1


    while True:
        print("What do you wish to do?\nA) Improve skill affinity")
        if len(player.lvskills) > 0:
            print("B) Learn Skills")
        grow = input().lower()
        if grow == "a":
            for i in range(11):
                print(chr(i + 65) + ")", list(player.element)[i] + ":", player.element[list(player.element)[i]]["aff"])
            print("Select the element which you wish to improve your affinity for")
        elif grow == "b":
            picklen = len(player.lvskills)
            if picklen > 3:
                picklen = 3
            for i in range(picklen):
                print(chr(i + 65) + ")", player.lvskills[i].name)
            print("Select the skill which you wish to learn")
        else:
            lookup(grow)
            continue

        x = input().upper()
        if len(x) != 1:
            lookup(x)
            continue
        elif grow == "a" and ord(x)-65 < 11:
            print(list(player.element)[ord(x)-65], "affinity has increased by 1")
            player.element[list(player.element)[ord(x)-65]]["aff"] += 1
            break
        elif grow == "b" and ord(x)-65 < len(player.lvskills):
            print("You learnt", player.lvskills[ord(x)-65].name)
            player.skills.append(player.lvskills[ord(x)-65])
            player.lvskills.remove(player.lvskills[ord(x)-65])
            break
        else:
            print("[INVALID INPUT]")
            time.sleep(1)



def dlv(demon):
    hpup = random.randint(3,4)
    print("HP increased by", hpup)
    demon.mxhp += hpup
    mpup = random.randint(2, 3)
    print("MP increased by", mpup)
    demon.mxmp += mpup
    highest = [0, 0]
    stats = [demon.str, demon.vit, demon.mag, demon.agl, demon.luck]
    for k in range(len(stats)):
        if stats[k] > highest[1]:
            highest[0] = k
            highest[1] = stats[k]
    increase = [highest[0]]
    for i in range(2):
        bonus = random.randint(0, len(stats)-1)
        increase.append(bonus)
    for i in range(len(increase)):
        if increase[i] == 0:
            print("Strength increased by 1")
            demon.str += 1
        elif increase[i] == 1:
            print("Vitality increased by 1")
            demon.vit += 1
        elif increase[i] == 2:
            print("Magic increased by 1")
            demon.mag += 1
        elif increase[i] == 3:
            print("Agility increased by 1")
            demon.agl += 1
        elif increase[i] == 4:
            print("Luck increased by 1")
            demon.luck += 1

    if len(demon.lvskills) > 0:
        print(demon.name, "learnt", demon.lvskills[0].name)
        demon.skills.append(demon.lvskills[0])
        demon.lvskills.remove(demon.lvskills[0])

