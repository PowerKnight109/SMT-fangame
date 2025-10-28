from Skills import strike, skilluse, effects, items
from CharacterSheets import player
from AI import  Descartes
from Dictionary import glossary
from UI import namedisplay
import time
import random
graveyard = {}

def fight(party, enemy):
    egraveyard = []
    pgraveyard = []
    pt = len(party)
    hpt = 0
    turn = 0
    combatants = party + enemy

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

        namedisplay(enemy, False)
        partymenu = input("A) Fight\nB) Talk\nC) Status\nD) Skip\nE) Flee\n").lower()

        if partymenu == "a":
            baton = 0
            while len(enemy) > 0 and len(party) > 0 and (pt > 0 or hpt > 0):
                if baton >= len(party):
                    baton = 0
                print("\nTurns:", pt, "        Half Turns:", hpt)
                namedisplay([party[baton]], True)
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
                            input("Press enter to continue\n")
                        else:
                            print("That is not a valid target!")
                            time.sleep(1)
                    elif ord(aim) - 65 >= len(enemy):
                        print("That is not a valid target!")
                        time.sleep(1)

                    else:
                        attack = skilluse(party, enemy, party[baton], enemy[ord(aim)-65], strike, [pgraveyard, egraveyard])
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
                            input("")
                        continue
                    elif ord(chooseskill)-65 < len(party[baton].skills):
                        cast = party[baton].skills[ord(chooseskill) - 65]
                        if party[baton].element["Seal"]["dur"] > 0:
                            print(party[baton].name, "is sealed! They are unable to use skills.")
                            continue
                        if cast.cost > party[baton].mp:
                            print("You don't have enough MP!")
                            time.sleep(1)
                            continue
                        else:
                            if cast.friendly == 1:
                                group = party
                            elif cast.friendly == 2:
                                group = pgraveyard
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
                                    input("")
                                else:
                                    print("That is not a valid target!")
                                    time.sleep(1)
                                continue

                            elif ord(aim) - 65 >= len(group):
                                print("That is not a valid target!")
                                time.sleep(1)
                                continue


                            used = skilluse(party, enemy, party[baton], group[ord(aim)-65], cast, [pgraveyard, egraveyard])
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
                        time.sleep(1)
                        continue

                elif unitmenu == "c":
                    backer = 0
                    for i in range(len(items)):
                        if items[i].cost > 0:
                            print(chr(i + 65 - backer) + ")", items[i].name+ ":",  items[i].cost)
                        else:
                            backer += 1
                    if backer == len(items):
                        print("You have no items")
                        time.sleep(1)
                        continue
                    itemuse = input("Which item would you like to use?\n").upper()
                    if len(itemuse) != 1:
                        if itemuse.lower() in glossary:
                            print(glossary[itemuse.lower()])
                            input("")
                        continue
                    elif ord(itemuse) - 65 < len(items):
                        useitem = items[ord(itemuse) - 65 + backer]
                        if useitem.cost <= 0:
                            print("You don't have that item!")
                            time.sleep(1)
                            continue
                        else:
                            if useitem.friendly == 1:
                                group = party
                            elif useitem.friendly == 2:
                                group = pgraveyard
                            else:
                                group = enemy
                            if len(group) < 1:
                                print("There's no-one to target!")
                                time.sleep(1)
                                continue
                            elif len(group) == 1:
                                aim = "A"
                            else:
                                print("Who will you target?")
                                for i in range(len(group)):
                                    print(chr(i + 65) + ")", group[i].name)
                                aim = input().upper()

                            if len(aim) != 1:
                                if aim.lower() in glossary:
                                    print(glossary[aim.lower()])
                                    input("")
                                else:
                                    print("That is not a valid target!")
                                    time.sleep(1)
                                continue

                            elif ord(aim) - 65 >= len(group):
                                print("That is not a valid target!")
                                time.sleep(1)
                                continue

                            skilluse(party, enemy, party[baton], group[ord(aim) - 65], useitem, [pgraveyard, egraveyard])
                            time.sleep(1)

                            if hpt > 0:
                                hpt -= 1
                            else:
                                pt -= 1

                elif unitmenu == "e":
                    if pt > 0:
                        pt -= 1
                        hpt += 1
                    else:
                        hpt -= 1


                else:
                    if unitmenu in glossary:
                        print(glossary[unitmenu])
                        input("")
                    else:
                        print("You can't do that yet")
                        time.sleep(1)
                    continue

                for i in range(len(pgraveyard)):
                    if pgraveyard[i].hp > 0:
                        party.append(pgraveyard[i])
                        pgraveyard.remove(pgraveyard[i])

                baton += 1



        elif partymenu == "b":
            print("Who will you talk to?")
            for i in range(len(enemy)):
                print(chr(i + 65) + ")", enemy[i].name)
            aim = input().upper()
            if len(aim) != 1:
                if aim.lower() in glossary:
                    print(glossary[aim.lower()])
                    input("")
                else:
                    print("That is not a valid target!")
                    time.sleep(1)
                continue
            elif ord(aim) - 65 >= len(enemy):
                print("That is not a valid target!")
                time.sleep(1)
                continue
            elif len(enemy[ord(aim)-65].script) == 0:
                print("This enemy does not yet have dialogue")
                time.sleep(1)
                continue
            result = enemy[ord(aim)-65].script[random.randint(0, len(enemy[ord(aim)-65].script)-1)]()
            if result == "agg":
                pt = 0
                hpt = 0
            elif result == "flee":
                print(enemy[ord(aim)-65], "left the battle!")
                enemy.remove(enemy[ord(aim)-65])
                if result == "rec":
                    party.append(enemy[ord(aim)-65])
                    enemy.remove(enemy[ord(aim)-65])
                elif turn == "none":
                    if enemy[ord(aim)-65].hp <= 0:
                        egraveyard.append(enemy[ord(aim)-65])
                        enemy.remove(enemy[ord(aim)-65])
                    time.sleep(1)
                    continue
            time.sleep(1)
            continue
        elif partymenu == "c":
            print("Who do you want to analyze?")
            for i in range(len(combatants)):
                print(chr(i + 65) + ")", combatants[len(combatants)-i-1].name)
                if i == len(enemy)-1:
                    print("\n")
            choose = input().upper()
            if len(str(choose)) != 1:
                if choose.lower() in glossary:
                    print(glossary[partymenu])
                    input("")
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
                time.sleep(1)
                continue




        elif partymenu == "e":
            print("You can't run from this battle!")
            time.sleep(1)
            continue

        elif partymenu != "d":
            if partymenu in glossary:
                print(glossary[partymenu])
                input("")
            else:
                print("Not a valid action")
                time.sleep(1)
            continue




        if len(enemy) < 1:
            print("You won the battle")
            return True

        print("[ENEMY TURN]")
        Descartes(enemy, party, egraveyard, pgraveyard)
        turn +=1
        pt = len(party)
        for i in range(len(combatants)):
            for j in range(3):
                if combatants[i].buffs[effects[j]]["dur"] > 0:
                    combatants[i].buffs[effects[j]]["dur"] -= 1




        if len(party) < 1 or player not in party:
            print("enemies win")
            return False






