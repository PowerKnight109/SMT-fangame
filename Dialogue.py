import time
import random
import math
from Formulas import dmgformula
from Skills import items
from CharacterSheets import player, pixie
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
#slimed = bargaintxt("LeMmE tHiNk", "GiMmE", ["A sMaLl bIt oF YoUr", "A nIcE cHuNk oF yOuR", "A mAsSiVe ChUnK oF yOuR", "A"], ['HP', 'MP', 'LiFe StOnE', 'ChAkRa DrOp', 'SoDa', 'ReViVal BeAd', 'MaCcA' ])


def pixiec1():
    print(pixie.image+"\n'WOW, A human!'\n'I've never seen a real life human before! Do you mind if I get a closer look?'")
    x = input("\nA) Of course\nB) Not sure I'm comfortable with that,\n").lower()
    if x == "a":
        y = random.randint(0, 100)
        if y <= 10:
            print("'Wow, humans are amazing! I think I'm going to join you from now on'")
            return "recruit"
        elif y <= 20:
            print("'Ha! You're too gullible!'")
            return "aggro"
        elif y <= 40:
            if y <= 30 and player.macca >= 0:
                print("'Tricked you!'")
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
                    print("'What? You don't have anything on you?'\n'How rude!'\n'Next time you try talking to a girl like me, make sure you're worth my time!'")
                else:
                    print("'Too easy!'")
                    stolen = stealables[random.randint(0, len(stealables)-1)]
                    print("The pixie stole 1", stolen.name, "from you!")
                    stolen.cost -= 1
            if random.randint(0, 100) <= 25:
                return "flee"
            else:
                return "none"
        else:
            print("'Thanks so much! All my friends are going to be SO jealous when I tell them I met a human in person!'")
            return pixier()

    elif x == "b":
        if random.randint(0, 100) >= 75:
            print("'Oh alright then' :(")
            return "none"
        else:
            print("'You're no fun!'")
        return "aggro"
    else:
        lookup(x)
        return pixiec1()

def pixier():
    print("'So, what brings you out here anyway?'")
    ask = input("\nA) Looking for friends\nB) Looking for allies\nC) Looking for demons to kill\nD) Looking for Macca\nE) Looking for items\n").lower()
    y = random.randint(0, 100)
    if ask == "a":
        if y <= 10:
            print("'Well, good luck with that.'")
            return "flee"
        elif y <= 40:
            print("'I know! Why don't we be friends then?'\n'Doesn't that sound like such a good idea?'")
            return "recruit"
        else:
            print("'Hey now, if you want to be friends with me you've got to give me something to prove it first.'")
            z = bargaining("friend", 5, 50,  random.randint(1, 2), pixied)
            if z == "pass":
                return "recruit"
            else:
                return z
    elif ask == "b":
        if y <= 10:
            print("'Yeah right! I bet you're the type who views demons as nothing more than tools!'")
            print("'Well guess what? You aren't fooling me with that bullshit!'")
            return "aggro"
        elif y <= 60:
            print("'Idk, see I'm not really the fighting type.'\n'You'd probably be better off bothering some other demons if that's what you want.'")
            return "none"
        else:
            print("'You're trying to recruit allies?'\n'Well, in that case you should probably know that most demons aren't going to join for free'\n'Most are going to want you to offer something in return. I'll lead by example'")
            z = bargaining("recruit", random.randint(1,2), 50, random.randint(1, 2), pixied)
            if z == "pass":
                return "recruit"
            else:
                return z
    elif ask == "c":
        if y < 50:
            print("'Die scum!'")
            return "aggro"
        else:
            print("'Y-you aren't talking about me are you? You don't mean you want to k-k-KILL me?'")
            if random.randint(0, player.agl)+player.luck > random.randint(0, pixie.agl)+pixie.luck:
                print("'P-please wait! You don't have to do this! I'll do anything!'\n")
                return threat(30, 50, pixie, pixied)

            else:
                return "flee"

    elif ask == "d":
        print("'Huh? You want some Macca?'")
        if random.randint(0, 100) < 50:
            print("'Alright, but first you'll have to guess which hand it's in'\n")
            input("A) Left\nB) Right\nC) Kata\n")
            if random.randint(0, 100) < 50:
                print("'Nope! You lose;D'")
            else:
                print("'Aw man, you guessed right!'\n'Guess I have to give you the money now' -_-"+'"')
                winnings = random.randint(5, 20)*5
                print("you gained", winnings, "Macca")
                player.macca += winnings
            return "none"
        else:
            print("'Sure, I guess could trade some with you'")
            funds = random.randint(1, 3)
            z = bargaining("Macca", 3, 60, funds, pixied)
            if z == "pass":
                print("You got", funds*30, "Macca")
                player.macca += funds*30
                return "none"
            else:
                return z
    elif ask == "e":
        product = items[random.randint(0, len(items)-1)]
        print("'Hmm... Well I do have this", product.name, "I could give to you'\n'But I'm not going to just give it to you for free. I want something in return!'")
        if product.name == "revival bead":
            z = bargaining(product.name, 3, 50, random.randint(1, 2), pixied)
        else:
            z = bargaining(product.name, 3, 60, 1, pixied)
        if z == "pass":
            print("You got a", product.name)
            product.cost += 1
            return "none"
        else:
            return z
    else:
        lookup(ask)
        return pixier()

