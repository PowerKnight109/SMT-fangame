from Skills import effects
from CharacterSheets import daemon, pixie, player, pixie1
import math
#45
def vision(spriteselect):
    sprite = ""
    retainers = []
    track = 0
    total = 0
    for i in range(len(spriteselect)):
        retainers.append(0)
        total += len(spriteselect[i].image)

    for i in range(total):
        if retainers[track] < (len(spriteselect[track].image)):
            if spriteselect[track].image[retainers[track]] == "\n":
                #if retainers[track] == len(spriteselect[track].image) - 1:
                # spriteselect.remove(spriteselect[track])
                if track >= len(spriteselect)-1:
                    sprite += (spriteselect[track].image[retainers[track]])

                else:
                    sprite += "          "

                track += 1
                if track >= len(spriteselect):
                    track = 0

            else:
                sprite += (spriteselect[track].image[retainers[track]])

        retainers[track] += 1



    return sprite


def namedisplay(subject, allied):
    display = ""
    for i in range(len(subject)):
        label = ""
        for j in range(3):
            if subject[i].buffs[effects[j]]["stage"] != 0:
                if j == 0:
                    label += "(ATK"
                elif j == 1:
                    label += "(DEF"
                elif j == 2:
                    label += "(EVA"
                if  subject[i].buffs[effects[j]]["stage"] > 0:
                    for k in range(subject[i].buffs[effects[j]]["stage"]):
                        label += "^"
                else:
                    for k in range(subject[i].buffs[effects[j]]["stage"]*-1):
                        label += "v"
                label += ")"
        for j in range(6):
            token = ["(SLP)", "(MIRA)", "(PSN)", "(CONF)", "(CHRM)", "(SL)"]
            if subject[i].element[effects[j+3]]["dur"] != 0:
                label += token[j]

        if not allied:
            label = subject[i].name + ":" + label
            mid = math.floor(len(label)/2)
            for k in range(20-mid):
                label = " " + label
            for k in range(40-(20+mid)):
                label += " "
            display += label
            display += "          "
            if i == len(subject)-1:
                display += "\n"






    for i in range(len(subject)):
        totalh = 0
        hbar = ""
        totalm = 0
        mbar = ""
        for j in range(37):
            totalh += subject[i].mxhp / (37)
            if totalh < subject[i].hp:
                hbar += "+"
            else:
                hbar += "-"
            if allied:
                totalm += subject[i].mxmp/(37)
                if totalm < subject[i].mp:
                    mbar += "+"
                else:
                    mbar += "-"


        if allied:
            display = "Active Demon:" +" " + subject[i].name +"\n"+vision(subject) +"HP:"+hbar+"("+str(subject[i].hp)+"/"+str(subject[i].mxhp)+")" + " " + "\nMP:" + mbar + "("+ str(subject[i].mp) +"/"+str(subject[i].mxmp) + ")"
            if len(label) > 0:
                display += "\n"+"Status:" + label
        else:
            display += "HP:" + hbar + "          "
            if i == 0:
                display =  vision(subject) + "\n" + display



    print(display)

#
# For Demons:
# [IMAGE]
# Jack Frost(PSN)
# HP:+++++++++++++++++++++++=


#namedisplay([daemon, pixie, pixie1, player], False)
namedisplay([player], True)



#spaces equal to name-25, name, spaces equal to 50-(25+name)