"""
Test yourself as a learning agent with "LunarLanderContinuous-v2"!
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, sys, gym, time, pyglet
from random_controller import Controller, Monitor




fps = 12  # frames per second (approximately)
interval = 1./fps  # interval between consecutive frames

# make and initialize the game environment
env = gym.make("LunarLanderContinuous-v2")
env.render(mode="human")

# rebind key events to custom controller
controller = Controller()
monitor = Monitor()


def rollout():
    """
    Read action from keyboard state -> take action in the env -> get result
        frame
    """
    global env, controller, monitor
    controller.update()
    action = controller.get_action()
    obs, r, done, _ = env.step(action)
    monitor.update(action=action, obs=obs, score=r)
    arr = env.render(mode="rgb_array")
    controller.feedback(obs = obs, reward = r, rgb = arr)
    return obs, r, done


if __name__ == "__main__":
    tot_r = 0.
    env.reset()
    while True:
        _, r, done = rollout()
        if done:
            break
        time.sleep(interval)