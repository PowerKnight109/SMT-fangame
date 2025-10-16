from Formulas import accformula, dmgformula, healformula, ailformula, ailrecformula
import math
import random

class skill:
    def __init__(self, name, element, power, cost, friendly, AOE ):
        self.name = name
        self.element = element
        self.power = power
        self.cost = cost
        self.friendly = friendly
        self.AOE = AOE

class cstrike(skill):
    def __init__(self):
        super().__init__("Strike", "Physical", 100, 0, False, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Physical", 100, 0)
            target.hp -= damage[0]
            print(target.name, "took", damage[0], "points of damage!")
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class cagi(skill):
    def __init__(self):
        super().__init__("Agi", "Fire", 130, 10, False, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Fire", 130, 0)
            print(target.name, "took", damage[0], "points of damage!")
            target.hp -= damage[0]
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class czio(skill):
    def __init__(self):
        super().__init__("Zio", "Lightning", 130, 10, False, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Lightning", 130, 0)
            print(target.name, "took", damage[0], "points of damage!")
            target.hp -= damage[0]
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class cbufu(skill):
    def __init__(self):
        super().__init__("Bufu", "Ice", 130, 10, False, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Ice", 130, 0)
            print(target.name, "took", damage[0], "points of damage!")
            target.hp -= damage[0]
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class czan(skill):
    def __init__(self):
        super().__init__("Zan", "Force", 130, 10, False, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Force", 130, 0)
            print(target.name, "took", damage[0], "points of damage!")
            target.hp -= damage[0]
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class cmudo(skill):
    def __init__(self):
        super().__init__("Mudo", "Dark", 140, 15, False, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Dark", 140, 0)
            print(target.name, "took", damage[0], "points of damage!")
            target.hp -= damage[0]
            if damage[1]:
                if ailformula(user, target, "Dark", 40) >= random.randint(0, 100):
                    print("CORRUPTED!")
                    target.hp = 0
                return 2
            else:
                return 1
        else:
            return 0

class cdia(skill):
    def __init__(self):
        super().__init__("Dia", "Heal", 100, 8, True, False)
    def use(self, user, target):
        heal = healformula(user, target, 10, 0.15)
        print(target.name, "recovered", heal, "points of damage!")
        target.hp += heal
        if target.hp > target.mxhp:
            target.hp = target.mxhp

class ctarukaja(skill):
    def __init__(self):
        super().__init__("Tarukaja", "Support", 0, 10, True, False)
    def use(self, user, target):
        if target.buffs["taru"]["stage"] >= 2:
            print("But their offensive stats were already maxed out!")
            target.buffs["taru"]["dur"] = 4
        else:
            print(target.name+"'s attack rose by one rank!")
            target.buffs["taru"]["stage"] += 1
            target.buffs["taru"]["dur"] = 4

class csukukaja(skill):
    def __init__(self):
        super().__init__("Sukukaja", "Support", 0, 10, True, False)
    def use(self, user, target):
        if target.buffs["suku"]["stage"] >= 2:
            print("But their evasive stats were already maxed out!")
            target.buffs["suku"]["dur"] = 4
        else:
            print(target.name+"'s accuracy and evasion rose by one rank!")
            target.buffs["suku"]["stage"] += 1
            target.buffs["suku"]["dur"] = 4

class crakunda(skill):
    def __init__(self):
        super().__init__("Rakunda", "Support", 0, 10, False, False)
    def use(self, user, target):
        if target.buffs["suku"]["stage"] <= -2:
            print("But their defensive stats were already at rock bottom!")
            target.buffs["raku"]["dur"] = 4
        else:
            print(target.name+"'s defence was lowered by one rank!")
            target.buffs["raku"]["stage"] -= 1
            target.buffs["raku"]["dur"] = 4

class cmarin_karin(skill):
    def __init__(self):
        super().__init__("Marin Karin", "Charm", 0, 10, False, False)
    def use(self, user, target):
        if ailformula(user, target, "Charm", 70) >= random.randint(0, 100):
            print(target.name, "became charmed!")
            target.element["Charm"]["dur"] = 1
            target.element["Charm"]["inflict"] += 1
            if target.element["Charm"]["res"] == -0.25:
                return -1
            else:
                return 1

        else:
            print("but it failed!")
            return 1

class chellish_slash(skill):
    def __init__(self):
        super().__init__("Hellish Slash", "Physical", 55, 5, False, False)
    def use(self, user, target):
        if accformula(user, target, 50):
            for i in range(4):
                damage = dmgformula(user, target,"Physical", 55, 0)
                print(target.name, "took", damage[0], "points of damage!")
                target.hp -= damage[0]
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

strike = cstrike()
agi = cagi()
zio = czio()
bufu = cbufu()
zan = czan()
mudo = cmudo()
dia = cdia()
tarukaja = ctarukaja()
sukukaja = csukukaja()
rakunda = crakunda()
marin_karin = cmarin_karin()
hellish_slash = chellish_slash()

ailments = [marin_karin]

def skilluse(allies, enemies, user, target, move):
    x = 0
    ailrecformula(user)
    if user.element["Poison"]["dur"] > 0:
        root = math.floor(user.atk + 5)
        a = random.randint(0, math.floor(root / 10 - 1))
        if a < 0:
            a = 0
        b = random.randint(0, 3)
        psndmg = root + a + b
        user.hp -= psndmg
        if user.hp <= 0:
            print(user.name, "died!")
            allies.remove(target)

    ailchance = random.randint(0, 100)
    if user.element["Sleep"]["dur"] > 0:
        print(user.name, "is fast asleep!")
        x = 1
    elif user.element["Confusion"]["dur"] > 0 and ailchance <= 15:
        print(user.name, "is too confused to move!")
        x = 1
    elif user.element["Charm"]["dur"] > 0 and ailchance <= 20:
        print(user.name, "is too charmed to move!")
        x = 1
    else:
        if user.element["Mirage"]["dur"] > 0 and ailchance <= 50:
            combatants = allies + enemies
            target = combatants[random.randint(0, len(combatants)-1)]
        elif user.element["Confusion"]["dur"] > 0 and ailchance <= 50:
            target = allies[random.randint(0, len(allies)-1)]
        elif user.element["Charm"]["dur"] > 0 and ailchance <=50:
            charmskill = []
            for i in range(len(user.skills)):
                if user.skills[i].friendly:
                    charmskill.append(user.skills[i])
            if len(charmskill) < 1:
                print(user.name, "is too charmed to move!")
                x = 1
                return x
            else:
                move = charmskill[random.randint(0, len(charmskill)-1)]
                target = enemies[random.randint(0, len(enemies)-1)]

        if target == user:
            print(user.name, "used", move.name, "on itself!")
        else:
            print(user.name, "used", move.name, "on", target.name + "!")
        user.mp -= move.cost

        if move.element == "Heal" or move.element == "Support":
            move.use(user, target)
            x = 1
        else:
            if target.element[move.element]["res"] == 1:
                print("NULLIFIED")
                x = 2
            elif target.element[move.element]["res"] > 1:
                if target.element[move.element]["res"] > 2:
                    print("REPELLED")
                    pure = dmgformula(user, user, "Almighty", move.power, -999)[0]
                    print(user.name, "took", pure, "points of damage!")
                    user.hp -= pure
                    if user.hp <= 0:
                        print(target.name, "died!")
                        allies.remove(target)

                else:
                    pure = dmgformula(user, user, "Almighty", move.power, -999)[0]
                    print("DRAINED")
                    target.hp += pure
                x = -2

            else:
                result = move.use(user, target)
                if result == 0:
                    print("MISS")
                    x = 2
                else:
                    if result == 1:
                        x = 1
                    elif result == 2:
                        x = -1
                    if target.hp <= 0:
                        print(target.name, "died!")
                        enemies.remove(target)

                    elif target.element["Sleep"]["dur"] > 0:
                        print(target.name, "woke up")
                        target.element["Sleep"]["dur"] = 0




    return x