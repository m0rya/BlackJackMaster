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

		self.ProbabilityName = []
		self.PlayerProbability = []
		self.DealerProbability = []
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

		remainingData = self.getRemainingCards()
		for i in range(10):
			self.countText[i].SetLabel(str(remainingData[i]))
			
		#reload probability 
		self.PlayerProbability = self.odds.calcBurstPlayer()
	

		print '#delete done'



	def InitUI(self):
		#frame = wx.Frame(None, wx.ID_ANY, 'testFrame', size=(1200, 700))

		leftPanel = wx.Panel(self,  pos = (0,0), size=(500,500))
		rightPanel = wx.Panel(self, pos = (500,0), size= (500,500))

		wx.StaticBox(rightPanel, label = 'deal Card', pos=(0,0), size=(500,250))
		wx.StaticBox(rightPanel, label = 'Remaining Card', pos=(0,250), size=(500,250))

		wx.StaticBox(leftPanel, label = 'Hand', pos=(0,0), size=(500,250))
		wx.StaticBox(leftPanel, label ='Probability', pos=(0,250), size=(500,250))

		##===deal Card===
		tmp = []
		tmp.append(wx.ToggleButton(rightPanel, wx.ID_ANY, 'H', size=(30,20), pos = (0,20)))
		tmp.append(wx.ToggleButton(rightPanel, wx.ID_ANY, 'D',size=(30,20), pos = (0,43)))
		tmp.append(wx.ToggleButton(rightPanel, wx.ID_ANY, 'S', size=(30,20), pos = (0,66)))
		tmp.append(wx.ToggleButton(rightPanel, wx.ID_ANY, 'C', size=(30,20), pos = (0,89)))

		#tButton.append(wx.ToggleButton(rightPanel, wx.ID_ANY, '1', size=(20,20), pos=(20,20)))
		for j in range(4):
			tmp = []
			for i in range(13):
				num = str(i+1)
				tmp.append(wx.ToggleButton(rightPanel, wx.ID_ANY, num, size=(30,20), pos=(40+i*31, 20+23*j)))
			self.tButton.append(tmp)

		layout = wx.BoxSizer(wx.HORIZONTAL)
		rightPanel.SetSizer(layout)

		#deal Button
		delete = wx.Button(rightPanel, wx.ID_ANY, 'delete', pos = (10, 120))
		addPlayer = wx.Button(rightPanel, wx.ID_ANY, 'add player', pos = (120, 120))
		addDealer = wx.Button(rightPanel, wx.ID_ANY, 'add dealer', pos = (230, 120))
		resetDeck = wx.Button(rightPanel, wx.ID_ANY, 'reset Decks', pos = (10, 150))
		resetHand = wx.Button(rightPanel, wx.ID_ANY, 'reset hand', pos = (120, 150))
		
		delete.Bind(wx.EVT_BUTTON, self.deleteCards)
			
		
		self.SetSize((1200, 700))
		self.Centre()
		self.Show()



		##===Reamining Decks===
		
		numText = []
		remainingData = self.getRemainingCards()
		for i in range(10):
			numText.append(wx.StaticText(rightPanel, wx.ID_ANY, str(i+1), pos=(30+10*3*i, 270)))
			self.countText.append(wx.StaticText(rightPanel, wx.ID_ANY, str(remainingData[i]), pos=(30+10*3*i, 300)))
		

		
		##===Probability===
		PlayerName = wx.StaticText(leftPanel, wx.ID_ANY, "#Player Probability", pos=(10,270))
		self.ProbabilityName.append(wx.StaticText(leftPanel, wx.ID_ANY, 'Burst',style=wx.TE_CENTER, pos=(10,290), size=(200,20)))
		self.ProbabilityName.append(wx.StaticText(leftPanel, wx.ID_ANY, 'Safe',style=wx.TE_CENTER,pos=(210,290), size=(200,20)))
		self.ProbabilityName.append(wx.StaticText(leftPanel, wx.ID_ANY, '~16',style=wx.TE_CENTER,pos=(210,340), size=(130,20)))
		self.ProbabilityName.append(wx.StaticText(leftPanel, wx.ID_ANY, '17~21',style=wx.TE_CENTER,pos=(340,340),size=(70,20)))
		
		self.ProbabilityName[0].SetForegroundColour("#FFFFFF")
		self.ProbabilityName[0].SetBackgroundColour("#000000")
		self.ProbabilityName[1].SetForegroundColour("#000000")
		self.ProbabilityName[1].SetBackgroundColour("#FFFFFF")
		
		self.ProbabilityName[2].SetForegroundColour("#FFFFFF")
		self.ProbabilityName[2].SetBackgroundColour("#000000")
		self.ProbabilityName[3].SetForegroundColour("#000000")
		self.ProbabilityName[3].SetBackgroundColour("#FFFFFF")
		


		tmpProbability = self.odds.calcBurstPlayer()
		print tmpProbability
		'''
		for i in range(len(tmpProbability)):
			
			self.PlayerProbability.append(wx.StaticText(leftPanel, wx.ID_ANY, str(tmpProbability[i]), pos=(
		'''
	'''	
	def SetProbability(self):
		tmpProbability = self.odds.calcBurstPlayer()
		self.ProbabilityName[0] = wx.StaticText(leftPanel, wx.ID_ANY, 'Burst', style=wx.TE_CENTER, pos=(10,290),size=(tmpProbability[2]*400,30))
		self.ProbabilityName[1] = wx.StaticText(leftPanel, wx.ID_ANY, 'Safe', style=wx.TE_CENTER, pos=(10+tmpProbability[2]*400,290), size=((100-tmpProbability[2])*400,30))
		self.ProbabilityName[2] = wx.StaticText(leftPanel, wx.ID_ANY, '~16', style=wx.TE_CENTER, pos=(
	'''
			

import Deck		
import Odds
import Player

decks = Deck.Decks(4)
player = Player.Player()
dealer = Player.Player()

odds = Odds.Odds(decks, player, dealer)

def main():
	ex = wx.App()
	MainFrame(None,decks,player,dealer,odds)
	ex.MainLoop()

if __name__ == '__main__':
	main()
