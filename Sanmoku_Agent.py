import random
from Sanmoku_Board import *
from Sanmoku_Player import *
from Sanmoku_Player_Random import *
from Sanmoku_Player_RandomPlus import *

class Sanmoku_Agent :
	
	def __init__(self, p1:Sanmoku_Player, p2:Sanmoku_Player) :
		self.player = [None, p1, p2]
		self.board = Sanmoku_Board()

		self.nwin = [0, 0, 0, 0]
		
	
	def game_start(self, nplay, disp=False) :
		
		for i in range(nplay) :
			
			player = random.randrange(2)+1
			self.board.new_game(player1=self.player[1].name, player2=self.player[2].name, start_player=player)
			
			while self.board.status == Sanmoku_Board.status_ongame :
				pos = self.player[player].select(self.board)
				#print('ava=%s npos=%d' %(ava, ava[npos]))
				self.board.set_board(pos, disp)
		
				if disp : self.board.display_board()
				
				player += 1
				if player == 3 : player = 1
		
			self.nwin[self.board.status] += 1
			print('Game=%d %s=%d %s=%d Draw=%d' %(i, self.player[1].name, self.nwin[1],self.player[2].name , self.nwin[2], self.nwin[3]))
			
			self.player[1].post_game(self.board)
			self.player[2].post_game(self.board)


if __name__ == "__main__":
	
	p1 = Sanmoku_Player_RandomPlus()
	print('%s : %d' %(p1.name, p1.number))
	p2 = Sanmoku_Player_RandomPlus()
	print('%s : %d' %(p2.name, p2.number))
	
	a = Sanmoku_Agent(p1, p2)
	a.game_start(1, True)
	#a.game_start(1000, False)