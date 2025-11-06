import time
import random
import math
from Formulas import dmgformula
from Skills import items
from CharacterSheets import player, pixie, pixie1, slime, preta, daemon
from Dictionary import lookup


class bargaintxt:
    def __init__(self, thinking, start, middle, end, gifted, out, pity, frust, angry, content, sated, thief, mugged, broke, snap, captured, betrayed):
        self.think = thinking
        self.start = start
        self.middle = middle
        self.end = end
        self.gifted = gifted
        self.out = out
        self.pity = pity
        self.frust = frust
        self.angry = angry
        self.content = content
        self.sated = sated
        self.thief = thief
        self.mugged = mugged
        self.broke = broke
        self.snap = snap
        self.captured = captured
        self.betrayed = betrayed


pixied = bargaintxt("let's see here", "I'll take", ["a small portion of your", "a moderate amount of your", "a large portion of your", "one"], ["HP", "MP", "Macca", "Life Stone", "Chakra Drop", "Amrita Soda", "Revival Bead"], "Oh wow, thanks!", "Wait, you seriously don't have any?", 'Well that just won'+"'"+'t do!"\n"Here take one of mine, It'+"'"+'s not safe to be wondering out here without any', "God, you don't have anything do you?", "Don't you think you can cheap out on me!", "Yeah, you're probably right", "Alright, I think I'm satisfied for now", "Thanks for the gifts, idiot!", "Is this enough?", "You've taken everything I have!", 'No way in hell!', "I-i-i can be helpful! Just please don't kill me!", "OW! Why did you do that?")
monsterd = bargaintxt("LeMmE tHiNk", "GiMmE", ["A sMaLl bIt oF YoUr", "A nIcE cHuNk oF yOuR", "A mAsSiVe ChUnK oF yOuR", "A"], ['HP', 'MP', 'MaCcA', 'LiFe StOnE', 'ChAkRa DrOp', 'SoDa', 'ReViVal BeAd'], "AlRigHT!", "YoURe fLaT OUT?", "In tHaT caSe, TaKe thIs", "QuIT wASTinG mY TIMe!", "YoU PrIcK!", "AlRigHt, yOU gOT mE", "i'VE hAd my fiLL", "Get SCAmmEd, IdIoT!", "AlrIgHT, AlRiGHt, HeRE", "I'm fLAt bROke!", "ThAt's IT!", "AlRigHT, fIne", "Hey WaIt, Why'Re yOU hiTTinG ME!?")
toughd = bargaintxt("Let's see here", "Fork over", ["A small bit of your", "a nice piece of your", "A bunch of your", "one"], ["HP", "MP", 'MaCcA', "Life Stone", "Chakra Drop", "Amrita Soda", "Revival Bead"], "That's the stuff!", "You don't have ANY?", "Take one of mine then!", "Alright, I've had it with you!", "Stingy people like you PISS ME OFF!", "Fair enough", "I think that's enough", "Man, you're so gullible!", "Alright fine, take it", "You've bled me dry!", "I'll make you pay for trying that!", "Better than dying, I guess", "OW! The fuck's wrong with you!?")

def pixiec1(demon):
    print(pixie.image+"\n\nPIXIE:\n'WOW, A human!'\n'I've never seen a real life human before! Do you mind if I get a closer look?'")
    x = input("\nA) Of course\nB) Not sure I'm comfortable with that,\n").lower()
    if x == "a":
        y = random.randint(0, 100)
        if y <= 10:
            print("\nPIXIE:\n'Wow, humans are amazing! I think I'm going to join you from now on'")
            return "recruit"
        elif y <= 20:
            print("\nPIXIE:\n'Ha! You're too gullible!'")
            return "aggro"
        elif y <= 40:
            if y <= 30 and player.macca >= 0:
                print("\nPIXIE:\n'Tricked you!'")
                loss = random.randint(1, 30)
                if loss > player.macca:
                    loss = player.macca
                print("The pixie frisked you and stole", loss, "Macca!")
                player.macca -= loss
            else:
                stealables = []
                for i in range(len(items)):
                    if items[i].cost > 0:
                        stealables.append(items[i])
                if len(stealables) == 0:
                    print("\nPIXIE:\n'What? You don't have anything on you?'\n'How rude!'\n'Next time you try talking to a girl like me, make sure you're worth my time!'")
                else:
                    print("\nPIXIE:\n'Too easy!'")
                    stolen = stealables[random.randint(0, len(stealables)-1)]
                    print("The pixie stole 1", stolen.name, "from you!")
                    stolen.cost -= 1
            if random.randint(0, 100) <= 25:
                return "flee"
            else:
                return "none"
        else:
            print("\nPIXIE:\n'Thanks so much! All my friends are going to be SO jealous when I tell them I met a human in person!'")
            return pixier(demon)

    elif x == "b":
        if random.randint(0, 100) >= 75:
            print("\nPIXIE:\n'Oh alright then' :(")
            return "none"
        else:
            print("\nPIXIE:\n'You're no fun!'")
        return "aggro"
    else:
        lookup(x)
        return pixiec1(demon)

