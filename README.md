# Gym-Snake-AI

Environment used: [gym-snake](https://github.com/grantsrb/Gym-Snake)

## Description

Training an agent using tabular reinforcement learning methods on the classic snake game.

The agent has been trained using TD learning.

The algorithm used was SARSA lambda

### State Space:

The state is defined by direction of the apple with respect to the head and whether the cells next to the head contain an obstacle. An obstacle is defined as either a wall or the body of the snake.

Direction of the apple:
 -Four variables were defined to store 1 if the apple is in front, to the left, behind, or to the right of the snake else the value is 0.
 -These variables are defined with respect to the head of the snake.
 
Obstacles:
 -Obstacles are defined as either the body of the snake or the wall.
 -Three variables were defined to store 1 if there is an obstacle in front, to the left, or to the right of the snake else the value is 0.

This reluts in a state space of the size = (2x2x2x2) x (2x2x2) = 128.
 
The agent was trained for 5000 episodes, and tested for 200 episodes.

## Results

Graphs were plotted between episode and rewards

Maximum reward recived: 53
Average reward recieved: 28.356

![image](https://user-images.githubusercontent.com/88096518/136699180-639b4a14-1cd3-4cfd-a1b3-0e10c1b7c6ea.png)

alpha = 0.1

gamma = 0.8

lamda = 0.9

Training:

![Training](https://user-images.githubusercontent.com/88096518/137182424-fa8f1313-38e2-4b9b-b7e4-281cb2898dd3.png)

### Execution:
![gif](https://user-images.githubusercontent.com/88096518/136910303-fba4dc52-c58b-4003-aaa9-f5df3a1e873c.gif)


