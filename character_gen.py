from random import choice
import json

characteristics = json.load(open("characteristics.json", mode="r"))
new_char = {}
for characteristic in characteristics:
    for option in characteristics[characteristic]:
        chosen = choice(characteristics[characteristic][option])
        new_char[option] = chosen
print(new_char)