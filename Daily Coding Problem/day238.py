import numpy

''' Unfinished '''

class Deck:
	def __init__(self):
		self.two = 2
		self.three = 3
		self.four = 4
		self.five = 5
		self.six = 6
		self.seven = 7
		self.eight = 8
		self.nine = 9
		self.ten = 10
		self.face = 10
		self.deck = []

		self.compile()

	def print_deck(self):
		print(self.deck)

	def compile(self):
		i = 2
		while i<=10:
			self.deck.append([i]* 4)
			print(self.deck, "First")

			if i > 2:
				print(i)
				self.deck[0] += self.deck[1]
				self.deck.remove(self.deck[1])
				print(self.deck, "second")
			else:
				pass

			i += 1
		print(self.deck)



deck = Deck()
