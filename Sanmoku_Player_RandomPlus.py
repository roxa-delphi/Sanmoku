import random
from Sanmoku_Player import *
from Sanmoku_Board import *

class Sanmoku_Player_RandomPlus(Sanmoku_Player) :
	
	def __init__(self, name='') :
		if name == '' :
			self.name = 'RP' + str(Sanmoku_Player.num)
		else :
			self.name = name
		self.number = Sanmoku_Player.num
		Sanmoku_Player.num += 1
		self.history = []
		
		
	def select(self, board:Sanmoku_Board) :
		next = board.win_pos(self.number)
		if next != -1 :
			self.history.append([board.board.copy(), next])
			return next
		
		next = board.lose_pos(self.number)
		if next != -1 :
			self.history.append([board.board.copy(), next])
			return next
			
		ava = board.get_available()
		next = random.randrange(len(ava))
		self.history.append([board.board.copy(), ava[next]])
		return ava[next]

	def post_game(self, board:Sanmoku_Board) :
		#print('%s history %s' %(self.name, self.history))
		
		self.history = []
	
