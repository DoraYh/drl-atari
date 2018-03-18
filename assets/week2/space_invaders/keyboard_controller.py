
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
        
    def on_key_press(self, symbol, modifiers):
        if symbol in self.valid_keys:
            self.pressed[symbol] = True

    def on_key_release(self, symbol, modifiers):
        if symbol in self.valid_keys:
            self.pressed[symbol] = False

    def get_action(self, obs):
        return self.space.sample();
    
        if self.pressed[gkey.LEFT] and self.pressed[gkey.RIGHT] and self.pressed[gkey.SPACE]:
            return self.SHOOT
        elif self.pressed[gkey.LEFT] and self.pressed[gkey.SPACE]:
            return 1 + self.LEFT + self.SHOOT
        elif self.pressed[gkey.RIGHT] and self.pressed[gkey.SPACE]:
            return 1 + self.RIGHT + self.SHOOT
        elif self.pressed[gkey.LEFT] and self.pressed[gkey.RIGHT]:
            return 0
        elif self.pressed[gkey.LEFT]:
            return self.LEFT
        elif self.pressed[gkey.RIGHT]:
            return self.RIGHT
        elif self.pressed[gkey.SPACE]:
            return self.SHOOT
        else:
            return 0


if __name__ == "__main__":
    print("No unittestings available.")

