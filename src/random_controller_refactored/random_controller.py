from __future__ import absolute_import

import numpy as np
from controller_base import ControllerBase


class RandomController(ControllerBase):
    def __init__(self, action_space):
        super(RandomController, self).__init__(action_space)

    def get_discrete_action(self, obs=None, reward=None, raw_pixels=None):
        """
        Args:
            obs: numerical observations
            reward: float
            raw_pixels: np.array(shape=[height, weight, channels],
                                 dtype=np.uint8)

        Return:
            action: a valid action
        """
        if len(self.spaces) == 1:
            return np.random.randint(self.spaces[0])
        else:
            action = np.empty(shape=[len(self.spaces)], dtype=int)
            for idx, num_actions in enumerate(self.spaces):
                action[idx] = np.random.randint(num_actions)
            return action

    @staticmethod
    def rand_scale(_range):
        return _range[0] + np.random.rand()*(_range[1] - _range[0])

    def get_continuous_action(self, obs=None, reward=None, raw_pixels=None):
        if len(self.spaces) == 1:
            return self.rand_scale(self.spaces[0])
        else:
            action = np.empty(shape=[len(self.spaces)], dtype=np.float32)
            for idx, _range in enumerate(self.spaces):
                action[idx] = self.rand_scale(_range)
            return action

    def feed_obs(self, obs=None, reward=None, raw_pixels=None):
        pass
