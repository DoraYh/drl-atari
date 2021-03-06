"""
Test yourself as a learning agent with "SpaceInvaders-v0"!
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, sys, gym, time, pyglet
from keyboard_controller import Controller


fps = 23  # frames per second (approximately)
interval = 1./fps  # interval between consecutive frames

# make and initialize the game environment
env = gym.make("SpaceInvaders-v0")
env.render(mode="human")

# rebind key events to custom controller
controller = Controller()
env.unwrapped.viewer.window.on_key_press = controller.on_key_press
env.unwrapped.viewer.window.on_key_release = controller.on_key_release


def rollout():
    """
    Read action from keyboard state -> take action in the env -> get result
        frame
    """
    global env, controller
    action = controller.get_action()
    obs, r, done, _ = env.step(action)
    env.render(mode="human")
    return obs, r, done


if __name__ == "__main__":
    tot_r = 0.
    env.reset()
    while True:
        _, r, done = rollout()
        if done:
            break
        time.sleep(interval)
