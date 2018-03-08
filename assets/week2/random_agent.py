"""
This simple script is for validating the installation of `gym` package and
`atari` dependency with random agents/players.

And the rendering is slowed down with `time.sleep` for better visualization
result.

Usage:
	python random_agent.py cartpole  # for running 'CartPole-v0'
	python random_agent.py spaceinvaders  # for running 'SpaceInvaders-v0'
"""
import time


def cartPole():
	import gym
	env = gym.make("CartPole-v0")
	env.reset()
	for _ in range(100):
		env.render()
		env.step(env.action_space.sample())  # take a random sample
		time.sleep(0.02)


def spaceInvaders():
	import gym
	env = gym.make("SpaceInvaders-v0")
	env.reset()
	for _ in range(500):
		env.render()
		env.step(env.action_space.sample())  # take a random sample
		time.sleep(0.02)


if __name__ == "__main__":
	import sys
	if len(sys.argv) >= 2 and sys.argv[1] == "cartpole":
		cartPole()
	elif len(sys.argv) >= 2 and sys.argv[1] == "spaceinvaders":
		spaceInvaders()
	else:
		print("Usage:\n"
			  "\tpython random_agent.py cartpole  # for running 'CartPole-v0'\n"
			  "\tpython random_agent.py spaceinvaders  # for running 'SpaceInvaders-v0'")

