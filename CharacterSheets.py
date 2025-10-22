
# input("What is your name?\n")
from Skills import strike, agi, zio, bufu, zan, mudo, dia, marin_karin, tarukaja, sukukaja, rakunda, hellish_slash


# class buffs:
#     def __init__(self, stage, duration):
#         self.stage = stage
#         self.dur = duration



class chara:
    def __init__(self, name, race, lv, mxhp, hp, mxmp, mp, xp, str, vit, agl, mag, luck, loyal, coward, play, element, skills, macca, buffs, guard, image):
        self.name = name
        self.race = race
        self.lv = lv
        self.mxhp = mxhp
        self.hp = hp
        self.mxmp = mxmp
        self.mp = mp
        self.xp = xp
        self.str = str
        self.vit = vit
        self.agl = agl
        self.mag = mag
        self.luck = luck
        self.loyal = loyal
        self.coward = coward
        self.play = play
        self.element = element
        self.skills = skills
        self.macca = macca
        self.buffs = buffs
        self.guard = guard
        self.image = image

#taru = impacts attack, raku = impacts defence, suku = impacts evasion/accuracy


player = chara("You", "Human", 5, 100, 100, 100, 100, 0, 5, 5, 5, 5, 5, 0, 0, 0, {
      #"aff" = affinity, "res" = resistance, "dur" = duration "inflict" = times inflicted
       "Physical":{"aff": 0, "res":0},
       "Fire":{"aff": 0, "res":0},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 0, "res": 0},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": 0},
       "Almighty": {"aff": 0},
       "Support": {"aff": 0},
       "Heal": {"aff": 0},
       "Ailment": {"aff": 0},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": 0, "dur": 0, "inflict": 0},
       "Confusion": {"res": 0, "dur": 0, "inflict": 0},
       "Charm": {"res": 0, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
        }, [agi, zio], 0, {"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "                       #+-+#            \n                     #####+++           \n                    ######++#           \n                      ##+..##           \n                    ####+-++            \n                     ##++-++++++        \n                    ###.--#+#+-++       \n                    #+-.-+####+#++      \n                   ##++--#### ####++    \n              ##+++##+--.+###   +++#    \n           #######+##-----####+####     \n          #+# ######--...-+#+###        \n                 ##--++++++#+##+#       \n                ++#+#++#+-+-++###       \n              ++#########..##++##       \n               +##########.-# ##        \n              ++#+#+##########          \n            +++ +# -#### ##+++          \n           --      +####  #+++#         \n         +--       +###    #+++#        \n       --+         ####     #++#        \n      .-           +###     ##+##       \n    ..+            +###      #####      \n   .+              +###       +####     \n ++                 ###        #####    \n+#                  ###         ####    \n                   ####          ####   \n                   ####           #+#   \n                   ####           ##++  \n                   ####            ##++ \n                  ####+             ### \n                #####               ##+#\n                                     ##+\n")

daemon = chara("Daemon", "Brute", 7, 78, 78, 73, 73, 0, 11, 9, 9, 8, 7, -10, -20, 0, {
       "Physical":{"aff": 2, "res":0},
       "Fire":{"aff": 2, "res":0.5},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":-0.25},
       "Force": {"aff": 0, "res": 0},
       "Light": {"aff":-4, "res": -0.25},
       "Dark": {"aff": 2, "res": 1},
       "Almighty": {"aff":0},
       "Support": {"aff": 0},
       "Heal": {"aff": 0, "inflict": 0},
       "Ailment": {"aff": 0},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": -0.25, "dur": 0, "inflict": 0},
       "Confusion": {"res": 0, "dur": 0, "inflict": 0},
       "Charm": {"res": 0, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
}, [strike, hellish_slash, agi, mudo, tarukaja, rakunda], 0,{"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "          ▓▓▓▓▓▓███████                 \n       █▓▓█████████     █ ███████       \n    ███████████▓██▓     █ █   ████▓█    \n  ███ ███  ██   █▓█▓▓▓▒ ▓▓▓▓▓ ▓██████   \n ██  ██    █      ▓▓██▒▓▓▓▒▓▓▓▓█▓█████  \n██   █            ▓▓▓▓█▓▓▓▓▓▓▓██▓▓▓████ \n                 ▓███▓▓██▓█████ ██ █████\n                ▓████▓▓██▓▓███▓     ████\n                ▓████▓▓██▓█▓█▓▓     █  █\n               ▒▓████▓▓█   ▓▓█▓        █\n            ▒▓ █▓▓████▓▓█  ▓███▓█      █\n          ▓███ ▓▓█████▓▓█████▓▓         \n         ██    ▓▓██  ▒▓█▓▓███           \n         ██▓▓███▓▓▓   ███▓█             \n           █   ▓▓██   ▓████             \n               ████  ▓████              \n                ███▓▓▓███               \n                 ▓▓███▓█                \n            ▒▒▒▒▓▓▓█████                \n           ▒▒▒▒▒▒ ██████                \n           ░▒▓▓▒  ███ █                 \n                  ███                   \n")

pixie = chara("Pixie(1)", "Fairy", 2, 55, 55, 82, 82, 0, 2, 4, 7, 8, 6, 5, 0, 30,  {
       "Physical":{"aff": -2, "res":0},
       "Fire":{"aff": 0, "res":-0.25},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 1, "res": 0.5},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": -0.25},
       "Almighty": {"aff":0},
       "Support": {"aff": 1},
       "Heal": {"aff": 1, "inflict": 0},
       "Ailment": {"aff": 1},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": -0.25, "dur": 0, "inflict": 0},
       "Confusion": {"res": -0.25, "dur": 0, "inflict": 0},
       "Charm": {"res": 0.5, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
        }, [strike, dia, zio, zan, marin_karin, sukukaja], 0,{"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "                                        ▒\n                                     ░░░ \n        ░                          ░░░░  \n        ░░                       ░░░░░   \n         ░░                     ░░░░░░   \n          ░░  ▒               ░░░░░░░    \n           ░░ ░              ░░░░░░░     \n           ░░░░▓           ░░░░░░░░      \n           ▓░░░░         ▒░░░░░░░        \n         ▓▓▓█▓█▓█       ░░░░░░░    ░░░   \n        ▓▓███▒▒█▒     ░░░░░░░  ░░░░░░    \n        ███▒░░▒▓███ ░░░░░░░░░░░░░░░      \n         █▓▒░░░▓███░░░▒░░░░░░░░░         \n           █▒░▒░░░▒▓▒░░▒▒                \n        ▓▓▓▒▒▓▓░▒▒░▓█                    \n      ▓▓▓▓▓▓▓▓▓▓▒▒░▒█                    \n   ▓▓▓▓▓▓▓▓▓█ ▓▓▓▓▓▓▓                    \n  ▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓                    \n ▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓▓░░▒                    \n ▓▓█ ▓▓▓▓▓▓▓▓▓▓░▒░░░▓                    \n     ▓▓▓▓ █▒▓▒▒░░░░░                     \n    ▓▓▓▓▓   ▒▓▒▒▒▒░▒                     \n   ▓▓▓  ▓▓                               \n  ▓▓▓    ▓▓▓                             \n ▓▓▓▓    ▓▓█                             \n▓▓▓       ▓▓                             \n▓          ▓                             \n")

pixie1 = chara("Pixie", "Fairy", 2, 55, 55, 82, 82, 0, 2, 4, 7, 8, 6, 5, 0, 30,  {
       "Physical":{"aff": -2, "res":0},
       "Fire":{"aff": 0, "res":-0.25},
       "Ice":{"aff":0, "res": 0},
       "Lightning":{"aff":0, "res":0},
       "Force": {"aff": 1, "res": 0.5},
       "Light": {"aff":0, "res": 0},
       "Dark": {"aff": 0, "res": -0.25},
       "Almighty": {"aff":0},
       "Support": {"aff": 1},
       "Heal": {"aff": 1, "inflict": 0},
       "Ailment": {"aff": 1},
       "Sleep": {"res": 0, "dur": 0, "inflict": 0},
       "Mirage": {"res": 0, "dur": 0, "inflict": 0},
       "Poison": {"res": -0.25, "dur": 0, "inflict": 0},
       "Confusion": {"res": -0.25, "dur": 0, "inflict": 0},
       "Charm": {"res": 0.5, "dur": 0, "inflict": 0},
       "Seal": {"res": 0, "dur": 0, "inflict": 0},
        }, [strike, dia, zio, zan, marin_karin, sukukaja], 0,{"taru": {"stage": 0, "dur":0}, "raku": {"stage": 0, "dur":0}, "suku": {"stage": 0, "dur":0}}, False, "                        ░░░░░      ░░░  \n                      ░░░      ░░░░░░░░░\n                     ░░░░   ░░░░░░   ░░░\n                    ░░░░░ ░░░░░░░░      \n                   ░░░░░░░░░░░░░░       \n                   ░░░░░░░░░░░░░        \n                  ░░░░░░░░░░░░░         \n            ▓▓▓███░░░░░░░░░░░░░░░░      \n           ▒▒▒▓▓▓▒▓░░░░░░░░░░ ░░  ░     \n           ▒▒▓▒░▒▒▓░░░░░░░░░     ░░     \n           ██▒░░░▓▓░░░░░░░░             \n               ░░▓▓▒░░░▒ ░░             \n                 ▒▒▒▓▒░▓   ░            \n                  ▒▒▓▓▓▓▓ ░░            \n                   ▓▓▓▓▓▓▓              \n                  ▓▒▒▓▓▓▒▓▓             \n           ▒▒▒▒▒▒▒░░░░▒█▓▒▓▓            \n          ▒▓▓▓▓▓██░░░░▓▓█▓▒▓▓▓▓         \n        ▓▒▒▓█████▒░░▒▓▓▓   ▓▓▓▓         \n       ▒▒▓▓███                          \n     ▒▒▓▓▓▓▓▓▓▓                         \n   ▒▒▓▓▓    ▓▓▓▓                        \n ▒▒▓▓█       ▓▓▓▓                       \n▒▓▓█          ▒▒▓█                      \n█              ▒▓█                      \n                ▓█                      \n")







