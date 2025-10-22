import random
import time
from Skills import ailments, skilluse, strike

schema = {"Weak": {}, "Res" : {}, "Null": {},  "Rflct": {}, "Drn": {}}

def memory(word):
    antibodies = 0
    for i in range((len(schema))):
        for j in range(len(schema[list(schema)[i]])):
            if word in schema[list(schema)[i]][list(schema[list(schema)[i]])[j]]:
                if i == 0:
                    antibodies = -1
                elif i == 1:
                    antibodies = 1
                elif i == 2:
                    antibodies = 2
                elif i == 3:
                    antibodies = 3
    return antibodies


def Descartes(enemies, party):
    pt = len(enemies)
    hpt = 0
    relay = -1
    while len(enemies) > 0 and len(party) > 0 and (pt > 0 or hpt > 0):
        prioritylist = [[party[0], -9999, strike]]
        relay += 1
        if relay > len(enemies)-1:
            relay = 0
        if enemies[relay].play/10 > random.randint(0, 100):
            print(enemies[relay].name, "got distracted and missed their turn!")
            pt -= 1
            continue
        elif enemies[relay].coward/2 > random.randint(0, 1000):
            print(enemies[relay].name, "got too scared to move!")
            pt -= 1
            continue

        for j in range(len(enemies[relay].skills)):
            x = 0
            #bounty = 100
            if enemies[relay].skills[j].cost > enemies[relay].mp or (enemies[relay].skills[j].cost > 0 and enemies[relay].element["Seal"]["dur"] > 0):
                x = -999
                base = 0

            elif enemies[relay].skills[j] in ailments:
                base = enemies[relay].element["Ailment"]["aff"]*5 + 5
            elif enemies[relay].skills[j].element == "Support":
                base = enemies[relay].element["Support"]["aff"]*5 + 5
            else:
                base = enemies[relay].element[enemies[relay].skills[j].element]["aff"]*5 + enemies[relay].skills[j].power/10
            if enemies[relay].skills[j].friendly:
                group = enemies
            else:
                group = party

            for k in range(len(group)):
                reward = 1
                if group == enemies:
                    if enemies[relay].skills[j].name == "Patra":
                        for i in range(11, 16):
                            if group[k].element[list(group[k].element)[i]]["dur"] > 0:
                                x += 60
                               # bounty += 40

                    elif enemies[relay].skills[j].name == "Dia" or enemies[relay].skills[j].name == "Media":
                        x += (100-(group[k].hp/group[k].mxhp)*100)/2
                        if enemies[relay].hp == enemies[relay].mxhp:
                            x -= 999
                        if enemies[relay].element["Heal"]["inflict"] > 0:
                            x -= 60
                            enemies[relay].element["Heal"]["inflict"] -= 1


                        # if enemies[relay] == group[k]:
                        #     x += enemies[relay].coward/2
                        #     x -= enemies[relay].loyal/2
                        # else:
                        #     x += enemies[relay].loyal/2

                    if enemies[relay].skills[j].element == "Support" and group[k].buffs["taru"]["stage"] <= 0 and group[k].buffs["raku"]["stage"] <= 0 and group[k].buffs["suku"]["stage"] <= 0:
                        x += 40
                    elif enemies[relay].skills[j].element == "Support" and group[k].buffs["taru"]["stage"] >= 2 and group[k].buffs["raku"]["stage"] >= 2 and group[k].buffs["suku"]["stage"] >= 2:
                        x -= 60



                    if enemies[relay] == enemies[k]:
                        x += enemies[relay].coward/2
                        x -= enemies[relay].loyal/2
                    else:
                        x += enemies[relay].loyal/2

                elif enemies[relay].skills[j].element == "Support":
                    x += enemies[relay].play/2
                    if group[k].buffs["taru"]["stage"] >= 0 and group[k].buffs["suku"]["stage"] >= 0 and group[k].buffs["raku"]["stage"] >=0:
                        x += 40
                    elif group[k].buffs["taru"]["stage"] <= -2 and group[k].buffs["suku"]["stage"] <= -2 and group[k].buffs["raku"]["stage"] <= -2:
                        x -= 60
                    x += enemies[relay].play/2

                else:
                    chem = memory(enemies[relay].skills[j].element)
                    if chem == -1:
                        if pt > 0:
                            x += 60
                            reward = 1.5
                        else:
                            x += 40
                    elif chem == 2:
                        x -= 80
                        reward = 0
                    elif chem == 3:
                        x -= 120
                        reward = 0

                    if enemies[relay].skills[j] in ailments:
                        for d in range(11, 17):
                            if group[k].element[list(group[k].element)[d]]["dur"] > 0:
                                x -= 60

                    else:
                        x -= enemies[relay].coward/2
                        x -= enemies[relay].play/2
                        x += (100 - (group[k].hp / group[k].mxhp) * 100)/2
                        x += group[k].buffs["taru"]["stage"] * 20
                        if group[k].element["Sleep"]["dur"] > 0:
                            x -= 30



                if enemies[relay].skills[j].name == "Sukunda" or enemies[relay].skills[j].name == "Masakunda" or enemies[relay].skills[j].name == "Sakukaja" or enemies[relay].skills[j].name == "Masukukaja":
                    x += enemies[relay].play/2

                if pt >= 2:
                    risk = 1
                elif pt == 1:
                    risk = 1.3
                elif hpt > 1:
                    risk = 1.6
                elif hpt == 1:
                    risk = 2


                final = (base+x)*reward/risk

                if enemies[relay].skills[j] not in ailments:
                    final += enemies[relay].element[enemies[relay].skills[j].element]["aff"]*10
                else:
                    final += enemies[relay].element["Ailment"]["aff"]*10
                if random.randint(0, 1) == 0:
                    final -= final * (random.randint(10, 20) / 100)
                else:
                    final += final*(random.randint(10, 20)/100)

                data = [group[k], final, enemies[relay].skills[j]]

                for d in range(len(prioritylist)):
                    if prioritylist[d][1] > data[1]:
                        prioritylist.insert(d, data)
                if data not in prioritylist:
                        prioritylist.append(data)

        for i in range(len(prioritylist)):
            print(prioritylist[i][2].name, prioritylist[i][1])
        y = skilluse(enemies, party, enemies[relay], prioritylist[len(prioritylist)-1][0], prioritylist[len(prioritylist)-1][2])
        time.sleep(1)
        if prioritylist[len(prioritylist)-1][2].element == "Heal":
            enemies[relay].element["Heal"]["inflict"] = 2
        if y == -2:
            pt = 0
            hpt = 0
        elif y == -1:
            if pt > 0:
                pt -= 1
                hpt += 1
            else:
                hpt -= 1
        else:
            for j in range(y):
                if hpt == 0:
                    pt -= 1
                else:
                    hpt -= 1


