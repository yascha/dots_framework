dots_framework
==============

Framework to play a dots game between multiple bots



#### Overview
- each bot will be called with a string of characters which represent the game and board states
- bots will make a single move per incantation

#### Installation
To run the dots framework, the following libraries must be installed:
- python27-colorama

All dependencies can be installed by running the following command:
```
make install-deps
```

#### API
- moves must be sent to the framework as a series of (x,y) coordinates where (0,0) is the bottom left corner of the board


##### Things that need to be passed to each bot:
- board state
- number of remaining moves
- remaining time in s
- current score?


