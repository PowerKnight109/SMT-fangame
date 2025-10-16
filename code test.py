from contextlib import nullcontext
from CharacterSheets import player, pixie, pixie1, daemon
from CombatSystem import fight
import time
import random
from Dictionary import glossary


from Formulas import ailformula
from Skills import agi, zio, bufu, zan, dia, sukukaja, marin_karin, skilluse





memory = {"Weak": {}, "Res" : {}, "Null": {},  "Bad": {}}

# for i in range(len(party)):
#     weak = []
#     res = []
#     null = []
#     bad = []
#     for j in range(7):
#         current = party[i].element[list(party[i].element)[j]]["res"]
#         if current != 0:
#             if current < 0:
#                 weak.append(list(party[i].element)[j])
#             elif current < 1:
#                 res.append(list(party[i].element)[j])
#             elif current == 1:
#                 null.append(list(party[i].element)[j])
#             elif current > 1:
#                 bad.append( list(party[i].element)[j])
#         memory["Weak"][party[i].name] = weak
#         memory["Res"][party[i].name] = res
#         memory["Null"][party[i].name] = null
#         memory["Bad"][party[i].name] = bad

for i in range(2, 6):
    print(i)


# print("[ROUND 2]\nvs Daemon, Pixie")
# time.sleep(1)
# if fight([player, pixie], [daemon, pixie1]):
#     print("You Win!")
# print("GAME OVER")

if "Sealed demons are unable to use skills other than their basic attack" in glossary:
    print("True")
else:
    print("False")