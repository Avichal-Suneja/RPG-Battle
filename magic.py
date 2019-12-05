import random

class spell:
	def __init__(self, name, cost, dmg, kind):
		self.name = name
		self.cost = cost
		self.dmg = dmg
		self.kind = kind

	def generate_damage(self):
		low = self.dmg - 15
		high = self.dmg + 15
		return random.randrange(low,high)

