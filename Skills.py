from Formulas import accformula, dmgformula, critformula, healformula, ailformula, ailrecformula
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
        super().__init__("Strike", "Physical", 100, 0, 0, False)
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

class clunge(skill):
    def __init__(self):
        super().__init__("Lunge", "Physical", 145, 5, 0, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Physical", 145, 0)
            target.hp -= damage[0]
            print(target.name, "took", damage[0], "points of damage!")
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class cbestial_bite(skill):
    def __init__(self):
        super().__init__("Bestial Bite", "Physical", 130, 10, 0, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            if critformula(user, target, 0):
                damage = dmgformula(user, target, "Physical", 200, 999)
            else:
                damage = dmgformula(user, target, "Physical", 130, -999)
            target.hp -= damage[0]
            print(target.name, "took", damage[0], "points of damage!")
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0

class cgram_slice(skill):
    def __init__(self):
        super().__init__("Gram Slice", "Physical", 140, 10, 0, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Physical", 140, 30)
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
        super().__init__("Agi", "Fire", 130, 10, 0, False)
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
        super().__init__("Zio", "Lightning", 130, 10, 0, False)
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
        super().__init__("Bufu", "Ice", 130, 10, 0, False)
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
        super().__init__("Mudo", "Dark", 140, 15, 0, False)
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

class chama(skill):
    def __init__(self):
        super().__init__("Hama", "Light", 140, 15, 0, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Light", 140, 0)
            print(target.name, "took", damage[0], "points of damage!")
            target.hp -= damage[0]
            if damage[1]:
                if ailformula(user, target, "Light", 40) >= random.randint(0, 100):
                    print("BANISHED!")
                    target.hp = 0
                return 2
            else:
                return 1
        else:
            return 0

class clife_drain(skill):
    def __init__(self):
        super().__init__("Life Drain", "Almighty", 120, 10, 0, False)
    def use(self, user, target):
        if accformula(user, target, 98):
            damage = dmgformula(user, target,"Almighty", 120, 0)
            print(user.name, "drained", damage[0], "points of damage from", target.name+"!")
            target.hp -= damage[0]
            user.hp += damage[0]
            if user.hp > user.mxhp:
                user.hp = user.mxhp
            if damage[1]:
                return 2
            else:
                return 1
        else:
            return 0
#
# class cmegido(skill):
#     def __init__(self):
#         super().__init__("Megido", "Almighty", 125, 40, 0, False)
#     def use(self, user, target):
#         if accformula(user, target, 98):
#             damage = dmgformula(user, target,"Almighty", 125, 0)
#             print(target.name, "took", damage[0], "points of damage!")
#             target.hp -= damage[0]
#             if damage[1]:
#                 return 2
#             else:
#                 return 1
#         else:
#             return 0
#
#
# class cmegidola(skill):
#     def __init__(self):
#         super().__init__("Megidola", "Almighty", 160, 40, 0, False)
#     def use(self, user, target):
#         if accformula(user, target, 98):
#             damage = dmgformula(user, target,"Almighty", 160, 0)
#             print(target.name, "took", damage[0], "points of damage!")
#             target.hp -= damage[0]
#             if damage[1]:
#                 return 2
#             else:
#                 return 1
#         else:
#             return 0

class cdia(skill):
    def __init__(self):
        super().__init__("Dia", "Heal", 100, 8, 1, False)
    def use(self, user, target):
        heal = healformula(user, target, 10, 0.15)
        print(target.name, "recovered", heal, "points of damage!")
        target.hp += heal
        if target.hp > target.mxhp:
            target.hp = target.mxhp

class cpatra(skill):
    def __init__(self):
        super().__init__("Patra", "Heal", 100, 8, 1, False)
    def use(self, user, target):
        fixed = False
        for i in range(11, len(target.element)):
            if target.element[list(target.element)[i]]["dur"] > 0:
                target.element[list(target.element)[i]]["dur"] = 0
                print(target.name, "was cured of", list(target.element)[i] + "!")
                fixed = True
        if not fixed:
            print("But", target.name, "was not suffering from any status effects")

class ctarukaja(skill):
    def __init__(self):
        super().__init__("Tarukaja", "Support", 0, 10, 1, False)
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
        super().__init__("Sukukaja", "Support", 0, 10, 1, False)
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
        super().__init__("Rakunda", "Support", 0, 10, 0, False)
    def use(self, user, target):
        if target.buffs["suku"]["stage"] <= -2:
            print("But their defensive stats were already at rock bottom!")
            target.buffs["raku"]["dur"] = 4
        else:
            print(target.name+"'s defence was lowered by one rank!")
            target.buffs["raku"]["stage"] -= 1
            target.buffs["raku"]["dur"] = 4

class cdormina(skill):
    def __init__(self):
        super().__init__("Dormina", "Sleep", 0, 10, 0, False)
    def use(self, user, target):
        if ailformula(user, target, "Sleep", 80) >= random.randint(0, 100):
            print(target.name, "fell asleep!")
            target.element["Sleep"]["dur"] = 1
            target.element["Sleep"]["inflict"] += 1
            if target.element["Sleep"]["res"] == -0.25:
                return 2
            else:
                return 1
        else:
            print("but it failed!")
            return 1

class cdustoma(skill):
    def __init__(self):
        super().__init__("Dustoma", "Mirage", 0, 10, 0, False)
    def use(self, user, target):
        if ailformula(user, target, "Mirage", 75) >= random.randint(0, 100):
            print(target.name, "had their vision obscured!")
            target.element["Mirage"]["dur"] = 1
            target.element["Mirage"]["inflict"] += 1
            if target.element["Mirage"]["res"] == -0.25:
                return 2
            else:
                return 1
        else:
            print("but it failed!")
            return 1

class cmarin_karin(skill):
    def __init__(self):
        super().__init__("Marin Karin", "Charm", 0, 10, 0, False)
    def use(self, user, target):
        if ailformula(user, target, "Charm", 70) >= random.randint(0, 100):
            print(target.name, "became charmed!")
            target.element["Charm"]["dur"] = 1
            target.element["Charm"]["inflict"] += 1
            if target.element["Charm"]["res"] == -0.25:
                return 2
            else:
                return 1
        else:
            print("but it failed!")
            return 1

class cpoisma(skill):
    def __init__(self):
        super().__init__("Poisma", "Poison", 0, 10, 0, False)
    def use(self, user, target):
        if ailformula(user, target, "Poison", 85) >= random.randint(0, 100):
            print(target.name, "became poisoned!")
            target.element["Poison"]["dur"] = 1
            target.element["Poison"]["inflict"] += 1
            if target.element["Poison"]["res"] == -0.25:
                return 2
            else:
                return 1
        else:
            print("but it failed!")
            return 1

class cpulinpa(skill):
    def __init__(self):
        super().__init__("Pulinpa","Confusion", 0, 10, 0, False)
    def use(self, user, target):
        if ailformula(user, target, "Confusion", 70) >= random.randint(0, 100):
            print(target.name, "became confused!")
            target.element["Confusion"]["dur"] = 1
            target.element["Confusion"]["inflict"] += 1
            if target.element["Confusion"]["res"] == -0.25:
                return 2
            else:
                return 1
        else:
            print("but it failed!")
            return 1

class cmakajama(skill):
    def __init__(self):
        super().__init__("Makajama", "Seal", 0, 10, 0, False)
    def use(self, user, target):
        if ailformula(user, target, "Seal", 65) >= random.randint(0, 100):
            print(target.name, "became sealed!")
            target.element["Seal"]["dur"] = 1
            target.element["Seal"]["inflict"] += 1
            if target.element["Seal"]["res"] == -0.25:
                return 2
            else:
                return 1
        else:
            print("but it failed!")
            return 1


class chellish_slash(skill):
    def __init__(self):
        super().__init__("Hellish Slash", "Physical", 55, 5, 0, False)
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


class clife_stone(skill):
    def __init__(self):
        super().__init__("Life Stone", "Heal", 100, 3, 1, False)
    def use(self, user, target):
        print(target.name, "had their health restored by", str(math.floor(target.mxhp*0.3))+"!")
        target.hp += (target.mxhp*0.3)
        target.hp = math.floor(target.hp)
        if target.hp > target.mxhp:
            target.hp = target.mxhp

class cchakra_drop(skill):
    def __init__(self):
        super().__init__("Chakra Drop", "Heal", 100, 3, 1, False)
    def use(self, user, target):
        print(target.name, "regained 50MP!")
        target.mp += 50
        if target.mp > target.mxmp:
            target.mp = target.mxmp

class camrita_soda(skill):
    def __init__(self):
        super().__init__("Amrita Soda", "Heal", 100, 3, 1, False)
    def use(self, user, target):
        fixed = False
        for i in range(11, len(target.element)):
            if target.element[list(target.element)[i]]["dur"] > 0:
                target.element[list(target.element)[i]]["dur"] = 0
                print(target.name, "was cured of", list(target.element)[i] + "!")
                fixed = True
        if not fixed:
            print("But", target.name, "was not suffering from any status effects")

class crevival_bead(skill):
    def __init__(self):
        super().__init__("Revival Bead", "Heal", 100, 1, 2, False)
    def use(self, user, target):
        print(target.name, "was revived!")
        target.hp = target.mxhp/2

strike = cstrike()
lunge = clunge()
bestial_bite = cbestial_bite()
gram_slice = cgram_slice()
agi = cagi()
zio = czio()
bufu = cbufu()
zan = czan()
mudo = cmudo()
hama = chama()
life_drain = clife_drain()
# megido = cmegido()
# megidola = cmegidola()
dia = cdia()
patra = cpatra()
tarukaja = ctarukaja()
sukukaja = csukukaja()
rakunda = crakunda()
dormina = cdormina()
dustoma = cdustoma()
marin_karin = cmarin_karin()
poisma = cpoisma()
pulinpa = cpulinpa()
makajama = cmakajama()
hellish_slash = chellish_slash()

life_stone = clife_stone()
chakra_drop = cchakra_drop()
amrita_soda = camrita_soda()
revival_bead = crevival_bead()

ailments = [dormina, dustoma, marin_karin, poisma, pulinpa, makajama]
effects = ["taru", "raku", "suku", "Sleep", "Mirage", "Poison", "Confusion", "Charm", "Seal"]
items = [life_stone, chakra_drop, amrita_soda, revival_bead]

def skilluse(allies, enemies, user, target, move, grave):
    #grave[0] = user's graveyard, grave[1] = target graveyard
    x = 1
    ailrecformula(user)
    if user.element["Poison"]["dur"] > 0:
        root = math.floor(user.str + 5)
        a = random.randint(0, math.floor(root / 10 - 1))
        if a < 0:
            a = 0
        b = random.randint(0, 3)
        psndmg = root + a + b
        print(user.name, "took", psndmg, "damage from being poisoned!")
        user.hp -= psndmg

    if user.hp > 0:
        ailchance = random.randint(0, 100)
        if user.element["Sleep"]["dur"] > 0:
            print(user.name, "is fast asleep!")

        elif user.element["Confusion"]["dur"] > 0 and ailchance <= 15:
            print(user.name, "is too confused to move!")

        elif user.element["Charm"]["dur"] > 0 and ailchance <= 20:
            print(user.name, "is too charmed to move!")

        else:
            if user.element["Mirage"]["dur"] > 0 and ailchance <= 50:
                combatants = allies + enemies
                target = combatants[random.randint(0, len(combatants)-1)]
            elif user.element["Confusion"]["dur"] > 0 and ailchance <= 50:
                target = allies[random.randint(0, len(allies)-1)]
            elif user.element["Charm"]["dur"] > 0 and ailchance <=50:
                charmskill = []
                for i in range(len(user.skills)):
                    if user.skills[i].friendly == 1:
                        charmskill.append(user.skills[i])
                if len(charmskill) < 1:
                    print(user.name, "is too charmed to move!")
                    return x
                else:
                    move = charmskill[random.randint(0, len(charmskill)-1)]
                    target = enemies[random.randint(0, len(enemies)-1)]

            if target == user:
                print(user.name, "used", move.name, "on itself!")
            else:
                print(user.name, "used", move.name, "on", target.name + "!")
            if move in items:
                move.cost -= 1
            else:
                user.mp -= move.cost

            if move.element == "Heal" or move.element == "Support":
                move.use(user, target)
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

                        elif target.element["Sleep"]["dur"] > 0:
                            print(target.name, "woke up")
                            target.element["Sleep"]["dur"] = 0
    loss = 0
    for i in range(len(allies)):
        if allies[i-loss].hp <= 0:
            print(allies[i-loss].name, "died!")
            grave[0].append(allies[i-loss])
            allies.remove(allies[i-loss])
            loss += 1
    loss = 0
    for i in range(len(enemies)):
        if enemies[i-loss].hp <= 0:
            print(enemies[i-loss].name, "died!")
            grave[1].append(enemies[i-loss])
            enemies.remove(enemies[i-loss])
            loss += 1
    return x