def pixiec2(demon):
    print(pixie.image + "\n\nPIXIE:\n'Whoa, you talked to me! Could you want me to join you?'\n'Okay then, let's talk!'\n'I'm  gonna ask you a question, so make sure you answer in a way that'd make me happy, okay?'")
    time.sleep(1)
    h = input("'So... do you think I'm cute?'\n\nA) You're cute\nB) Not really\nC) I'm leaving\n").lower()
    if h == "a":
        print("\nPIXIE:\n'Ahaha! Thanks!'")
        return pixier(demon)
    elif h == "b":
        print("\nPIXIE:\n'How rude!'")
        return "aggro"
    else:
        print("\nPIXIE:\n'Don't you dare turn away!'")
        return "aggro"

def pixier(demon):
    print("\n'So, what brings you out here anyway?'")
    ask = input("\nA) Looking for friends\nB) Looking for allies\nC) Looking for demons to kill\nD) Looking for Macca\nE) Looking for items\n").lower()
    y = random.randint(0, 100)
    if ask == "a":
        if y <= 10:
            print("\nPIXIE:\n'Well, good luck with that.'")
            return "flee"
        elif y <= 40:
            print("\nPIXIE:\n'I know! Why don't we be friends then?'\n'Doesn't that sound like such a good idea?'")
            return "recruit"
        else:
            print("\nPIXIE:\n'Hey now, if you want to be friends with me you've got to give me something to prove it first.'")
            z = bargaining("friend", 5, 50,  random.randint(1, 2), pixied, pixie)
            if z == "pass":
                return "recruit"
            else:
                return z
    elif ask == "b":
        if y <= 10:
            print("\nPIXIE:\n'Yeah right! I bet you're the type who views demons as nothing more than tools!'")
            print("'Well guess what? You aren't fooling me with that bullshit!'")
            return "aggro"
        elif y <= 60:
            print("\nPIXIE:\n'Idk, see I'm not really the fighting type.'\n'You'd probably be better off bothering some other demons if that's what you want.'")
            return "none"
        else:
            print("\nPIXIE:\n'You're trying to recruit allies?'\n'Well, in that case you should probably know that most demons aren't going to join for free'\n'Most are going to want you to offer something in return. I'll lead by example'")
            z = bargaining("recruit", random.randint(1,2), 50, random.randint(1, 2), pixied, pixie)
            if z == "pass":
                return "recruit"
            else:
                return z
    elif ask == "c":
        if y < 50:
            print("\nPIXIE:\n'Die scum!'")
            return "aggro"
        else:
            print("\nPIXIE:\n'Y-you aren't talking about me are you? You don't mean you want to k-k-KILL me?'")
            if random.randint(0, player.agl)+player.luck > random.randint(0, pixie.agl)+pixie.luck:
                print("'P-please wait! You don't have to do this! I'll do anything!'\n")
                return threat(30, 50, pixie, pixied)

            else:
                return "flee"

    elif ask == "d":
        print("\nPIXIE:\n'Huh? You want some Macca?'")
        if random.randint(0, 100) < 50:
            print("'Alright, but first you'll have to guess which hand it's in'\n")
            input("A) Left\nB) Right\nC) Kata\n")
            if random.randint(0, 100) < 50:
                print("\nPIXIE:\n'Nope! You lose;D'")
            else:
                print("\nPIXIE:\n'Aw man, you guessed right!'\n'Guess I have to give you the money now' -_-"+'"')
                winnings = random.randint(5, 20)*5
                print("you gained", winnings, "Macca")
                player.macca += winnings
            return "none"
        else:
            print("\nPIXIE:\n'Sure, I guess could trade some with you'")
            funds = random.randint(1, 3)
            z = bargaining("Macca", 3, 60, funds, pixied, pixie)
            if z == "pass":
                print("You got", funds*30, "Macca")
                player.macca += funds*30
                return "none"
            else:
                return z
    elif ask == "e":
        product = items[random.randint(0, len(items)-1)]
        print("\nPIXIE:\n'Hmm... Well I do have this", product.name, "I could give to you'\n'But I'm not going to just give it to you for free. I want something in return!'")
        if product.name == "revival bead":
            z = bargaining(product.name, 3, 50, random.randint(1, 2), pixied, pixie)
        else:
            z = bargaining(product.name, 3, 60, 1, pixied, pixie)
        if z == "pass":
            print("You got a", product.name)
            product.cost += 1
            return "none"
        else:
            return z
    else:
        lookup(ask)
        return pixier(demon)


