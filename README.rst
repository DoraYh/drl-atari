++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
DRL-Atari: Playing Atari Games with Deep Reinforcement Learning
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**[Progress Branch]**:
*This branch is only for tracking progress, and all codes should*
*be submitted to master branch via pull requests*.

**[About the Final Score]**:
*The final score of this course would largely depend*
*on your participation in this project, but not only the final*
*codes.*


################################################################################


.. contents:: **[Table of Contents]**:
    :depth: 2


################################################################################


Week 1: Preliminaries
================================================================================

**[Tips]**:
*Check correspondent item in Projects board* (`Spring-2018`_)
*once you get something done*.

.. _`Spring-2018`: https://github.com/lukeluochina/drl-atari/projects/1


Prepare your operating system
--------------------------------------------------------------------------------

We use Ubuntu 16.04 LTS in this project, and any releases with
Ubuntu 16.04 should work, such as ``ubuntu-16.04.4-desktop-amd``,
``Kubuntu 16.04.4 LTS``, ``ubuntu-16.04.4-server-amd``.

If you don't have access to a computer with Ubuntu 16.04 and
you don't want to enable Dual Boot on your current computer,
``VirtualBox`` may be a good alternative.

In this course, you are strongly suggested to get familiar with
using Shell commands in Linux.

.. csv-table:: Links
    :header: "Name", "URL"

    "Ubuntu 16.04", "http://releases.ubuntu.com/16.04/"
    "VirtualBox", "https://www.virtualbox.org/"


Prepare your Python environment
--------------------------------------------------------------------------------

We use Python 3.6 in this project, and the Anaconda release is
recommended (which would significantly reduce your time spent
in setting-up environments).

.. csv-table:: Links
    :header: "Name", "URL"

    "Anaconda For Linux Installer", "https://www.anaconda.com/download/#linux"


Get familiar with ``NumPy``
--------------------------------------------------------------------------------

Follow the sections ``Python`` and ``NumPy`` of the `tutorial`_ in
Stanford cs231n.

.. _`tutorial`: http://cs231n.github.io/python-numpy-tutorial/

**[Tips]**:
*Feel free to skip this part if you are already experienced in it*.


Get familiar with ``Jupyter Notebook``
--------------------------------------------------------------------------------

Explore ``Jupyter Notebook`` yourself with the help of two cheat sheets
in the `assets`_.

.. _`assets`: assets/week1/

**[Tips]**:
*Feel free to skip this part if you are already experienced in it*.


################################################################################


Week 2: Prepare the Atari Emulators
================================================================================

**[Tips]**:
*Check correspondent item in Projects board* (`Spring-2018`_)
*once you get something done*.

.. _`Spring-2018`: https://github.com/lukeluochina/drl-atari/projects/1


Install OpenAI Gym
--------------------------------------------------------------------------------

You should install ``gym`` as well as the ``atari`` dependency in this part.
Main steps are concluded as below:

.. code:: bash

    (anaconda-py3)$ sudo apt install g++ cmake zlib1g-dev
    (anaconda-py3)$ pip install gym
    (anaconda-py3)$ git clone https://github.com/openai/gym.git && cd gym
    (anaconda-py3)$ pip install -e ".[atari]"

You could run `random_agent.py`_ to validate your installation. And for better
understanding, you should also refer to `OpenAI Gym Docs`_.

.. _`random_agent.py`: assets/week2/random_agent.py
.. _`OpenAI Gym Docs`: https://gym.openai.com/docs/


OpenAI Gym for Human Players
--------------------------------------------------------------------------------

Refer to the example from `OpenAI Gym`_.

.. _`OpenAI Gym`: https://github.com/openai/gym/blob/master/examples/agents/keyboard_agent.py


A Redundant but More Friendly Wrapper for OpenAI Gym
--------------------------------------------------------------------------------

Refer to the project `gym-tracker`_.

.. _`gym-tracker`: https://github.com/alvinwan/gym-tracker


Get it Off-the-shelf for Newbies to Atari Games with Illustrative Guides
--------------------------------------------------------------------------------

Refer to a DQN `model`_.

.. _`model`: https://github.com/devsisters/DQN-tensorflow/blob/master/assets/model.png
