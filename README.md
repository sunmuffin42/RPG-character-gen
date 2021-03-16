# RPG* Character Generator
##### (* but really just DnD for now re: races)

A simple Python 3 script to generate characteristics for NPCs.
The `master_list.txt` file is where the characters go after they've been generated, and as it stands it contains a couple examples of what the output would look like. 

When you run `$ python character_gen.py`, it will print out the generated items in a simple format that resembles a JSON but is easier to read for anyone unfamiliar with JSON (also, it's very easy to make this a JSON by some RegExes like `(\w.+ ):  (.+$))` and `\"$1\": \"$2\",` or however your engine likes it). The program will prompt you to enter the number of NPCs you want to generate (`> Number of characters?`). Type an integer and it will take care of the rest.

The result will look like this in the terminal:
```
{
	race: Minotaur
	clothes: fancy clothes
	accents: southeastern US
	accent_thickness: major confusion
	vocal_tics: tiny child
	approach_to_strangers: noncommital
	characteristics: excitable and passionate (rambly)
}
```

The result will look like this in the output file (`master_list.txt`):
```
{
	name: 
	context: 
	race: Minotaur
	clothes: fancy clothes
	accents: southeastern US
	accent_thickness: major confusion
	vocal_tics: tiny child
	approach_to_strangers: noncommital
	characteristics: excitable and passionate (rambly)
},
```

Note that the output to the terminal will appear without the name and context; the idea being that you can go into the text file afterward and add the names of people (`name`, obviously) and where the players met them (`context`).

I'd recommend playing with the `characteristics.json` file just so it won't generate anything you don't want to try to do. I included things I'm fine with doing, but not everyone can do a Kiwi accent, e.g.

NB: I know a lot of these things are not exclusive even in the same group (eg one can be drunk and sexy, one can use multiple sets of pronouns, etc). This is for quick decisions on the fly and is always up to the interpretation of the GM, never definitive (OBVIOUSLY).