def pretac1(demon):
    name = "\nPRETA:\n"
    print(demon.image + "\n"+name+"'Man, I'm starving! Got anything to eat?'\n")
    eat = input("A) No, sorry\nB) Me\nC) A knuckle sandwich\nD) I've got a coupon for 2 free pizzas in my pocket\n").lower()
    if eat == "a":
        print(name+"'Then how about I eat YOU instead!'")
        return "aggro"
    elif eat == "b":
        x = random.randint(0, 100)
        if x < 50:
            print(name+"'...You're weird.'")
            return "flee"
        elif x <= 75:
            print(name+"'But if I do that, what am I supposed to do with the leftovers? I'm not lugging your corpse around!'\n'Forget it, I'll just take the whole thing to go for now. I can eat you later when we get back to my place.'")
            return "recruit"
        else:
            print(name+"'Don't mind if I do!'")
            return "aggro"
    elif eat == "c":
        print(name+"'A knuckle sandwich? I've never heard of a sandwich like that.'\n'The hell's it taste like?'\n")
        input("A) Sweet, like revenge\nB) Bitter, like defeat\nC) Salty, like your tears\nD) Like a cool night on a hot summer day\nE) Pain\nF) Beef\n")
        print(name+"'Wow! I don't know what that means, but it sure sounds good.'\n'Hey, maybe I should join you. That way I can have all the sandwiches I want!'")
        z = bargaining("buddy", 10, 0, 0, toughd, preta)
        if z == "pass":
            return "recruit"
        else:
            return z

    elif eat == "d":
        print(name+"'Gimme that!'\nThe preta snatches the coupons from your hand and chows down on them.\n'Man, that hit the spot! I think I'll stick with you for now, you seem to know where the good food is.'")
        return "recruit"


    lookup(eat)
    pretac1(demon)

def slimec1(demon):
    name = "\nSLIME:\n"
    print(demon.image+"\n"+name+"'HeY, yOu lOoK toUGh! Let'S hAVe aN ARm wREstLinG MAtcH!'\n")
    match = input("A) You're on!\nB) I'll pass\n").lower()
    if match == "a":
        print("\nYou had an arm wrestling match with the demon.\nDue to the Slime having no arms, you are automatically declared the winner.")
        time.sleep(1.5)
        print(name+"'WOw! YoU'Re StROng!'\n'I sHOUld jOIn yOU sO I cAN be AS stROnG as yOU!'")
        return "recruit"
    elif match == "b":
        print(name+"'WhAT a WImP!'")
        return "none"
    else:
        lookup(match)
        return slimec1(demon)

