# Gym-Snake-AI

Environment used: [gym-snake](https://github.com/grantsrb/Gym-Snake)

## Description

Training an agent using tabular reinforcement learning methods on the classic snake game.

The agent has been trained using TD learning.

The algorithm used was SARSA lambda

### State Space:

The state is defined by direction of the apple with respect to the head and whether the cells next to the head contain an obstacle. An obstacle is defined as either a wall or the body of the snake.

-Direction of the apple:
 -

The agent was trained for 5000 episodes, and tested for 200 episodes.

## Results

Graphs were plotted between episode and rewards

Maximum reward recived: 53
Average reward recieved: 28.356

![image](https://user-images.githubusercontent.com/88096518/136699180-639b4a14-1cd3-4cfd-a1b3-0e10c1b7c6ea.png)

alpha = 0.1

gamma = 0.8

lamda = 0.9

![gif](https://user-images.githubusercontent.com/88096518/136910303-fba4dc52-c58b-4003-aaa9-f5df3a1e873c.gif)


