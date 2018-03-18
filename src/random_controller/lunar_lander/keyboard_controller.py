"""
Keyboard controller
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time
import pyglet
from pyglet.window import Window as gWindow
from pyglet.window import key as gkey
import numpy as np


class Controller(object):
    """
    mission: help control the satellite to land on the moon so that it should
        not crash, locate at the target plane ( always at (0, 0) ) and
        cost fuel as little as possible

    there are totally three engines to help the satellite
    land on the moon, one is the main engine and the other two are
    left engine and right engine
    
        ---
      //   \\
    1 ||   || 2
      -------
    //   0   \\

    in the figure above, the main engine is tagged with 0, the left engine
    and right are tagged with 1 and 2, respectively (some other documents
    might have different representation)

    we play this game via controlling the power of the main engine,
    together with using the left engine and the right to adjust the
    direction.
    
    power of the main engine is represented by a floating point number 
    within the range [0, 1] and specially, the left engine and the right
    one cannot work simultaneously, and their powers are represented
    together with one floating point number within the range [-1, 1].
    
    when the power is ranging within [-1, -0.5], the left works, and when
    the power is ranging within [0.5, 1], the right works, while no engines 
    work when it is in between [-0.5, 0.5]
    """
    def __init__(self, delta=1., h_delta=None, v_delta=None):
        """
        in our control scheme, the main engine is stateful while the left and
        the right one are stateless. it means that if you don't fire or
        you don't cool down the main engine, power of it remains unchanged. but
        to the left and the right engines, they work if and only if you are
        pressing correspondent keys

        gkey.A: fire left engine
        gkey.D: fire right engine
        gkey.U: fire main engine
        gkey.J: cool down main engine

        note that if both A and D are pressed, they counteract
        if both U and J are pressed, they counteract as well

        Args:
            delta: power delta for each update step / frame
                if you change the fps, you might need to change the delta
                as well
            h_delta: power delta for horizontal engines
            v_delta: power delta for vertical engine
        Returns:
            None
        """
        # power of different engines, indexed by directions
        # actually the powers possibly go out of [0, 1] or [-1, 1]
        # we would get them back with post-processing
        self.HORIZONTAL = 0
        self.VERTICAL = 1
        self.powers = {direction: 0. for direction in [self.HORIZONTAL,
            self.VERTICAL]}
        # power delta for each update step
        self.h_delta = h_delta if h_delta is not None else delta
        self.v_delta = v_delta if v_delta is not None else delta


    def update(self):
        """
        update the powers randomly, note that value of
        the powers are coupled with the activation functions `_act1` and `_act2`
        
        """
        self.powers[self.HORIZONTAL] = np.random.rand(1)[0]*2.-1
        self.powers[self.VERTICAL] = np.random.rand(1)[0]

    def get_action(self):
        """return np.array([
            np.float32(self.powers[self.VERTICAL]),
            np.float32(self.powers[self.HORIZONTAL])]
            , dtype=np.float32)"""
        return np.array([
            self.powers[self.VERTICAL],
            self.powers[self.HORIZONTAL]
            ]
            , dtype=np.float32)


class Monitor(object):
    """
    Simple helper class for monitoring engines, observations, and scores.
    """
    def __init__(self):
        self.engines = [0., 0., 0.]
        self.obs = None
        self.score = 0.
    
    def update(self, action=None, obs=None, score=None):
        if action is not None:
            self.engines[0] = action[0]
            self.engines[1] = \
                action[1] if action[1] > 0. else 0.
            self.engines[2] = \
                -action[1] if action[1] < 0. else 0.

        if obs is not None:
            self.obs = obs

        if score is not None:
            self.score += score

        self._print()

    def _print(self):
        os.system("clear")

        print("Main engine: {:.2f}\t\t| Left engine: {:.2f}\t| Right engine: "
              "{:.2f}\n\n"
              "Position x: {:.2f}\t\t| Position y: {:.2f}\n\n"
              "v_x: {:.2f}\t\t\t| v_y: {:.2f}\n\n"
              "angle: {:.2f}\t\t\t| angular_v: {:.2f}\n\n"
              "left_contact_ground: {}\t| right_contact_ground: {}\n\n"
              "Score: {:.2f}\n".format(
                    self.engines[0], self.engines[1], self.engines[2],
                    self.obs[0], self.obs[1],
                    self.obs[2], self.obs[3],
                    self.obs[4], self.obs[5],
                    "True" if self.obs[7] > 1e-5 else "False",
                    "True" if self.obs[6] > 1e-5 else "False",
                    self.score))


if __name__ == "__main__":
    print("No unittestings available.")
