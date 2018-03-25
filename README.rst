++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
DRL-Agent: Playing Games with Deep Reinforcement Learning
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**[Progress Branch]**:
*This branch is only for tracking progress, and all code should*
*be submitted to master branch via pull requests*.

**[About the Final Score]**:
*The final score of this course would largely depend*
*on your participation in this project, but not only the final*
*code.*


################################################################################


.. contents:: **[Table of Contents]**:
    :depth: 2


################################################################################


Week 1: Preliminaries
================================================================================

**[Tips]**:
*Check correspondent item in Projects board* (`Spring-2018`_)
*once you get something done*.

.. _`Spring-2018`: https://github.com/lukeluochina/drl-atari/projects/


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


Week 2: Prepare the Environments
================================================================================

**[Tips]**:
*Check correspondent item in Projects board* (`Spring-2018`_)
*once you get something done*.

.. _`Spring-2018`: https://github.com/lukeluochina/drl-atari/projects/


Recall
--------------------------------------------------------------------------------

Before we diving into the code and the environments, we recall **the target of**
**our project**: we are aiming at building game agents, which interact with
the environments and should achieve human-level control. Intelligence of
our agents would come from Deep Reinforcement Learning.

In this week, we would prepare the game environments and get some basic
knowledge about Reinforcement Learning.


Install OpenAI Gym
--------------------------------------------------------------------------------

First we would install the "playground", OpenAI Gym for our DRL algorithms.
OpenAI Gym is "a toolkit for developing and comparing reinforcement learning
algorithms", as described in `its GitHub Repository`_.

.. _`its GitHub Repository`: https://github.com/openai/gym

Steps for installing it are concluded as below:

.. code:: bash

    (anaconda-py3)$ sudo apt-get install git g++ cmake zlib1g-dev -y
    (anaconda-py3)$ pip install gym==0.10.3
    (anaconda-py3)$ git clone https://github.com/openai/gym.git && cd gym
    # for atari games (e.g., "SpaceInvaders-v0")
    (anaconda-py3)$ pip install -e ".[atari]"

In this project, Han is going to use DQN to play "SpaceInvaders-v0", and so the
above environment is sufficient. Ruiqi will concerns on continuous control
problem and so should also install ``box2d`` environment (we would play the game
"LunarLanderContinuous-v2" in it with DRL in the future but before that, knowing
about ``atari`` is a good start).

.. code:: bash

    # only for games based on box2d (e.g. "LunarLander-v2")
    (anaconda-py3)$ sudo apt-get install build-essential python3-dev swig3.0 -y
    (anaconda-py3)$ sudo ln -s /usr/bin/swig3.0 /usr/bin/swig
    (anaconda-py3)$ pip install box2d==2.3.2 box2d-kengz==2.3.3
    (anaconda-py3)$ pip install box2d-py==2.3.1 -I
    (anaconda-py3)$ pip install -e ".[box2d]"

To validate the installation of ``atari`` game environments, you could run the
commands below:

.. code:: python

    >>> import gym
    >>> env = gym.make("SpaceInvaders-v0")
    >>> obs = env.reset()
    >>> obs, r, done, _ = env.step(0)

To validate the installation of ``box2d`` environments, run commands:

.. code:: python

    >>> import gym
    >>> import numpy as np
    >>> env = gym.make("LunarLanderContinuous-v2")
    >>> obs = env.reset()
    >>> obs, r, done, _ = env.step(np.array([0., 0.]))

If there throws no exception, then the installed environment should work.
For more details on the environments, see `OpenAI Gym Docs`_.

.. _`OpenAI Gym Docs`: https://gym.openai.com/docs/


Wrappers for Human Players
--------------------------------------------------------------------------------

To get you understand what you are going to do with DRL in the following weeks
intuitively, I (@lukeluochina) wrapped these two learning environments (i.e., 
`"SpaceInvaders-v0"`_ and `"LunarLanderContinuous-v2"`_) with some gaming
logics, so you can play them and learn by yourself first.

.. _`"SpaceInvaders-v0"`: assets/week2/space_invaders/keyboard_space_invaders.py
.. _`"LunarLanderContinuous-v2"`: assets/week2/lunar_lander/keyboard_lunar_lander.py

**[Tips]**:
*Since I'm neither an expert in designing games, nor*
*experienced in using OpenAI Gym, problems such as wrong logics*,
*inefficient implementation are very likely to appear in my wrappers*.
*So be careful! And any kind of suggestions are welcomed*.


Coding Task: Build Random Agents (Week2)
--------------------------------------------------------------------------------

**Coding task in this week is to build random agents for your games**.
Random agents you build in this project should only differ from intelligent
agents in the way they process inputs,
which is to say, before each step, your random agents should still get
sufficient inputs (like raw pixels, positions, velocity, etc.), then ignore
them, pick valid action randomly, and at last go on with the selected action.

**[Tips]**:
*If you are confused by my poor English, feel free to ask me in Chinese via*
*WeChat group*.

Before **2018.03.18 23:59**, you should submit your code for random agents.
(Instructions for submitting code would be updated later.)


Reading Task (Week2, Week3)
--------------------------------------------------------------------------------

**[Reinforcement Learning: An Introduction, Sutton and Barto 2012]**:

- Chapter 3.6 MDP
- Chapter 3.7 Value Functions
- Chapter 4.1 Policy Evaluation
- Chapter 4.2 Policy Improvement
- Chapter 4.3 Policy Iteration
- Chapter 4.4 Value Iteration

Before **2018.03.25 23:59**, you should hand in a memo explaining the terms
"MDP", "value function", "policy evaluation", "policy improvement",
"policy iteration", and "value iteration" in your words. You can write the memo
either in English or in Chinese, depending on your preference.


################################################################################


Week3: Reinforcement Leaning Basics
================================================================================

Go on finishing the reading task.


################################################################################


Week4: Paper Reading
================================================================================

Read the paper *Playing Atari with Deep Reinforcement Learning* [1].

Before **2018.04.01 23:59**, you should hand in a memo summarizing this paper.
There are plenty of materials you can refer to on the Internet,
but make sure you don't copy them.


################################################################################


References
================================================================================

[1] Mnih, Volodymyr, et al. "Playing atari with deep reinforcement learning." arXiv preprint arXiv:1312.5602 (2013).
