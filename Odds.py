
class Odds(object):

	def __init__(self,decks,  player, dealer):
		self.decks = decks
		self.player = player
		self.dealer = dealer
	
	def calcBurstPlayer(self):
		score = self.player.getScore()
	
		#if dont have 'A'
		if score[0] == score[1]:
			if score[0]  <= 11 or score[0] == 21:
				return 0

			else:
				borderLine = 21-score[0]
				way = 0
				for i in range(borderLine+1,11):
					way += self.decks.countSpecificNum(i)

				allCards = self.decks.countAllCard()
				
				#print way
				#print allCards
				burst =  float(way)/allCards*100.0
				burst = round(burst,2)
				
				#17~21
				probability = []
				for i in range(5):
					if score[0] < 17+i:
						tmp = 17+i-score[0]
						way = self.decks.countSpecificNum(tmp)
						tmpResult = float(way)/allCards*100
						probability[0] += (round(tmpResult,2))

					else:
						probability[0] += 0
				probability.append(100-probability[0]-burst)
				probability.append(burst)
				
				return probability

	
	def calcDealerHand(self):
		scoreTmp =  self.dealer.getScore()
		score = scoreTmp[0]
		allCards = self.decks.countAllCard()
		result = []

		#score is A
		if score == 1:
			minCount = 0

			#under 16
			for i in range(1,6):
				minCount += self.decks.countSpecificNum(i)
			tmpResult = (float(minCount)/allCards*100)
			result.append(round(tmpResult,2))

			#17-21
			for i in range(6,11):
				minCount = self.decks.countSpecificNum(i)
				tmpResult = (float(minCount)/allCards*100)
				result.append(round(tmpResult,2))
			return result	

		#score is higher than 7
		if score > 6:
			#under 16
			tmp = 16-score
			minCount = 0

			for i in range(1,tmp+1):
				minCount += self.decks.countSpecificNum(i)
			tmpResult = (float(minCount)/allCards*100)
			result.append(round(tmpResult,2))


			#17-21
			for i in range(7,11):
				if score >= i:
					minCount = self.decks.countSpecificNum(i+10-score)
					tmpResult = (float(minCount)/allCards*100)
					result.append(round(tmpResult,2))
				else:
					result.append(0)

			return result
					

		#score is lower than 6
		if score <= 6:
			result = [100,0,0,0,0,0]
			return result


			
			
#=======Test======
if False:
	player = Player.Player()
	dealer = Player.Player()
	decks = Deck.Decks(3)

	odds = Odds(decks, player,dealer)
	
	print decks.getAllRemaining()

	player.getCard(0,7)
#	player.getCard(0,10)
	
	decks.deleteCard(0,7)
#	decks.deleteCard(0,10)
	
	dealer.getCard(0,1)
	decks.deleteCard(0,1)

	for i in range(3):
		for j in range(4):
			decks.deleteCard(j,10)
			decks.deleteCard(j,11)
			decks.deleteCard(j,12)
			decks.deleteCard(j,13)
			
	'''	
	for i in range(20):
		randMark = random.randint(0,3)
		randNum = random.randint(0,12)

		decks.deleteCard(randMark, randNum)
	'''	
	print decks.getAllRemaining()
	print odds.calcDealerHand()	
