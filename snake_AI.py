import gym
import gym_snake
import numpy as np
import random
import matplotlib.pyplot as plt

#constants for the matrix:
matrix = 2
direction = 4
actions = [0, 1, 2]
action_space = 3

#making the env
env = gym.make('snake-v0')
#env.grid_size = [8, 8]

#global variables:
epsilon = 1
total_episodes = 5200
alpha = 0.1
gamma = 0.8
lamda = 0.9

'''
define q 8D matrix
1. 0- apple is not up
   1- apple is up
2. 0- apple is not down
   1- apple is down
3. 0- apple is not right
   1- apple is right
4. 0- apple is not left
   1- apple is left
5. 0- obstacle is not up
   1- obstacle is up
6. 0- obstacle is not left
   1- obstacle is left
7. 0- obstacle is not right
   1- obstacle is right
8. actions
   0- straight
   1- clock wise
   2- anticlock wise
e = eligibility traces
'''
q = np.zeros((matrix, matrix, matrix, matrix, matrix, matrix, matrix, action_space))
e = np.zeros((matrix, matrix, matrix, matrix, matrix, matrix, matrix, action_space))

#changing actons wrt head to actions wrt the environment
def take_action(head_d, action):
    rel = [[0, 1, 3],
           [1, 2, 0],
           [2, 3, 1],
           [3, 0, 2]]
    actual_action = rel[head_d][action]
    return actual_action
    
#policy - epsilon greedy
def epsilon_greedy(apple_up, apple_down, apple_right, apple_left, ob_up, ob_left, ob_right,):
    action = 0
    
    #explore:
    if np.random.uniform(0,1) < epsilon:
        action = random.choice(actions)
        
    #greedy policy:
    else:
        action = int(np.argmax(q[apple_up, apple_down, apple_right, apple_left, ob_up, ob_left, ob_right, :]))
        
    return action

#updating q matrix after each step
def updateQ(delta):
    
    for apple_up in range(matrix):
        for apple_down in range(matrix):
            for apple_right in range(matrix):
                for apple_left in range(matrix):
                    for ob_up in range(matrix):
                        for ob_left in range(matrix):
                            for ob_right in range(matrix):
                                for a in actions:
                                    q[apple_up, apple_down, apple_right, apple_left, ob_up, ob_left, ob_right, a] += alpha * delta * e[apple_up, apple_down, apple_right, apple_left, ob_up, ob_left, ob_right, a]
                                    e[apple_up, apple_down, apple_right, apple_left, ob_up, ob_left, ob_right, a] *= gamma * lamda
                                        
#find position of the apple/fruit
def find_apple(obs):
    for x in range(0,150,10):
        for y in range(0,150,10):
            if (np.array_equal(obs[x][y],np.array([0,0,255]))):
                apple_pos_x = y // 10
                apple_pos_y = x // 10
 
    return apple_pos_x, apple_pos_y

#defining relative position of fruit with respect to the head
def relative_pos_apple(obs, h_x , h_y, h_d):
    a_x, a_y = find_apple(obs)
    apple_up, apple_down, apple_right, apple_left = 0, 0, 0, 0
    
    #for x values
    #apple is on left
    if (a_x - h_x) < 0:
        apple_left = 1
        
    #apple is on the right
    elif (a_x - h_x) > 0:
        apple_right = 1
    
    #same x coordinate
    elif(a_x - h_x) == 0:
        apple_left = 0
        apple_right = 0
        
    #for y values
    #if apple is upwards
    if (a_y - h_y) < 0:
        apple_up = 1
        
    #if apple is below
    elif (a_y - h_y) > 0:
        apple_down = 1
        
    #same y coordinate
    elif(a_y - h_y) == 0:
        apple_up = 0
        apple_down = 0
    
    
    #turning the matrix accoring to the direction of the head:
    #right
    if(h_d == 1):
        apple_up, apple_right, apple_down, apple_left = apple_right, apple_down, apple_left, apple_up
    
    #down
    elif(h_d == 2):
        apple_up, apple_right, apple_down, apple_left = apple_down, apple_left, apple_up, apple_right 
    
    #left
    elif(h_d == 3):
        apple_up, apple_right, apple_down, apple_left = apple_left, apple_up, apple_right, apple_down
        
        
    return apple_up, apple_down, apple_right, apple_left


