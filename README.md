# Gym-Snake-AI

Training an agent using RL tabular methods on gym-snake

Environment used: gym-snake: https://github.com/grantsrb/Gym-Snake

The agent has been trained using TD learning.

The algorithm used was SARSA lambda

Rewards:

-1 for game over i.e. bumping into a wall or itself

1 for eating the fruit

0 otherwise

The agent was trained for 5000 episodes, and tested for 200 episodes.

## Results

Graphs were plotted between episode and rewards

Maximum reward recived: 53
Average reward recieved: 28.356

![image](https://user-images.githubusercontent.com/88096518/136699180-639b4a14-1cd3-4cfd-a1b3-0e10c1b7c6ea.png)

alpha = 0.1

gamma = 0.8

lamda = 0.9



