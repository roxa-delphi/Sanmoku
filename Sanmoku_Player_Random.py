import random
from Sanmoku_Player import *
from Sanmoku_Board import *

class Sanmoku_Player_Random(Sanmoku_Player) :
	
	def __init__(self, name='') :
		if name == '' :
			self.name = 'Random' + str(Sanmoku_Player.num)
		else :
			self.name = name
		self.number = Sanmoku_Player.num
		Sanmoku_Player.num += 1
		
	def select(self, board:Sanmoku_Board) :
		ava = board.get_available()
		next = random.randrange(len(ava))
		return ava[next]
	
	def post_game(self, board:Sanmoku_Board) :
		pass
	
