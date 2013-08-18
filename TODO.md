TODO
====

1. Use lists instead of tuples
2. Learn to use stringformatting when outputting (e.g. to a string or stdout)
3. Minimize repeated operations - e.g. int(path), just assign it to a variable
4. Instead of global variables like "carmen" & "player", think about having 1 controller method (self) that has all these variables as part of its state (never have a function acting on a variable that hasn't been passed as a parameter)
5. Better clues & better clueing of what you're supposed to do
6. Additional villains and stolen items
7. Add a conception of "time" so that it makes sense for the player to have to make a choice: take the time to visit multiple clue sources within one city, or potentially skip useful information to catch up to the villain faster
8. Maybe use a dict, e.g.:

cities = {
'ind': City('name', ['sjo','slc'], 'clue'),
'sjo': City(...),
}

City:
__init__(self, name, dest, clue):


