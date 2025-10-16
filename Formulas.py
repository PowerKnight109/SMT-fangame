import random
import math


def accformula(attacker, evader, move):
    if evader.element["Confusion"]["dur"] > 0 or evader.element["Charm"]["dur"] > 0 or evader.element["Sleep"]["dur"] > 0:
        return True
    else:
        root = (attacker.agl*3 + attacker.luck + 20)/(evader.agl*3 + evader.luck +20)
        if root < 1:
            base = 1 - (0.5**(1-root)/30 + (1-root)/12)
        else:
            base = 1 + 0.5**(root-1)/15 + (root-1)*2/3

        sukuvalues = [0.85, 0.9, 1, 1.1, 1.2]
        raw = base * move * sukuvalues[2+attacker.buffs["suku"]["stage"]] * sukuvalues[2-evader.buffs["suku"]["stage"]]

        if raw < 99:
            scaled = raw
        elif raw < 114:
            scaled = (raw - 99)/30 + 99
        elif raw < 149:
            scaled = (raw - 114)/70 + 99.5
        else:
            scaled = 100

        if attacker.element["Mirage"]["dur"] != 0:
            scaled = scaled*0.5

        if scaled >= random.randint(0, 32767)/32767 * 100:
            return True
        else:
            return False

def critformula(attacker, defender, move):
    root = (attacker.luck+10)/(defender.luck+10)
    if root > 4:
        root = 4
    base = ((attacker.lv+10)/(defender.lv+10) + root**2)*3

    if attacker.lv <= defender.lv:
        correction = 1 - (0.5**(defender.lv-attacker.lv)/60 + (defender.lv-attacker.lv)/120)
        if correction < 0.5:
            correction = 0.5
    elif attacker.lv - defender.lv < 11:
        correction = 1 + (attacker.lv-defender.lv)/40
    else:
        correction = 1.25 + (0.5**(attacker.lv-defender.lv-10)/60 + (attacker.lv-defender.lv-10)/120)
        if correction > 1.5:
            correction = 1.5

    critrate = math.floor((move + base)*correction)
    if critrate > random.randint(0, 100):
        print("CRITICAL")
        return True


def dmgformula(attacker, defender, type, move, crit):
    bonus = False
    if type == "physical":
        stat = attacker.str
    else:
        stat = attacker.mag

    if (attacker.lv + 10) >= stat:
        assault = (attacker.lv + 10) + stat
    else:
        assault = 0.5 ** (stat - (attacker.lv + 10)) / 2 + stat / 2 + (attacker.lv + 10) * 3 / 2

    if assault - defender.vit <= assault / 2:
        base = assault * 2 / 3 - defender.vit / 3 - 0.5 ** (defender.vit - assault / 2) / 3
    elif assault - defender.vit <= assault * 3 / 4:
        base = assault - defender.vit
    else:
        base = assault * 5 / 6 - defender.vit / 3 + 0.5 ** (assault / 4 - defender.vit) / 3
    if base < 1:
        base = 1

    guard = 1
    if defender.guard:
        guard = 0.8


    pot = [0.45, 0.53, 0.57, 0.61, 0.65, 0.75, 0.8, 0.85, 0.9, 1, 1.1, 1.15, 1.2, 1.25, 1.35, 1.39, 1.43, 1.47, 1.55]
    stab = pot[9 - attacker.element[type]["aff"]]
    efficacy = 1
    efficacy -= defender.element[type]["res"]
    if efficacy >= 1.25:
        print("WEAKNESS")
    if efficacy < 1:
        print("RESIST")
    if type == "Physical" and efficacy != 0.5 and attacker.name != defender.name:
        if critformula(attacker, defender, crit):
            efficacy += 0.5
    if efficacy > 1:
        bonus = True

    if attacker.lv + defender.lv <= 30:
        sum = 0
    elif attacker.lv + defender.lv <= 130:
        sum = (attacker.lv + defender.lv - 30) / 1000
    else:
        sum = 0.1
    if defender.lv - attacker.lv > 2:
        correct = 1 - 0.5 ** (defender.lv / attacker.lv - 1) * sum * (defender.lv - attacker.lv - 2)
        if correct < 0.5:
            correct = 0.5
    elif attacker.lv - defender.lv > 2:
        correct = 1 + 0.5 ** (1 - defender.lv / attacker.lv) * sum * (attacker.lv - defender.lv - 2) * 1.2
        if correct > 1.5:
            correct = 1.5
    else:
        correct = 1

    taruvalues = [0.7, 0.8, 1, 1.2, 1.4]
    rakuvalues = [1.4, 1.2, 1, 0.8, 0.7]

    min = math.floor(base * (move / 100) * (taruvalues[2+attacker.buffs["taru"]["stage"]]) * (rakuvalues[2+defender.buffs["raku"]["stage"]]) * stab * efficacy * correct * guard)
    if min < 1:
        min = 1
    a = math.floor((min / 10) - 1)
    if a < 0:
        a = 0
    damage = min + random.randint(0, a) + random.randint(0, 3)

    return [damage, bonus]


def ailformula(attacker, defender, type, move):
    if attacker.luck/defender.luck <0.5:
        rate = 0.25 - 0.5**(0.5 - attacker.luck/defender.luck)/20 + (attacker.luck/defender.luck)/2
    elif attacker.luck/defender.luck <= 1.5:
        rate = attacker.luck/defender.luck
    else:
        rate = 0.5**(attacker.luck/defender.luck) + 0.275

    pot = [0.4, 0.5, 0.55, 0.6, 0.65, 0.75, 0.8, 0.85, 0.9, 1, 1.1, 1.15, 1.2, 1.25, 1.35, 1.4, 1.45, 1.5, 1.6]
    potmod = pot[9-attacker.element["Ailment"]["aff"]]

    if type == "Dark" or type == "Light":
        resistance = 1
    else:
        resistance = (1 - defender.element[type]["res"]) - defender.element[type]["inflict"] * ((1 - defender.element[type]["res"]) * 2 + 1) / 10

    guard = 1
    if defender.guard:
        if defender.element[type]["res"] == -0.25:
            guard = 0.4
        else:
            guard = 0.5

    total = math.floor(rate * move * potmod * resistance * guard)
    if total > 100:
        total = 100
    return total

def ailrecformula(patient):
    root = 4 + (patient.lv-1)/2
    for i in range(11, 17):
        if patient.element[list(patient.element)[i]]["dur"] > 0:
            if patient.element[list(patient.element)[i]]["dur"] > 2:
                if list(patient.element)[i] == "Poison" or list(patient.element)[i] == "Sleep":
                    co = 1
                else:
                    co = 15
                base = co*patient.luck/root
                if base < co/2:
                    base = co/2
                elif base > 85:
                    base = 85
                rate = math.floor(base + 15*patient.element[list(patient.element)[i]]["dur"])
                if random.randint(0, 100) < rate:
                    patient.element[list(patient.element)[i]]["dur"] = 0
                    print(patient.name, "recovered from", list(patient.element)[i]+"!")

            else:
                patient.element[list(patient.element)[i]]["dur"] += 1

def healformula(user, target, move, perc):
    root = target.mxhp*perc + move
    pot = [0.6, 0.75, 0.8, 0.85, 0.9, 1, 1.1, 1.15, 1.2, 1.25, 1.4]
    recover = root * pot[5 + user.element["Heal"]["aff"]]
    return math.floor(recover)