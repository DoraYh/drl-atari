from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, sys, gym, time
from random_controller import RandomController


fps = 23  # frames per second (approximately)
interval = 1./fps  # interval between consecutive frames

# make and initialize the game environment
env = gym.make("SpaceInvaders-v0")
controller = RandomController(("discrete", [env.action_space.__dict__["n"]]))


# get observation and reward from environment
def rollout(obs=None, reward=None, raw_pixels=None):
    """
    Read action from keyboard state -> take action in the env -> get result
        frame
    """
    global env, controller
    action = controller.get_discrete_action(obs, reward, raw_pixels)
    raw_pixels, r, done, _ = env.step(action)
    env.render(mode="human")
    return None, r, raw_pixels, done


if __name__ == "__main__":
    raw_pixels = env.reset()
    env.render(mode="human")
    r = 0.
    while True:        
        _, r, raw_pixels, done = rollout(reward=r, raw_pixels=raw_pixels)
        if done:
            break
        time.sleep(interval)
