TODO
====

1. Instead of global variables like "carmen" & "player", think about having 1 controller method (self) that has all these variables as part of its state (never have a function acting on a variable that hasn't been passed as a parameter)
1. Better clues & better clueing of what you're supposed to do
1. Additional villains and stolen items
1. Add a conception of "time" so that it makes sense for the player to have to make a choice: take the time to visit multiple clue sources within one city, or potentially skip useful information to catch up to the villain faster
1. Text-wrap more of the exposition
1. Add a "press any key to continue" bit to space out some of the exposition
1. Maybe use a dict, e.g.:

cities = {
'ind': City('name', ['sjo','slc'], 'clue'),
'sjo': City(...),
}

City:
__init__(self, name, dest, clue):