# def monsterc1(demon):
#     name = "\n"+demon.name+"\n"
#     print(name+"'thERE's A hUMan sCeNt oN YA. you GOT ThE mAN-stink. whY's THAt, buDDy...?'\n")
#     hum = input("A) I'm human\nB) I ate a human\nC) I saw humans around\n").lower()
#     if hum == "a":
#         if random.randint(0, 100) >= 60:
#             print(name+"'EEHEeee...? wHAT THE hELL's A huMan DoINg hEre?'\n")
#             q = input("A) Hunting Demons\nB) Moving in\nC) Tourism\n").lower()
#             if q == "a":
#                 if random.randint(0, 100) >= 65:
#                     print(name+"'So HEY, WhaT DO YoU AcTUAlLY Do With THE DemoNS you KILL?'\n")
#                     c = input("A) Taxidermy\nB)I eat them\nC) Use them for research\n").lower()
#                     if c == "a":
#                         print(name+"'No WAY I'm GOnna be thE InTEriOR dEcOratiNg fOr sOme cHUmp-ass HuMan'S ROoM!'")
#                         return "aggro"
#                     elif c == "b":
#                         print(name+"'WAIt! I'm SuPPosed tO eAt YoU! nOt tHE oTHEr wAY rOUnd!'")
#                         return threat(60, 2, demon, monsterd)
#                     elif c == "c":
#                         print(name+"'EeHEE! YOU DUmbAsS huMaNs AnD YouR TiNy braiNs, AlwAys waSTiNG TiME puzZlINg OveR USelEss ShIt!'\n'AlL YoU goTtA Do Is ASk fOR a dEMON's kNOWLedGE! MUcH EasIER!'")
#                         return monsterr(demon)
#
#                     else:
#                         lookup(q)
#                         return monsterc1(demon)
#                 else:
#                     print(name+"WeLL, YoU sURe aS hELL aREn'T kILlIng mE!")
#                     return "aggro"
#             elif q == "b":
#                 print(name+"'firST yOU dEsTROy THE hUmAN wOrLd'S EnVIronmeNT, AND nOW YoU'rE GoNNA MesS WiTH oUrs!?'\n'FuCK OFF, bUDDy! GO die iN YOur OwN RuIned worLd, yOu GODDAmN ParaSITE!'")
#                 return "aggro"
#             elif q == "c":
#                 ilist = ["Life Stone", "Chakra Drop", "Amrita Soda", "Revival Bead"]
#                 print(name+"'eEhee! WEll, heRE, TAKe a souVEnir!'")
#                 x = random.randint(0, len(items)-1)
#                 print("The demon handed you one", ilist[x])
#                 items[ilist[x]] += 1
#                 return "flee"
#             else:
#                 lookup(q)
#                 return monsterc1(demon)
#
#         else:
#             print(name+"EeeHeEeE! thEn i'm GONna eAt yA!")
#             return "aggro"
#     elif hum == "b":
#         print(name+"'eEheE! ReALLy!? hoW Was iT?'\n'taSTed DElicioUS, RIGhT?'")
#         taste = input("A) Pretty tasty\nB) They tasted awful\nC) Good flavour notes, and finely aged\n").lower()
#         if taste == "a":
#             print(name+"'EeHEe! i wAnnA EaT A hUmAn ToO!'\n'bUt IF i JUSt eAt YOU, ThAt's PROBably closE ENouGH!'")
#             return "aggro"
#         elif taste == "b":
#
#         else:
#             lookup(taste)
#             return monsterc1(demon)
#     else:
#         lookup(hum)
#         return monsterc1(demon)

