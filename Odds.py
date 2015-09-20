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
				
				print way
				print allCards
				result =  float(way)/allCards*100.0
				return round(result,2)

			
#=======Test======
import Deck
import Player
import random

if True:
	player = Player.Player()
	dealer = Player.Player()
	decks = Deck.Decks(3)

	odds = Odds(decks, player,dealer)
	
	player.getCard(0,7)
	player.getCard(0,10)
	
	decks.deleteCard(0,7)
	decks.deleteCard(0,10)

	for i in range(20):
		randMark = random.randint(0,3)
		randNum = random.randint(0,12)

		decks.deleteCard(randMark, randNum)
		

	print odds.calcBurstPlayer()