def threat(defend, max, victim, text):
    count = 0
    while True:
        x = input("A) Extort\nB) Recruit\nC) Spare\nD) Attack\n").lower()
        if x == "a":
            if count == 3:
                print("'"+text.broke+"'")
                return "flee"
            elif random.randint(0, 100)+victim.coward < defend:
                print("'"+text.snap+"'")
                return "aggro"
            else:
                stolen = random.randint(1, max)*10
                print("The", victim.name, " handed over", stolen, "Macca")
                print("'"+text.mugged+"'")
                player.macca += stolen
                count += 1
                continue
        elif x == "b":
             if random.randint(0, 100)+victim.coward > defend + victim.loyal:
                 print("'"+text.captured+"'")
                 return "recruit"
             else:
                print("'"+text.snap+"'")
                return "aggro"
        elif x == "c":
            return "flee"
        elif x == "d":
            print("You seize the opportunity to strike the defenceless demon, showing no mercy!")
            time.sleep(1)
            betrayal = dmgformula(player, victim, "Almighty", 100, -999)[0]
            print(victim.name, "took", betrayal, "points of damage!")
            victim.hp -= betrayal
            print("'" + text.betrayed +"'")
            return "none"
        else:
            lookup(x)
            return threat(defend, max, victim, text)




def bargaining(item, patience, morality, target, dialogue):
    frustration = 0
    mood = 0
    offers = {"HP": player.hp, "MP": player.mp, "Macca": player.macca, "Life Stone": items[0].cost, "Chakra Drop": items[1].cost, "Amrita Soda": items[2].cost, "Revival Bead": items[3].cost,}
    while True:
        demand = random.randint(0, len(list(offers)) - 1)
        if list(offers)[demand] == item:
            continue
        else:
            print("'"+dialogue.think+"'")
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
                        print("'"+dialogue.sated+"'")
                        return "pass"
                    else:
                        ditch = morality/2
                        if ditch > random.randint(0, 100):
                            print("'"+dialogue.thief+"'")
                            return "flee"
            elif haggle == "a" and offers[list(offers)[demand]]== 0:
                print("'"+dialogue.out+"'")
                if random.randint(0, 100) >= morality and list(offers[demand]) != "HP" and list(offers)[demand] != "MP" and list(offers)[demand] != "Macca":
                    print("'"+dialogue.pity+"'")
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
                    print("'"+dialogue.content+"'")
                    return "pass"
                else:
                    print("'"+dialogue.angry+"'")
                    return "aggro"
            else:
                lookup(haggle)
                return bargaining(item, patience, morality, target, dialogue)
        if frustration >= patience:
            print("'"+dialogue.frust+"'")
            return "aggro"


class script:
    def __init__(self, opening, recruited):
        self.opening = opening
        self.recruited = recruited

pixiescript = script([pixiec1], "'I'm Pixie of the Fairy race'\n'I'll do my best to support you!'")
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