def monsterc2(demon):
    name = "\n"+demon.name.upper()+":\n"
    print(demon.image+"\n"+name+"'EehEeHEEHEE! I SmEll blOoD! BLood!'\n")
    blood = input("A) Laugh with them\nB) Sniff the air\nC) Stay silent\n").lower()
    if blood == "a":
        print(name+"'EEHEe... You GET It, rIght? you LovE THE FEELInG oF GetTINg SPLaTteReD wIth blOOD, too!'")
        love = input("\nA) I do\nB) I don't get it\nC) Those stains are tough to get out\n").lower()
        if love == "a":
            print(name+"'You DoN'T get it! yOU're TALkiN' ouT YOuR ass!'\n'You don't uNdERstaNd Me at aLL!'")
            return "aggro"
        elif love == "b":
            print(name+"'you saY That, bUt i KNow whaT You reAlLY arE.'\n'TheRe's somEthIN' dARK behind thAT preTtY faCe. reEeAaAL DARk.'\n'IT's Okay. YOu DoN't hAVE To HIDe it! I miGHT evEN hELp yA!'")
            return monsterr(demon)
        elif love == "c":
            print(name+"'EehEe, Uh... gOod pOint.'\n'heY if I jOIn Ya, You WoULdN'T mINd GIVin' Me a qUicK RINsE, would Ya?'\n")
            rinse = input("A) Of course\nB) I'm not touching you with a 10-foot pole\n").lower()
            if rinse == "a":
                if random.randint(0, 100) < 25:
                    print(name+"'mAnn, yOu'Re a ReaL fREAk, yoU kNOw tHat?'")
                    return "flee"
                else:
                    print(name+"'ThEn It'S seTTleD!'\n'YoU'Re gONna bE My nEw MAId!'\n")
                    return "recruit"
            else:
                print(name+"'DiDn'T haVE to BE sUcH a DiCK aBOut iT!'")
                return "aggro"
    elif blood == "b":
        print(name+"'YeaH, gET A Good whiff OF thAT... ThAT's wHat surVIVaL oF tHE FiTTEsT sMelLs LiKe...'")
        smell = input("\nA) It smells great\nB) I think that's just your stink\nC) I prefer the smell of barbecue\n").lower()
        if smell == "a":
            print(name+"'StiLL, iT's NOT THe BEST-sMellin' thING AROuND.'\n'aFtEr all, i loVe tHe SmELL Of PReSeNtS FoR me eveN mORE!'")
            return monsterr(demon)
        elif smell == "b":
            print(name+"'eEhee! yEah, YOu CAn Tell, RIgHT? I sMeLL JUSt hOW a deMon lOrD SHoULd!'\n'C'MOn, thE biG stiNky Demon lOrd's HunGRy For TREASURE! BrIng oUT yoUR ofFerINGs!'")
            offer = input("\nA) I offer seeking your strength\nB) I offer seeking prosperity\nC) I offer seeking gifts\nD) I'm not calling you that\n").lower()
            if offer == "a":
                x = bargaining("Ally", 2, 10, 5, monsterd, demon)
                if x == "pass":
                    return "recruit"
                else:
                    return x
            elif offer == "b":
                x = bargaining("Macca", 2, 10, 1, monsterd, demon)
                if x == "pass":
                    m = random.randint(0, 12)*10
                    print("You got", m, "macca")
                    return "none"
                else:
                    return x
            elif offer == "c":
                gift = items[random.randint(0, len(items)-1)]
                x = bargaining(gift.name, 4, 10, random.randint(0, 1), monsterd, demon) == "pass"
                if x == "pass":
                    print("The demon handed you a", items.name)
                    items.cost += 1
                    return "none"
                else:
                    return x
            else:
                print(name+"'TheN fACe tHe DeMOn lORD's wRAtH!'")
                return "aggro"
        elif smell == "c":
            print(name+"'YoU'rE GEtTin' DiSTrActeD, man! TAkE This SERiOuSlY!'\n'hERe, If you'RE HUNGRY, eaT this!'")
            gift = items[random.randint(0, len(items)-1)]
            print("The demon handed you a", gift.name)
            gift.cost += 1
            return "none"
    elif blood == "c":
        print(name+"'I dUNNO hoW YOU caN act sO coOL AND cOMPosED.'\n'dOESn'T ThIS SmElL GET You wORKEd UP? DON'T ya FeEl thE rUsH!?'\n")
        cold = input("A) Not really\nB) I don't smell any blood\nC) The stench paralyzed me\n").lower()
        if cold == "a":
            print(name+"'MaN... yoU'Re USeD to bEiNG SurRounDEd by BlOoD, huh? YoU CAn'T EVen SMELL IT aNyMoRe...'\n'cRaP... ThiS Guy mIght bE evEn MORe iNSANE THAN mE.'")
            return threat(40, 1, demon, monsterd)
        elif cold == "b":
            print(name+"'ReALly? GueSs I wAs JuSt ImAgiNINg iT tHEn'")
            return "none"
        elif cold == "c":
            print(name+"'HA! WeAKlinGs liKe yOU deSErVe to DIe!'")
            return "aggro"

    lookup(blood)
    return monsterc2(demon)

