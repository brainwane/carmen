TODO
====

1. After winning, ask "play again?" If yes, start new game object with same player object but restarted location; if no, sys.exit
1. Text-wrap more of the exposition
1. Better clues & better clueing of what you're supposed to do
1. Additional villains and stolen items
1. Add a conception of "time" so that it makes sense for the player to have to make a choice: take the time to visit multiple clue sources within one city, or potentially skip useful information to catch up to the villain faster
1. Separate presentation and logic (e.g., don't print in any of the choice steps)
1. Add a "press any key to continue" bit to space out some of the exposition
1. Maybe use a dict, e.g.:

cities = {
'ind': City('name', ['sjo','slc'], 'clue'),
'sjo': City(...),
}

City:
__init__(self, name, dest, clue):

