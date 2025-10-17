from Skills import strike, skilluse
from CharacterSheets import player
from AI import  Descartes
from Dictionary import glossary
import time




def fight(party, enemy):
    pt = len(party)
    hpt = 0
    turn = 0
    combatants = party + enemy
    effects = ["taru", "raku", "suku", "Sleep", "Mirage", "Poison", "Confusion", "Charm", "Seal"]
    for i in range(len(party)):
        if strike in party[i].skills:
            party[i].skills.remove(strike)

    for i in range(len(combatants)):
        combatants[i].hp = combatants[i].mxhp
        combatants[i].mp = combatants[i].mxmp

        for j in range(3):
            combatants[i].buffs[effects[j]]["dur"] = 0
            combatants[i].buffs[effects[j]]["stage"] = 0
        for j in range(3, 9):
            combatants[i].element[effects[j]]["dur"] = 0
            combatants[i].element[effects[j]]["inflict"] = 0

    while True:
        print("\n\n")
        for i in range(len(combatants)):
            for j in range(3):
                if combatants[i].buffs[effects[j]]["dur"] <= 0:
                    combatants[i].buffs[effects[j]]["stage"] = 0

        combatants = party + enemy

        partydisplay = []
        enemydisplay = []
        partyhealth = []
        enemyhealth = []
        partymp = []

        for i in range(len(combatants)):
            display = ""
            for j in range(3):
                if combatants[i].buffs[effects[j]]["stage"] != 0:
                    if j == 0:
                        display += "(ATK"
                    elif j == 1:
                        display += "(DEF"
                    elif j == 2:
                        display += "(EVA"
                    if  combatants[i].buffs[effects[j]]["stage"] > 0:
                        for k in range(combatants[i].buffs[effects[j]]["stage"]):
                            display += "^"
                    else:
                        for k in range(combatants[i].buffs[effects[j]]["stage"]*-1):
                            display += "v"
                    display += ")"
            for j in range(6):
                token = ["(SLP)", "(MIRA)", "(PSN)", "(CONF)", "(CHRM)", "(SL)"]
                if combatants[i].element[effects[j+3]]["dur"] != 0:
                    display += token[j]

            total = 0
            bar = ""
            total2 = 0
            bar2 = ""
            for j in range(30):
                total += combatants[i].mxhp / 30
                if total < combatants[i].hp:
                    bar += "+"
                else:
                    bar += "-"
                if i < len(party):
                    total2 += combatants[i].mxmp/30
                    if total2 < combatants[i].mp:
                        bar2 += "+"
                    else:
                        bar2 += "-"

            if i < len(party):
                partydisplay.append(display)
                partyhealth.append(bar)
                partymp.append(bar2)
            else:
                enemydisplay.append(display)
                enemyhealth.append(bar)


        for i in range(len(enemy)):
            print(enemy[i].name + enemydisplay[i]+":", enemyhealth[i])
            # print(enemydisplay)
            # print(partydisplay)
            # print(pixie.buffs["suku"]["stage"])



        partymenu = input("A) Fight\nB) Talk\nC) Status\nD) Skip\nE) Flee\n").lower()

        if partymenu == "a":
            baton = 0
            while len(enemy) > 0 and len(party) > 0 and (pt > 0 or hpt > 0):
                if baton >= len(party):
                    baton = 0
                print("\nTurns:", pt, "        Half Turns:", hpt, "\n\nActive Demon:", party[baton].name, "\nHP:", str(party[baton].hp)+"/"+str(party[baton].mxhp), partyhealth[baton], "     MP:", str(party[baton].mp)+"/"+str(party[baton].mxmp), partymp[baton])
                if len(partydisplay[baton]) > 0:
                    print("Status:", partydisplay[baton])
                unitmenu = input( "A) Attack\nB) Skill\nC) Item\nD) Guard\nE) Pass\n").lower()
                if unitmenu == "a":
                    if len(enemy) == 1:
                        aim = "A"
                    else:
                        print("Who will you target?")
                        for i in range(len(enemy)):
                            print(chr(i + 65) + ")", enemy[i].name)
                        aim = input().upper()

                    if len(aim) != 1:
                        if aim.lower() in glossary:
                            print(glossary[aim.lower()])
                        else:
                            print("That is not a valid target!")
                    elif ord(aim) - 65 >= len(enemy):
                        print("That is not a valid target!")

                    else:
                        attack = skilluse(party, enemy, party[baton], enemy[ord(aim)-65], strike)
                        time.sleep(1)
                        if attack == -2:
                            pt = 0
                            hpt = 0
                        elif attack == -1:
                            if pt > 0:
                                pt -= 1
                                hpt += 1
                            else:
                                hpt -= 1
                        else:
                            for i in range(attack):
                                if hpt == 0:
                                    pt -= 1
                                else:
                                    hpt -= 1


                elif unitmenu == "b":
                    for i in range(len(party[baton].skills)):
                        print(chr(i+65)+")", party[baton].skills[i].name, "("+str(party[baton].skills[i].cost)+")")

                    chooseskill = input().upper()
                    if len(chooseskill) != 1:
                        if chooseskill.lower() in glossary:
                            print(glossary[chooseskill.lower()])
                        continue
                    elif ord(chooseskill)-65 < len(party[baton].skills):
                        cast = party[baton].skills[ord(chooseskill) - 65]
                        if party[baton].element["Seal"]["dur"] > 0:
                            print(party[baton].name, "is sealed! They are unable to use skills.")
                            continue
                        if cast.cost > party[baton].mp:
                            print("You don't have enough MP!")
                            continue
                        else:
                            if cast.friendly:
                                group = party
                            else:
                                group = enemy
                            if len(group) == 1:
                                aim = "A"
                            else:
                                print("Who will you target?")
                                for i in range(len(group)):
                                    print(chr(i + 65) + ")", group[i].name)
                                aim = input().upper()

                            if len(aim) != 1:
                                if aim.lower() in glossary:
                                    print(glossary[aim.lower()])
                                else:
                                    print("That is not a valid target!")
                                continue

                            elif ord(aim) - 65 >= len(group):
                                print("That is not a valid target!")
                                continue


                            used = skilluse(party, enemy, party[baton], group[ord(aim)-65], cast)
                            time.sleep(1)
                            if used == -2:
                                pt = 0
                                hpt = 0
                            elif used == -1:
                                if pt > 0:
                                    pt -= 1
                                    hpt += 1
                                else:
                                    hpt -= 1
                            else:
                                for i in range(used):
                                    if hpt > 0:
                                        hpt -= 1
                                    else:
                                        pt -= 1

                    else:
                        print("That's not a skill!")
                        continue

                elif unitmenu == "e":
                    if pt > 0:
                        pt -= 1
                        hpt += 1
                    else:
                        hpt -= 1


                else:
                    if unitmenu in glossary:
                        print(glossary[unitmenu])
                    else:
                        print("You can't do that yet")
                    continue

                baton += 1



        elif partymenu == "b":
            print("This feature has not been implemented yet")
            continue
        elif partymenu == "c":
            print("Who do you want to analyze?")
            for i in range(len(combatants)):
                print(chr(i + 65) + ")", combatants[len(combatants)-i-1].name)
                if i == len(enemy)-1:
                    print("\n")
            choose = input().upper()
            if len(str(choose)) != 1:
                continue
            elif ord(choose) - 65 < len(combatants):
                observee = combatants[len(combatants)-(ord(choose)-64)]
                print(observee.image, "\n"+observee.name, "(lv" + str(observee.lv) + ")\n" + "species:", observee.race, "\nHP:",
                      str(observee.hp) + "/" + str(observee.mxhp) + "\nMP:",
                      str(observee.mp) + "/" + str(observee.mxmp), "\n\nskill affinities:")
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

                print("\nstats:\nSTR:", observee.str, "\nVIT:", observee.vit, "\nMAG:", observee.mag, "\nAGL:",
                      observee.agl, "\nLCK:", observee.luck, "\n\nskills:")
                for i in range(len(observee.skills)):
                    print(observee.skills[i].name)
                while True:
                    end = input("Press enter to continue\n").lower()
                    if end.lower() in glossary:
                        print(glossary[end.lower()])
                    else:
                        break
                continue

            else:
                print("Not a valid target!")
                continue




        elif partymenu == "e":
            print("You can't run from this battle!")
            continue

        elif partymenu != "d":
            if partymenu in glossary:
                print(glossary[partymenu])
            continue




        if len(enemy) < 1:
            print("You won the battle")
            return True

        print("[ENEMY TURN]")
        Descartes(enemy, party)
        turn +=1
        pt = len(party)
        for i in range(len(combatants)):
            for j in range(3):
                if combatants[i].buffs[effects[j]]["dur"] > 0:
                    combatants[i].buffs[effects[j]]["dur"] -= 1




        if len(party) < 1 or player not in party:
            print("enemies win")
            return False