def monsterr(demon):
    name = "\n"+demon.name+"\n"
    print("'So wAdDyA wANt aNYwAY?'\n")
    want = input("A) Join me\nB) Give me advice\nC) Give me items\n").lower()
    if want == "a":
        print(name+"'YoU wAnT ME to JoIN yOU?'\n'wELl YoU'Re gONna hAVe to CouGh up SOme dOUgh FiRSt!'")
        x = bargaining("Ally", 4, 70, random.randint(3, 5), monsterd, demon)
        if x == "pass":
            return "recruit"
        else:
            return x
    elif want == "b":
        print(name+"'EeEehH? YOu wAnt aDVicE fROm MEe? WeLL Ok'\n'iF sOmEtHinG dOEsn'T tASte GoOd, sLATHer it IN BBQ sAUCe!'")
        return "none"
    elif want == "c":
        gift = random.randint(0, len(items)-1)
        print("WeLl, I dO haVe ThIs", monsterd.end[gift+3], "I cOUlD gIvE yoU.")
        x = bargaining(items[gift].name, 1, 70, 1, monsterd, demon)
        if x == "pass":
            print("The demon gave you one", items[gift].name)
            items [gift].cost += 1
            return "none"
    else:
        lookup(want)
        return monsterr(demon)


def threat(defend, max, victim, text):
    count = 0
    name = "\n"+victim.name.upper()+":\n"
    while True:
        x = input("A) Extort\nB) Recruit\nC) Spare\nD) Attack\n").lower()
        if x == "a":
            if count == 3:
                print(name+"'"+text.broke+"'")
                return "flee"
            elif random.randint(0, 100)+victim.coward < defend:
                print(name+"'"+text.snap+"'")
                return "aggro"
            else:
                stolen = random.randint(1, max)*10
                print("The", victim.name, " handed over", stolen, "Macca")
                print(name+"'"+text.mugged+"'")
                player.macca += stolen
                count += 1
                continue
        elif x == "b":
             if random.randint(0, 100)+victim.coward > defend + victim.loyal:
                 print(name+"'"+text.captured+"'")
                 return "recruit"
             else:
                print(name+"'"+text.snap+"'")
                return "aggro"
        elif x == "c":
            return "flee"
        elif x == "d":
            print("You seize the opportunity to strike the defenceless demon, showing no mercy!")
            time.sleep(1)
            betrayal = dmgformula(player, victim, "Almighty", 100, -999)[0]
            print(victim.name, "took", betrayal, "points of damage!")
            victim.hp -= betrayal
            print(name+"'" + text.betrayed +"'")
            return "none"
        else:
            lookup(x)
            return threat(defend, max, victim, text)

def bargaining(item, patience, morality, target, dialogue, demon):
    frustration = 0
    mood = 0
    name = "\n"+demon.name.upper()+":\n"
    offers = {"HP": player.hp, "MP": player.mp, "Macca": player.macca, "Life Stone": items[0].cost, "Chakra Drop": items[1].cost, "Amrita Soda": items[2].cost, "Revival Bead": items[3].cost,}
    while True:
        demand = random.randint(0, len(list(offers)) - 1)
        if list(offers)[demand] == item:
            continue
        else:
            print(name+"'"+dialogue.think+"'")
            time.sleep(1)
            if list(offers)[demand] == "HP" or list(offers)[demand] == "MP" or list(offers)[demand] == "Macca":
                perc = [0.25, 0.5, 0.75]
                x = random.randint(0, 2)
                value = x+1
                amount = math.floor(offers[list(offers)[demand]]*perc[x])
            else:
                x = 3
                amount = 1
                if list(offers)[demand] == "Revival Bead":
                    value = 3
                else:
                    value = 1

            if list(offers)[demand] == "Macca":
                print("'"+dialogue.start, amount, dialogue.end[demand]+"!'")
            else:
                print("'"+dialogue.start, dialogue.middle[x], dialogue.end[demand]+"!'")

            print("\nYou have:", offers[list(offers)[demand]])
            if offers[list(offers)[demand]] > 0:
                print("A) Comply")
            else:
                print("A) I don't have that")
            haggle = input("B) Ask for something else\nC) You've had enough\n").lower()
            if haggle == "a" and offers[list(offers)[demand]] > 0:
                offers[list(offers)[demand]] -= amount
                player.hp = offers["HP"]
                player.mp = offers["MP"]
                player.macca = offers["Macca"]
                items[0].cost = offers["Life Stone"]
                items[1].cost = offers["Chakra Drop"]
                items[2].cost = offers["Amrita Soda"]
                items[3].cost = offers["Revival Bead"]
                print("'"+dialogue.gifted+"'")
                mood += value
                if mood > target:
                    if random.randint(0,100) > morality:
                        print(name+"'"+dialogue.sated+"'")
                        return "pass"
                    else:
                        ditch = morality/2
                        if ditch > random.randint(0, 100):
                            print(name+"'"+dialogue.thief+"'")
                            return "flee"
            elif haggle == "a" and offers[list(offers)[demand]]== 0:
                print(name+"'"+dialogue.out+"'")
                if random.randint(0, 100) >= morality and list(offers[demand]) != "HP" and list(offers)[demand] != "MP" and list(offers)[demand] != "Macca":
                    print(name+"'"+dialogue.pity+"'")
                    offers[list(offers)[demand]] += 1
                    player.hp = offers["HP"]
                    player.mp = offers["MP"]
                    player.macca = offers["Macca"]
                    items[0].cost = offers["Life Stone"]
                    items[1].cost = offers["Chakra Drop"]
                    items[2].cost = offers["Amrita Soda"]
                    items[3].cost = offers["Revival Bead"]
                    return "flee"
                else:
                    frustration += 1

            elif haggle == "b":
                frustration += 1
            elif haggle == "c":
                if mood >= target:
                    print(name+"'"+dialogue.content+"'")
                    return "pass"
                else:
                    print(name+"'"+dialogue.angry+"'")
                    return "aggro"
            else:
                lookup(haggle)
                return bargaining(item, patience, morality, target, dialogue, pixie)
        if frustration >= patience:
            print(name+"'"+dialogue.frust+"'")
            return "aggro"



