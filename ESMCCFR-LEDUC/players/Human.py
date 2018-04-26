class Human:
	def __init__(self, rules, setup):
		self.rules = rules
		self.setup = setup

	def train(self, T=None):
		self._name = str(input("What's your name?\n"))

	def bet(self, state):
		bets = state.get_possible_bets()
		action = -1
		while (action not in bets):
			action = int(input("Select action from %s:\n" % str(bets)))
		return action

	def name(self):
		return self._name
