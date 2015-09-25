import wx

class MainFrame(wx.Frame):
	def __init__(self,*args, **kwargs):
		super(MainFrame, self).__init__(args[0], **kwargs)
		self.decks = args[1]
		self.player = args[2]
		self.dealer = args[3]
		self.odds = args[4]
		self.tButton = []
		self.countText =[]

		self.ProbabilityName = [0,0,0,0]
		self.PlayerProbability = [0,0,0,0]
		self.DealerProbability = []

		self.leftPanel = wx.Panel(self,  pos = (0,0), size=(450,800))
		self.InitUI()
	
	def getRemainingCards(self):
		result = []
		for i in range(1,11):
			result.append(decks.countSpecificNum(i))

		return result
	
	def getAllTButtonStatus(self):
		result = []
		#print self.tButton
		for i in range(len(self.tButton)):
			tmp = []
			for j in range(len(self.tButton[i])):
				tmp.append(self.tButton[i][j].GetValue())

			result.append(tmp)
		return result
	
	

	#button function
	def SetRemainingData(self):
		remainingData = self.getRemainingCards()
		for i in range(10):
			self.countText[i].SetLabel(str(remainingData[i]))

	def deleteCards(self,event):
		buttonStatus = self.getAllTButtonStatus()
		
		for i in range(len(buttonStatus)):
			for j in range(len(buttonStatus[i])):
				if buttonStatus[i][j] == True:
					if j+1 > 9:
						self.decks.deleteCard(i,10)
					else:
						self.decks.deleteCard(i,j+1)

					self.tButton[i][j].SetValue(False)

		self.SetRemainingData()
		#reload probability 
		self.SetProbability()
	
		print '#done delete'

	def resetHand(self, event):
		self.player.resetHandCard()
		self.SetProbability()

	def resetDecks(self, event):
		self.decks.resetDecks()
		self.SetRemainingData()

	def SetPlayerHand(self,event):
		buttonStatus = self.getAllTButtonStatus()

		for i in range(len(buttonStatus)):
			for j in range(len(buttonStatus[i])):
				if buttonStatus[i][j]:
					self.player.getCard(i,j+1)

		self.deleteCards(None)
		self.SetProbability()
		print '#done setPlayerHand'

	def SetProbability(self):
		tmpProbability = self.odds.calcBurstPlayer()
		#print '#78# calcBusrtPlayer %s' %(tmpProbability)
		
		tmpPos =[]
		tmpSize=[]
		tmpPos.append([10,290])
		tmpPos.append([10+tmpProbability[2]*4,290])
		tmpPos.append([tmpPos[1][0],tmpPos[1][1]+20*2])
		tmpPos.append([10+(tmpProbability[2]+tmpProbability[1])*4, 290+20*2])

		tmpSize.append([tmpProbability[2]*4, 20])
		tmpSize.append([(100-tmpProbability[2])*4, 20])
		tmpSize.append([tmpProbability[1]*4, 20])
		tmpSize.append([tmpProbability[0]*4,20])
		#print '#91# PlayerProbability Num %s'%(len(self.PlayerProbability))
		#print '#92# self.PlayerProbability '
		#print self.PlayerProbability

		##hide PreStaticText
		for i in range(4):
			self.ProbabilityName[i].Hide()
			self.PlayerProbability[i].Hide()

		self.ProbabilityName[0] = wx.StaticText(self.leftPanel, wx.ID_ANY, 'Burst', style=wx.TE_CENTER, pos=(tmpPos[0][0],tmpPos[0][1]),size=(tmpSize[0][0],tmpSize[0][1]))
		self.ProbabilityName[1] = wx.StaticText(self.leftPanel, wx.ID_ANY, 'Safe', style=wx.TE_CENTER, pos=(tmpPos[1][0],tmpPos[1][1]), size=(tmpSize[1][0],tmpSize[1][1]))
		self.ProbabilityName[2] = wx.StaticText(self.leftPanel, wx.ID_ANY, '~16', style=wx.TE_CENTER, pos=(tmpPos[2][0],tmpPos[2][1]), size=(tmpSize[2][0],tmpSize[2][1]))
		self.ProbabilityName[3] = wx.StaticText(self.leftPanel, wx.ID_ANY, '17~21', style=wx.TE_CENTER, pos=(tmpPos[3][0],tmpPos[3][1]), size=(tmpSize[3][0], tmpSize[3][1]))


		self.PlayerProbability[0] = wx.StaticText(self.leftPanel,wx.ID_ANY, str(tmpProbability[2]), style=wx.TE_CENTER, pos=(tmpPos[0][0],tmpPos[0][1]+20),size=(tmpSize[0][0],tmpSize[0][1]))
		self.PlayerProbability[1] = wx.StaticText(self.leftPanel,wx.ID_ANY, str(100-tmpProbability[2]), style=wx.TE_CENTER, pos=(tmpPos[1][0],tmpPos[1][1]+20),size=(tmpSize[1][0],tmpSize[1][1]))
		self.PlayerProbability[2] = wx.StaticText(self.leftPanel,wx.ID_ANY, str(tmpProbability[1]), style=wx.TE_CENTER, pos=(tmpPos[2][0],tmpPos[2][1]+20),size=(tmpSize[2][0],tmpSize[2][1]))
		self.PlayerProbability[3] = wx.StaticText(self.leftPanel,wx.ID_ANY, str(tmpProbability[0]), style=wx.TE_CENTER, pos=(tmpPos[3][0],tmpPos[3][1]+20),size=(tmpSize[3][0],tmpSize[3][1]))

		
		self.ProbabilityName[0].SetForegroundColour("#FFFFFF")
		self.ProbabilityName[0].SetBackgroundColour("#000000")
		self.ProbabilityName[1].SetForegroundColour("#000000")
		self.ProbabilityName[1].SetBackgroundColour("#FFFFFF")
		self.ProbabilityName[2].SetForegroundColour("#FFFFFF")
		self.ProbabilityName[2].SetBackgroundColour("#000000")
		self.ProbabilityName[3].SetForegroundColour("#000000")
		self.ProbabilityName[3].SetBackgroundColour("#FFFFFF")

		self.PlayerProbability[0].SetForegroundColour("#000000")
		self.PlayerProbability[0].SetBackgroundColour("#FF0000")
		self.PlayerProbability[1].SetForegroundColour("#FFFFFF")
		self.PlayerProbability[1].SetBackgroundColour("#228B22")
		self.PlayerProbability[2].SetForegroundColour("#FFFFFF")
		self.PlayerProbability[2].SetBackgroundColour("#0000CD")
		self.PlayerProbability[3].SetForegroundColour("#000000")
		self.PlayerProbability[3].SetBackgroundColour("#ff8C00")
	



	def InitUI(self):
		
		wx.StaticBox(self.leftPanel, label='deal Card', pos=(0,0),size=(500, 230))
		wx.StaticBox(self.leftPanel, label='Probability', pos=(0,230),size=(500,230))
		wx.StaticBox(self.leftPanel, label='Remaining Card', pos=(0,460),size=(500,150))

		##===deal Card===
	
		tmp=[]
		tmp.append(wx.ToggleButton(self.leftPanel, wx.ID_ANY, 'H', size=(30,20), pos = (0,20)))
		tmp.append(wx.ToggleButton(self.leftPanel, wx.ID_ANY, 'D',size=(30,20), pos = (0,43)))
		tmp.append(wx.ToggleButton(self.leftPanel, wx.ID_ANY, 'S', size=(30,20), pos = (0,66)))
		tmp.append(wx.ToggleButton(self.leftPanel, wx.ID_ANY, 'C', size=(30,20), pos = (0,89)))

		#tButton.append(wx.ToggleButton(rightPanel, wx.ID_ANY, '1', size=(20,20), pos=(20,20)))
		for j in range(4):
			tmp = []
			for i in range(13):
				num = str(i+1)
				tmp.append(wx.ToggleButton(self.leftPanel, wx.ID_ANY, num, size=(30,20), pos=(40+i*31, 20+23*j)))
			self.tButton.append(tmp)

		#deal Button
		delete = wx.Button(self.leftPanel, wx.ID_ANY, 'delete', pos = (10, 120))
		addPlayer = wx.Button(self.leftPanel, wx.ID_ANY, 'add player', pos = (120, 120))
		addDealer = wx.Button(self.leftPanel, wx.ID_ANY, 'add dealer', pos = (230, 120))
		resetDeck = wx.Button(self.leftPanel, wx.ID_ANY, 'reset Decks', pos = (10, 150))
		resetHand = wx.Button(self.leftPanel, wx.ID_ANY, 'reset hand', pos = (120, 150))
		
		delete.Bind(wx.EVT_BUTTON, self.deleteCards)
		addPlayer.Bind(wx.EVT_BUTTON, self.SetPlayerHand)
		resetHand.Bind(wx.EVT_BUTTON, self.resetHand)
		resetDeck.Bind(wx.EVT_BUTTON, self.resetDecks)
		
		
		self.SetSize((450, 700))
		self.Centre()
		self.Show()



		##===Reamining Decks===
		
		numText = []
		remainingData = self.getRemainingCards()
		for i in range(10):
			numText.append(wx.StaticText(self.leftPanel, wx.ID_ANY, str(i+1), pos=(30+10*3*i, 490)))
			self.countText.append(wx.StaticText(self.leftPanel, wx.ID_ANY, str(remainingData[i]), pos=(30+10*3*i, 520)))
		

		
		##===Probability===

		##Player ProbabilityName
		PlayerName = wx.StaticText(self.leftPanel, wx.ID_ANY, "#Player Probability", pos=(10,270))
		self.ProbabilityName[0] = wx.StaticText(self.leftPanel, wx.ID_ANY, 'Burst',style=wx.TE_CENTER, pos=(10,290), size=(200,20))
		self.ProbabilityName[1] = wx.StaticText(self.leftPanel, wx.ID_ANY, 'Safe',style=wx.TE_CENTER,pos=(210,290), size=(200,20))
		self.ProbabilityName[2] = wx.StaticText(self.leftPanel, wx.ID_ANY, '~16',style=wx.TE_CENTER,pos=(210,330), size=(130,20))
		self.ProbabilityName[3] = wx.StaticText(self.leftPanel, wx.ID_ANY, '17~21',style=wx.TE_CENTER,pos=(340,330),size=(70,20))
		
		self.ProbabilityName[0].SetForegroundColour("#FFFFFF")
		self.ProbabilityName[0].SetBackgroundColour("#000000")
		self.ProbabilityName[1].SetForegroundColour("#000000")
		self.ProbabilityName[1].SetBackgroundColour("#FFFFFF")
		
		self.ProbabilityName[2].SetForegroundColour("#FFFFFF")
		self.ProbabilityName[2].SetBackgroundColour("#000000")
		self.ProbabilityName[3].SetForegroundColour("#000000")
		self.ProbabilityName[3].SetBackgroundColour("#FFFFFF")

		##Player Probability Init
		self.PlayerProbability[0] = wx.StaticText(self.leftPanel, wx.ID_ANY, '0', style=wx.TE_CENTER, pos=(10,310), size=(200,20))
		self.PlayerProbability[1] = wx.StaticText(self.leftPanel, wx.ID_ANY, '1', style=wx.TE_CENTER, pos=(210, 310), size=(200,20))
		self.PlayerProbability[2] = wx.StaticText(self.leftPanel, wx.ID_ANY, '2', style=wx.TE_CENTER, pos=(210, 350), size=(130,20))
		self.PlayerProbability[3] = wx.StaticText(self.leftPanel, wx.ID_ANY, '3', style=wx.TE_CENTER, pos=(340,350), size=(70,20))

		#print '#207# PlayerProbability %s' %(len(self.PlayerProbability))
		self.PlayerProbability[0].SetForegroundColour("#000000")
		self.PlayerProbability[0].SetBackgroundColour("#FF0000")

		self.PlayerProbability[1].SetForegroundColour("#FFFFFF")
		self.PlayerProbability[1].SetBackgroundColour("#228B22")

		self.PlayerProbability[2].SetForegroundColour("#FFFFFF")
		self.PlayerProbability[2].SetBackgroundColour("#0000CD")

		self.PlayerProbability[3].SetForegroundColour("#000000")
		self.PlayerProbability[3].SetBackgroundColour("#ff8C00")
	
		
		


import Deck		
import Odds
import Player

decks = Deck.Decks(6)
player = Player.Player()
dealer = Player.Player()

odds = Odds.Odds(decks, player, dealer)

def main():
	ex = wx.App()
	MainFrame(None,decks,player,dealer,odds)
	ex.MainLoop()

if __name__ == '__main__':
	main()
