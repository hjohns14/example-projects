import numpy as np
import gym
import matplotlib.pyplot as plt



env = gym.make("MountainCar-v0")

'''
print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)
'''

# lEARNING RATE
LEARNING_RATE = 0.1
# How important the future actions are.
DISCOUNT = 0.95
EPISODES =25_001
SHOW_EVERY = 5000
#20x20 we just done want to hardcode it
DICRETE_OS_SIZE = [40] * len(env.observation_space.high)
discrete_os_win_size = (env.observation_space.high - env.observation_space.low)/DICRETE_OS_SIZE
epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPSILON_DECAY = EPISODES // 2
STATS_EVERY = 100

epsilon_decay_value = epsilon /(END_EPSILON_DECAY - START_EPSILON_DECAYING)

#The low and high is the reward. 0 is reaching the flag
#should be 20x20x3
q_table = np.random.uniform(low=-2, high=0, size=(DICRETE_OS_SIZE + [env.action_space.n]))
ep_rewards = []
aggr_ep_rewards = {'ep': [], 'avg': [], 'min': [], 'max': []}



#Convert continous new_state into discrete state
def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low)/ discrete_os_win_size

    return tuple(discrete_state.astype(np.int))





for episode in range(EPISODES):
    episode_reward = 0
    discrete_state =get_discrete_state(env.reset())
    if episode % SHOW_EVERY == 0:
        render = True
    
    else:
        render = False

    done = False
    while not done:

        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)

        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        new_discrete_state = get_discrete_state(new_state)

    

        if render:
            env.render()
        
        
        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action,)]

            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

            q_table[discrete_state +(action, )] = new_q
        elif new_state[0] >= env.goal_position:
            print(f"Completed by episode {episode}")
            q_table[discrete_state + (action, )] = 0


        discrete_state = new_discrete_state
    if END_EPSILON_DECAY >= episode >= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

    ep_rewards.append(episode_reward)

    if not episode % 100:
        np.save(f"data/q_tables/{episode}-q_table.npy", q_table)


    if not episode % STATS_EVERY: # == 0
        average_reward = sum(ep_rewards [-STATS_EVERY:])/len(ep_rewards[-STATS_EVERY:])
        aggr_ep_rewards['ep'].append(episode)
        aggr_ep_rewards['avg'].append(average_reward)
        aggr_ep_rewards['min'].append(min(ep_rewards [-STATS_EVERY:]))
        aggr_ep_rewards['max'].append(max(ep_rewards [-STATS_EVERY:]))
        print(f"Episode: {episode}. avg: {average_reward}. min: {min(ep_rewards [- SHOW_EVERY:])}. Max: {max(ep_rewards [- SHOW_EVERY:])}")
env.close()

plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['avg'], label="avg")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['min'], label="min")
plt.plot(aggr_ep_rewards['ep'], aggr_ep_rewards['max'], label="max")
plt.legend(loc=4)
plt.show()