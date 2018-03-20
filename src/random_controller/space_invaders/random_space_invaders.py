
# coding: utf-8

# In[1]:


"""
Test yourself as a learning agent with "SpaceInvaders-v0"!
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, sys, gym, time, pyglet
from random_controller import Controller


fps = 23  # frames per second (approximately)
interval = 1./fps  # interval between consecutive frames

# make and initialize the game environment
env = gym.make("SpaceInvaders-v0")
env.render(mode="human")

# rebind key events to custom controller
controller = Controller()

# get observation and reward from environment
def rollout(obs, reward):
    """
    Read action from keyboard state -> take action in the env -> get result
        frame
    """
    global env, controller
    
    """
    select the action by the raw pixels and reward
    """    
    action = controller.get_action(obs, reward)   
    
    obs, r, done, _ = env.step(action)
    env.render(mode="human")
    return obs, r, done


if __name__ == "__main__":
    tot_r = 0.
    r = 0
    obs = env.reset()
    while True:        
        obs, r, done = rollout(obs, r)
        if done:
            break
        time.sleep(interval)

