
# coding: utf-8

# In[ ]:


"""
Keyboard controller
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import time
import pyglet
import random
from gym import spaces
from pyglet.window import Window as gWindow
from pyglet.window import key as gkey


class Controller(object):
    """
    mission: see wikipedia (https://en.wikipedia.org/wiki/Space_Invaders).
    
    valid actions:
        1: shoot
        2: go right
        3: go left
        4: go right + shoot
        5: go left + shoot
        0: do nothing
    """
    def __init__(self):
        """
        gkey.LEFT: go left (3)
        gkey.RIGHT: go right (2)
        gkey.SPACE: shoot (1)
        gkey.LEFT + gkey.SPACE: go left + shoot (5)
        gkey.RIGHT + gkey.SPACE: go right + shoot (4)
        None: 0
        """
        self.valid_keys = [gkey.LEFT, gkey.RIGHT, gkey.SPACE]
        self.pressed = {valid_key: False for valid_key in self.valid_keys}
        self.SHOOT = 1
        self.RIGHT = 2
        self.LEFT = 3
        self.space = spaces.Discrete(6)

    def get_action(self, obs, reward):
        """
        choose the action randomly
        """
        return random.randint(0,5);

if __name__ == "__main__":
    print("No unittestings available.")

