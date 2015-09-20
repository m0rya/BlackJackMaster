class Player(object):
	def __init__(self):
		self.handCard = []
		return

	def getCard(self,mark, num):
		self.handCard.append([mark,num])

	def showHandCard(self):
		print self.handCard

	def resetHandCard(self):
		self.handCard = []

	def getScore(self):
		score = [0,0]
		for i in range(len(self.handCard)):
			if self.handCard[i][1] > 10:
				score[0] += 10
				score[1] += 10
			elif self.handCard[i][1] == 0:
				score[0] += 1
				score[1] += 11
				
			else:
				score[0] += self.handCard[i][1]
				score[1] += self.handCard[i][1]
				
		#return score
		return score
		'''
		if score[0] == score[1]:
			return score[0]
		else:
			return score
		'''

#======Test======
if False:
	player = Player()

	player.getCard(2,3)
	player.getCard(4,6)

	player.getCard(2,13)
	player.getCard(3, 0)
	player.showHandCard()
	print str(player.getScore())
	player.resetHandCard()

	player.showHandCard()
