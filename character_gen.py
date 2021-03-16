from random import choice
import json

characteristics = json.load(open("characteristics.json", mode="r"))
num_chars = int(input("Number of characters? "))
for i in range(num_chars):
    new_char = {}
    for characteristic in characteristics:
        for option in characteristics[characteristic]:
            chosen = choice(characteristics[characteristic][option])
            new_char[option] = chosen

    print("{")
    master_list = open("master_list.txt", mode="a")
    master_list.writelines("{\n")
    master_list.writelines("\tname: \n\tcontext: \n")
    for key in new_char:
        print("\t", key, ": ", new_char[key])
        master_list.writelines("\t" + key + ": " + new_char[key] +"\n")
    master_list.writelines("},\n")
    print("}")
    master_list.close()