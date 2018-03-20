from copy import deepcopy


class ControllerBase(object):
    def __init__(self, action_space):
        """Args:
            action_space: ("discrete", [num_actions]) or
                ("continuous", [(min, max)])
        """
        self._init_action_space(action_space)

    def _init_action_space(self, action_space):
        """Args:
            action_space: ("discrete", [num_actions]) or
                ("continuous", [(min, max)])
        """
        assert isinstance(action_space[1], list)
        if action_space[0] == "discrete":
            self.action_type = action_space[0]
            for num_actions in action_space[1]:
                assert isinstance(num_actions, int)
                assert num_actions > 0
            self.spaces = deepcopy(action_space[1])
        elif action_space[0] == "continuous":
            self.action_type = action_space[0]
            for _range in action_space[1]:
                assert len(_range) >= 2
                assert _range[0] < _range[1]
            self.spaces = deepcopy(action_space[1])
        else:
            raise NotImplementedError

    def get_discrete_action(self, obs=None, reward=None, raw_pixels=None):
        """Get a valid action."""
        raise NotImplementedError

    def get_continuous_action(self, obs=None, reward=None, raw_pixels=None):
        """Get a valid action."""
        raise NotImplementedError

    def feed_obs(self):
        """In some games, between taking consecutive actions, the agent might
        be able to capture observations for multiple times. In such cases,
        the agent can be fed the observations instantly without returning the
        action."""
        raise NotImplementedError
