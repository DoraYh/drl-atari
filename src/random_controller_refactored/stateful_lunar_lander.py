from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os, time
import numpy as np
import gym

from random_controller import RandomController


class State(object):
    def __init__(self, delta=1., h_delta=None, v_delta=None):
        self.HORIZONTAL = 0
        self.VERTICAL = 1
        self.powers = {direction: 0. for direction in [self.HORIZONTAL,
            self.VERTICAL]}
        # power delta for each update step
        self.h_delta = h_delta if h_delta is not None else delta
        self.v_delta = v_delta if v_delta is not None else delta
        # whether the key is being pressed
        self.valid_keys = ["A", "D", "U", "J"]

    # TODO(lukeluochina): using exponential function and conditional
    # statements in critical control steps might hurt performance
    @staticmethod
    def _act1(x):
        """
        regulate the power of the horizontal engines to [-1., -0.5] or [0.5, 1.]
        with sigmoid function
        """
        y = 1./( 1. + np.exp(x/3.) ) - 0.5
        if y < 0. - 1e-5:
            return y - 0.5
        elif y > 0. + 1e-5:
            return y + 0.5
        else:
            return 0.

    # TODO(lukeluochina): using exponential function in critical control
    # steps might hurt performance
    @staticmethod
    def _act2(x):
        """
        regulate the power of the main engine to [0., 1.] with sigmoid function
        """
        return 2./(1+np.exp(x/3.))-1.

    def get_action(self, pressed):
        """
        update the powers according to the given state and return the action,
        note that value of the powers are coupled with the activation functions
        `_act1` and `_act2`
        """
        if pressed[2] and not pressed[3]:
            self.powers[self.VERTICAL] -= self.v_delta
            # at most 16 steps
            self.powers[self.VERTICAL] = max(-16*self.v_delta,
                self.powers[self.VERTICAL])
        elif pressed[3] and not pressed[2]:
            self.powers[self.VERTICAL] += self.v_delta
            self.powers[self.VERTICAL] = min(0., self.powers[self.VERTICAL])

        if pressed[0] and not pressed[1]:
            self.powers[self.HORIZONTAL] = min(0., self.powers[self.HORIZONTAL])
            self.powers[self.HORIZONTAL] -= self.h_delta
        elif pressed[1] and not pressed[0]:
            self.powers[self.HORIZONTAL] = max(0., self.powers[self.HORIZONTAL])
            self.powers[self.HORIZONTAL] += self.h_delta
        else:
            self.powers[self.HORIZONTAL] = 0.

        return np.array([self._act2(self.powers[self.VERTICAL]),
            self._act1(self.powers[self.HORIZONTAL])], dtype=np.float32)


fps = 12  # frames per second (approximately)
interval = 1./fps  # interval between consecutive frames

# make and initialize the game environment
env = gym.make("LunarLanderContinuous-v2")
controller = RandomController(("discrete", [2, 2, 2, 2]))
state = State()


def rollout(obs=None, reward=None, raw_pixels=None):
    """
    Read action from keyboard state -> take action in the env -> get result
        frame
    """
    global env, controller, state
    _action = controller.get_discrete_action(obs, reward, raw_pixels)
    action = state.get_action(_action)
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
