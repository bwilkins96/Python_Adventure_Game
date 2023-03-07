# Overview #
This is a text-based adventure game that I designed as my final project
in SWDV 600: Intro to Programming at Maryville University.

Running 'python adventure_game.py' will generate and run an instance of the adventure game.

Alternatively, AdventureGame can be imported from 'adventure_game.py'.
A game can be produced using AdventureGame() and run using the run instance method.

e.g. From adventure_game import AdventureGame -> AdventureGame().run()

# Requirements #
This is a very open-ended problem and intentionally so. The goal is for you 
to make design choices about how the game plays, how it is themed, 
and how you structure the data required to make it work. 
You are encouraged to be as creative as possible in making your adventure game
fun and interesting. The theme is entirely up to you. However, you must adhere to a 
few requirements:

Your adventurer must have a name, keep track of how many trinkets they've collected, 
and their personal resource. They can have other things as well, but these are required.

Trinket examples from previous games: 
Eggo waffles, holiday gifts, and Subway endorsement checks.

Personal resource examples from previous games: 
time to work on programming assignments, health points, and time for preparing dinner.

Your enemies must have a name, an introduction 
(e.g. "It's Aaron Burr! He'll kill your political aspirations and then shoot you in the back!"),
and a personal resource that you can reduce when "attacking". 
Again, other things are also possible and encouraged, but these are required.
Enemy examples from previous games: sharks, nosy neighbors, Krampus, and Kylo Ren

Your adventurer must progress towards something in a 'straight line' 
(no mazes), no more than 10 steps/moves/transitions/time slices away from the start.

With each step of progress, it must be possible for the adventurer
to collect some amount of your chosen random trinket, or be attacked. 
Other things can happen as well, but those two must be possible.

There must be at least three possible enemies you encounter. 
You should be using some element of random chance so it is possible that 
on a particular play of the game, we might not encounter one or more of the enemies, 
but there should be at least three possibilities.

The game must end. It cannot be infinite. 
Your adventurer may make it to the goal or not make it to the goal, 
but the game must end at some point without errors 
(i.e., no Exceptions from Python to end the game).

Once the game is over, you must at least output
the total number of your chosen trinkets the adventurer collected 
and the final amount of their personal resource. 
You can output other things as well as they are relevant to your adventure game,
but trinket count and personal resource amount are required.