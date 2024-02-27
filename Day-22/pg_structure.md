# Pong Game Breakdown

## Modules

Pong Game consists of a **ball**, **scoring**, and **player paddles** with key movements, ball movements, and ability to reset.

### Create screen

1. Get the screen and coordinate system up and running

### Create Player paddles and movement

Here we will need play paddle class that has a movement system, moves on key strokes, fixed movemenet up and down on the coordinate system, and can't go above or below the screen size.

paddle will have weidth of 20
height 200
xpos = 350
y_pos = 0

2. Create Paddle 1
3. Create Paddle 2

### Ball Module

Here we will need to create a ball class that can move, handle change in directions from players, and interact with the boundaries of the game.

4. Create ball and move across screen
5. Detect collsion with wall and bounce
6. Detect collision with paddle
7. Detect when paddle misses

### Scoring

Here we will need a scoring class that prints the score of the game, as well as game over

8. Keep score