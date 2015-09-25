class Deck(object):
	def __init__(self):
		self.cards = [[1 for i in range(13)] for j in range(4)]

	def deleteCard(self, mark, num):
		self.cards[mark][num-1] = 0

	def reset(self):
		self.cards = [[1 for i in range(13)] for j in range(4)]

	def showCardStatus(self):
		for i in range(len(self.cards)):
			for j in range(len(self.cards[i])):
				print self.cards[i][j],

			print

	def countRemaining(self):
		count = 0
		for i in range(len(self.cards)):
			for j in range(len(self.cards[i])):
				if self.cards[i][j] == 1:
					count += 1		
		return count
	
	def countSpecificNum(self, num):
		
		count = 0
		if num != 10:
			for i in range(len(self.cards)):
				if self.cards[i][num-1] == 1:
					count += 1
		elif num == 10:
			for i in range(len(self.cards)):
				for j in range(9,13):
					if self.cards[i][j] == 1:
						count += 1
						
		return count


class Decks(object):
	def __init__(self, deckNum):
		self.deckNum = deckNum 

		self.decks = [Deck() for i in range(deckNum)]

	def showDecksCardStatus(self):
		for i in range(self.deckNum):
			self.decks[i].showCardStatus()

			print "======================"


	def deleteCard(self, mark, num):
		for i in range(len(self.decks)):
			if self.decks[i].cards[mark][num-1] == 1:
				self.decks[i].deleteCard(mark, num)
				return

		else:
			print "Error: over flow card"

	def countAllCard(self):
		count = 0
		for i in range(self.deckNum):
			count += self.decks[i].countRemaining()

		return count



	def countSpecificNum(self, num):
		count = 0
		for i in range(self.deckNum):
			count += self.decks[i].countSpecificNum(num)

		return count

	def getAllRemaining(self):
		result=[]

		for i in range(1,14):
			tmpCount = self.countSpecificNum(i)
			if i == 10:
				tmp = 0
				for m in range(self.deckNum):
					for n in range(11,14):
						tmp += self.decks[m].countSpecificNum(n)

				tmpCount -= tmp
			result.append(tmpCount)

		return result
		



#=======Test=========
if False:

	import random
	decks = Decks(2)
	print decks.countAllCard()
	print decks.countSpecificCard(1)


	for i in range(20):
		randMark = random.randint(0,3)
		randNum  = random.randint(0,12)

		decks.deleteCard(randMark, randNum)
	
	print decks.countAllCard()
	print decks.countSpecificCard(1)

	decks.showDecksCardStatus()
