# Cycle-CSE210-05
Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python .\__main__.py
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- game                (source code for game)
  +-- casting           (main object classes for game)
  +-- directing         (main class to run game)
  +-- scripting         (classes that control movement and events)
  +-- services          (classes for keyboard events and video service)
  +-- shared            (classes to help with visual effect and placement)
+-- __main__.py         (entry point for program)
+-- constants.py        (constant values)
+-- README.md           (general info)
```
## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Rules
---
Players can move up, down, left and right
* Player 1 moves using the W, S, A and D keys
* Player 2 moves using the I, K, J and L keys
As the players move their tails will grow and each player will try to maneuver their tails to block
their opponents path. If a player collides with their opponents tail the game is over.

## Authors
---
 # Kylar Sorensen    (Adjusting actor controls to handle two snakes.)
 # McKay Thomas      (Handling the second snake and changing the starting positions.)
 # Zak Sattler       (Handling the logic for tail growth every time the snake changes it's location.)
 # Brandon Smith     (Adding two classes player1 and player2 using polymorphism and inheritance on repare body and grow tail methods. Add README.)
 # Garret Cooper     (Adding the logic to handle collision between segments and adding a point to the snake that didn't collide.)