def finalcute(demon):
    if random.randint(0, 100) < 50:
        print("'Crap!'\n'I'm getting out of here!'")
        return "flee"
    print(demon.name, "struck up a conversation with", player.name)
    print("'H-hang on a minute! Surely you don't have to kill me!'\n'I-i was just playing a little prank!'\n'We're all fine now, right?'")
    return threat(10, 5, demon, demon.lines.opening)


def finalmonster(demon):
    if demon.coward > 0 and random.randint(0, 100) <= demon.coward:
        print("'HelL nO!'\n' I'm nOt sTiCKinG aROunD aND geTtIng kiLleD!'")
        return "flee"
    else:
        print("'If i gO dOWn, i'm tAKing YoU wItH mE!'")
        return "aggro"

def finaltough(demon):
    print("'So that's it huh...'\n'Well I'm not going down without a fight!'")
    return "aggro"

class script:
    def __init__(self, opening, recruited, friend, attack, support, heal, final):
        self.opening = opening
        self.recruited = recruited
        self.friend = friend
        self.attack = attack
        self.support = support
        self.heal = heal
        self.final = final

pixiescript = script([pixiec1, pixiec2], "'I'm Pixie of the Fairy race'\n'I'll do my best to support you!'", "'Oh?'\n'I see you have my friend with you.'\n'In that case, here's a little gift so you take good care of her.'", "'Take this!'", "'Just try and catch me!'", 'Crap, this is bad!', finalcute)
slimescript = script([slimec1, monsterc2], "'I'm SlIMe oF tHE fOUl rAce'\n'I'Ll inFEct AlL yOUr fOeS!'", "(ignore the fact he's talking normally)\n'HeY! ThAt's my pAl yOu gOt tHeRe.'\n'WeLl aNY fRiEnD oF HiS IS a FrIENd oF mINE!'", "'eAt tHiS!'", "'LEt's pOWer uP!'", "", finalmonster)
pretascript = script([pretac1], "'I'm Preta of the Haunt race'\n'I'm craving for some action!'", "'Oh hey, I see you've got one of my mates with you.'\n'Well then, here's something for the road!'", "'Lemme bite ya!'", "", "", finaltough)
daemonscript = script([monsterc2], "'I'm Daemon of the Brute race'\n'Let's cause some chaos!'", "", "'I'Ll tEAr yOU to sHReDS!'", "'LEtS kICk tHiNgs Up a nOTcH!'", "", finalmonster)
# if run == "none":
#     print("No turn passes")
# elif run == "aggro":
#     print("The Pixie attacks!")
# elif run == "flee":
#     print("The Pixie ran away")
# elif run == "recruit":
#     print("I'm the fairy, Pixie! Nice to meet you")
# else:
#     print("You should not be getting this message")

