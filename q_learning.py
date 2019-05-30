import numpy as np
import gym
import random
from time import sleep

env = gym.make('Taxi-v2')  # inicjacja środowiska
Q = np.zeros((env.observation_space.n, env.action_space.n))  # inicjacja Q-Table

train_epochs = 50000
test_epochs = 3
max_steps = 100
l_rate = 0.6
d_rate = 0.6
ex_rate = 1.0
max_ex_rate = 1.0
min_ex_rate = 0.01
drop_rate = 0.01  # jak szybko eksploracja przechodzi w eksploatację

# uczenie
for i in range(train_epochs):
    state = env.reset()
    finished = False

    for step in range(max_steps):
        t = random.uniform(0, 1)  # wybór między eksploracją a eksploatacją
        if t > ex_rate:
            action = np.argmax(Q[state, :])
        else:
            action = env.action_space.sample()  # losowa akcja

        new_state, reward, finished, _ = env.step(action)
        Q[state, action] += l_rate * (reward + d_rate * np.max(Q[new_state, :]) - Q[state, action])  # Bellman
        state = new_state

        if finished:
            break

    ex_rate = min_ex_rate + (max_ex_rate - min_ex_rate) * np.exp(-drop_rate * i)

# gotowy bot
for i in range(test_epochs):
    state = env.reset()
    finished = False
    print('Ride', i+1)

    for step in range(max_steps):
        env.render()
        action = np.argmax(Q[state, :])

        new_state, _, finished, _ = env.step(action)

        if finished:
            break

        state = new_state
        sleep(0.5)
    sleep(1)

env.close()
