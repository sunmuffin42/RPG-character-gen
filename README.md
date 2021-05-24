# RPG* Character Generator
##### (* but really just DnD for now re: races)

A simple Python 3 script to generate characteristics for NPCs.
The `master_list.txt` file is where the characters go after they've been generated, and as it stands it contains a couple examples of what the output would look like. 

When you run `$ python character_gen.py`, it will print out the generated items in a simple format that resembles a JSON but is easier to read for anyone unfamiliar with JSON (also, it's very easy to make this a JSON by some RegExes like `(\w.+ ):  (.+$))` and `\"$1\": \"$2\",` or however your engine likes it). The program will first prompt you to choose features to generate selectively or all at once. When prompted with `> What information do you want to generate? 'f' for full character, 'n' for name, 'p' for personality, 'v' for vocal tics, 'r' for race ('npvr' for all of these, but not full)`-- it is fairly straighforward. Any combination of `n`, `v`, `p`, or `r` will generate those things only. If you do not want some specific features, just type `f`.
After typing the letter(s), just hit enter/return, and it will prompt you to enter the number of NPCs you want to generate (`> Number of characters?`). Type an integer, press enter/return, and it will take care of the rest.

The result will look like this in the terminal:
```
> python character_gen.py
> What information do you want to generate? 'f' for full character, 'n' for name, 'p' for personality, 'v' for vocal tics, 'r' for race ('npvr' for all of these, but not full)
> f
> Number of characters?
> 1
{
	name: Graib
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
	context: 
	name: Graib
	race: Minotaur
	clothes: fancy clothes
	accents: southeastern US
	accent_thickness: major confusion
	vocal_tics: tiny child
	approach_to_strangers: noncommital
	characteristics: excitable and passionate (rambly)
},
```
and another example:
```
> python character_gen.py
> What information do you want to generate? 'f' for full character, 'n' for name, 'p' for personality, 'v' for vocal tics, 'r' for race ('npvr' for all of these, but not full)
> n
> Number of characters?
> 1
{
	name: Lech
}
```
In master_list.txt:
```
{
	context:
	name: Lech
}
```
```
> python character_gen.py
> What information do you want to generate? 'f' for full character, 'n' for name, 'p' for personality, 'v' for vocal tics, 'r' for race ('npvr' for all of these, but not full)
> vp
> Number of characters?
> 1
{
	approach_to_strangers :  sincere
	vibe :  easily/constantly amazed
	vocal_tics :  constant vowel length shift
}
```
and in master_list.txt:
{
	context:
	approach_to_strangers :  sincere
	vibe :  easily/constantly amazed
	vocal_tics :  constant vowel length shift	
}
Note that the output to the terminal will appear without the context; the idea being that you can go into the text file afterward and add where the players met them (`context`).

I'd recommend playing with the `characteristics.json` file just so it won't generate anything you don't want to try to do. I included things I'm fine with doing, but not everyone can do a Kiwi accent, e.g.

NB: I know a lot of these things are not exclusive even in the same group (eg one can be drunk and sexy, one can use multiple sets of pronouns, etc). This is for quick decisions on the fly and is always up to the interpretation of the GM, never definitive (OBVIOUSLY).