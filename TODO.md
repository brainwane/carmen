TODO
====

1. Learn to use stringformatting when outputting (e.g. to a string or stdout)
2. Minimize repeated operations - e.g. int(path), just assign it to a variable
3. Instead of global variables like "carmen" & "player", think about having 1 controller method (self) that has all these variables as part of its state (never have a function acting on a variable that hasn't been passed as a parameter)
4. Better clues & better clueing of what you're supposed to do
5. Additional villains and stolen items
6. Add a conception of "time" so that it makes sense for the player to have to make a choice: take the time to visit multiple clue sources within one city, or potentially skip useful information to catch up to the villain faster
7. Maybe use a dict, e.g.:

cities = {
'ind': City('name', ['sjo','slc'], 'clue'),
'sjo': City(...),
}

City:
__init__(self, name, dest, clue):

