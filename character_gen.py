from random import choice, randrange
import json

characteristics = json.load(open("characteristics.json", mode="r"))
info = input("What information do you want to generate? 'f' for full character, 'n' for name, 'p' for personality, 'v' for vocal tics, 'r' for race ('npvr' for all of these, but not full)\n").lower()
num_chars = int(input("Number of characters? "))
onsets = ["fl", "sl", "sp", "tr", "ts", "pl", "pr", "fr", "dr", "ch", "sh", "s", "w", "", "r", "t", "y", "p", "d", "f", "g", "gr", "gl", "kl", "kr", "h", "j", "k", "l", "z", "v", "b", "n", "m" "ks"]
codas = ["lf", "ls", "ps", "rt", "ts", "lp", "rp", "rf", "rd", "ch", "sh", "s", "w", "", "r", "t", "y", "p", "d", "f", "g", "rg", "lg", "lk", "rk", "h", "j", "k", "l", "z", "v", "b", "n", "m", "rn", "rm", "fs", "ds", "ts"]
nuclei = ["a", "e", "i", "o", "u", "ou", "ei", "au", "ai", "ae", "ao", "eo", "oi", "oa", "ia", "ua", "ie", "eu"]        

def pick_name():
    this_name = ""
    for i in range(randrange(1,3)):
        this_name += choice(onsets) + choice(nuclei) + choice(codas)
    return this_name.capitalize()

for i in range(num_chars):
    new_char = {}
    if "f" in info:
        new_char["name"] = pick_name()
        for characteristic in characteristics:
            for option in characteristics[characteristic]:
                chosen = choice(characteristics[characteristic][option])
                new_char[option] = chosen
    else:
        if "n" in info:
            new_char["name"] = pick_name()
        if "p" in info:
            new_char["approach_to_strangers"] = choice(characteristics["personalities"]["approach_to_strangers"])
            new_char["vibe"] = choice(characteristics["personalities"]["vibe"])
        if "v" in info:
            new_char["vocal_tics"] = choice(characteristics["voice"]["vocal_tics"])
        if "r" in info:
            new_char["race"] = choice(characteristics["physical_appearance"]["race"])
    print("{")
    master_list = open("master_list.txt", mode="a")
    master_list.writelines("{\n")
    master_list.writelines("\tcontext: \n")
    for key in new_char:
        print("\t", key, ": ", new_char[key])
        master_list.writelines("\t" + key + ": " + new_char[key] +"\n")
    master_list.writelines("},\n")
    print("}")
    master_list.close()