#find if wall/body is right next to the head
def wall(h_x, h_y, h_d):
    ob_up, ob_left, ob_right, ob_down = 0, 0, 0, 0
    
    snake_body = np.array(snake.body).tolist()
    
    #wall to left
    if(h_x == 0) or [(h_x-1), h_y] in snake_body:
        ob_left = 1
    
    #wall to right
    if(h_x == 14) or [(h_x+1), h_y] in snake_body:
        ob_right = 1
        
    #wall up
    if(h_y == 0) or [h_x, h_y-1] in snake_body:
        ob_up = 1
        
    #wall down
    if(h_y == 14) or [h_x, h_y+1] in snake_body:
        ob_down = 1
        
    #turning the matrix:
    #right
    if(h_d == 1):
        ob_up, ob_right, ob_down, ob_left = ob_right, ob_down, ob_left, ob_up
        
    #down 
    elif(h_d == 2):
        ob_up, ob_right, ob_down, ob_left = ob_down, ob_left, ob_up, ob_right
        
    #left
    elif(h_d == 3):
        ob_up, ob_right, ob_down, ob_left = ob_left, ob_up, ob_right, ob_down
    
    return ob_up, ob_left, ob_right

#defining graph arrays
graph_ep = []
graph_rew = []

#start
for episode in range(total_episodes):
    
    #defining eligibility traces
    e = np.zeros((matrix, matrix, matrix, matrix, matrix, matrix, matrix, action_space))
    
    ep_reward = 0
    print("******episode ",episode, " ********")
    steps = 0
    
    obs = env.reset()
    snake = env.controller.snakes[0]

    head_d1 = snake.direction
    h_x1 , h_y1 = snake.head
    ob_up1, ob_left1, ob_right1 = wall(h_x1, h_y1, head_d1)
    
    apple_up1, apple_down1, apple_right1, apple_left1 = relative_pos_apple(obs, h_x1, h_y1, head_d1)
    
    action1 = epsilon_greedy(apple_up1, apple_down1, apple_right1, apple_left1, ob_up1, ob_left1, ob_right1)
    
    #for end of episode
    rew = 0
    #start of episode
    while(rew != -1):
        
        env.render()
        
        actual_action = take_action(head_d1, action1)
        obs, rew, done, _ = env.step(actual_action)
        h_x2 , h_y2 = snake.head
        
        head_d2 = snake.direction
        apple_up2, apple_down2, apple_right2, apple_left2 = relative_pos_apple(obs, h_x2 , h_y2, head_d2)
        ob_up2, ob_left2, ob_right2 = wall(h_x2, h_y2, head_d2)

        #Choosing the next action
        action2 = epsilon_greedy(apple_up2, apple_down2, apple_right2, apple_left2, ob_up2, ob_left2, ob_right2)
        
        #finding delta
        predict = q[apple_up1, apple_down1, apple_right1, apple_left1, ob_up1, ob_left1, ob_right1, action1]
        target = q[apple_up2, apple_down2, apple_right2, apple_left2, ob_up2, ob_left2, ob_right2, action2]
        delta = rew + gamma*target - predict
        
        #updating eligibility traces:
        e[apple_up1, apple_down1, apple_right1, apple_left1, ob_up1, ob_left1, ob_right1, action1] = 1
        
        #updating the Q-value
        updateQ(delta)
        
        #updating variables
        apple_up1, apple_down1, apple_right1, apple_left1, ob_up1, ob_left1, ob_right1, head_d1, action1 = apple_up2, apple_down2, apple_right2, apple_left2, ob_up2, ob_left2, ob_right2, head_d2, action2
        h_x1, h_y1 = h_x2, h_y2 
        
        steps += 1
        ep_reward += rew
    
    #decaying epsilon after each episode
    if(episode < 150):
        epsilon = 0.9
    else:
        epsilon = 10/(episode+10)

    print("Episode reward:", ep_reward)

    #testing for 200 episodes after training for 5000 episodes:
    if(episode > 4999):
        #updating graph var
        graph_ep.append(episode - 4999)
        graph_rew.append(ep_reward)
    
print ("Performance : ", sum(graph_rew)/200)

#print graphs episodes vs rewards
print("Graphs:")

plt.plot(graph_ep, graph_rew)
plt.title('Episode vs Rewards')
plt.show()
