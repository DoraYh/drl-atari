from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, sys, gym, time

from random_controller import RandomController


fps = 12  # frames per second (approximately)
interval = 1./fps  # interval between consecutive frames

# make and initialize the game environment
env = gym.make("LunarLanderContinuous-v2")
controller = RandomController(("continuous", [(0., 1.), (-1., 1.)]))


def rollout(obs=None, reward=None, raw_pixels=None):
    """
    Read action from keyboard state -> take action in the env -> get result
        frame
    """
    global env, controller
    action = controller.get_continuous_action(obs, reward, raw_pixels)
    obs, r, done, _ = env.step(action)
    raw_pixels = env.render(mode="rgb_array")
    env.render(mode="human")
    return obs, r, raw_pixels, done


if __name__ == "__main__":
    env.render(mode="human")
    raw_pixels = env.render(mode="rgb_array")
    obs = env.reset()
    r = 0.
    while True:
        obs, r, raw_pixels, done = rollout(obs, r, raw_pixels)
        if done:
            break
        time.sleep(interval)
