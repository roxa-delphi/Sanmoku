

class Sanmoku_Board :
	
	board_empty = 0
	board_player1 = 1
	board_player2 = 2
	status_ongame = 0
	status_win_1 = 1
	status_win_2 = 2
	status_draw  = 3
	Mark = [' ', 'O', 'X']
	chk_win_pos = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
	
	def __init__(self, player1 = 'Player1', player2 = 'Player2', start_player = 1) :
		self.board = []
		for i in range(9) :
			self.board.append(Sanmoku_Board.board_empty)
		
		self.player_name = [None, player1, player2]	
		self.active_player = start_player
		self.status = Sanmoku_Board.status_ongame
		self.turn = 1
			
	def new_game(self, player1 = 'Player1', player2 = 'Player2', start_player = 1) :
		self.__init__(player1, player2, start_player)
	
	def display_board(self) :
		print(' -----')
		for y in range(3) :
			print(" %s %s %s" %(Sanmoku_Board.Mark[self.board[y*3]], Sanmoku_Board.Mark[self.board[y*3+1]], Sanmoku_Board.Mark[self.board[y*3+2]]))
	
	def set_board(self, pos, display = True) :
		if self.status != Sanmoku_Board.status_ongame :
			return
		
		if self.board[pos] != Sanmoku_Board.board_empty :
			if self.active_player == Sanmoku_Board.board_player1 :
				self.status = Sanmoku_Board.status_win_2
			else :
			  self.status = Sanmoku_Board.status_win_1
			return
		
		self.board[pos] = self.active_player
		self.check_win()
		
		if display : print('Turn=%d Player=%s pos=%s Status=%s' %(self.turn, self.player_name[self.active_player], pos, self.status))
		
		self.active_player += 1
		if self.active_player == 3 : 
			self.active_player = 1
		
		self.turn += 1
		return
	
	def check_win(self) :
		for lpos in Sanmoku_Board.chk_win_pos :
			if self.board[lpos[0]] != Sanmoku_Board.board_empty :
				if self.board[lpos[0]] == self.board[lpos[1]] and self.board[lpos[0]] == self.board[lpos[2]] :
					self.status = self.board[lpos[0]]
					return 
	
		if len(self.get_available()) == 0 :
			self.status = Sanmoku_Board.status_draw
	
	def get_available(self) :
		ret = []
		for i in range(9) :
			if self.board[i] == Sanmoku_Board.board_empty :
				ret.append(i)
		return ret
	
	def win_pos(self, player) :
		for lpos in Sanmoku_Board.chk_win_pos :
			v = 0
			n = -1
			for pos in lpos :
				if self.board[pos] == player :
					v += 1
				elif self.board[pos] == Sanmoku_Board.board_empty :
					n = pos
			if v == 2 and n != -1:
				#print('..chance %d' %(n))
				return n
		
		return -1
	
	def lose_pos(self, player) :
		cplayer = player + 1
		if cplayer == 3 : cplayer = 1
		return self.win_pos(cplayer)
		
		
if __name__ == "__main__":
	b = Sanmoku_Board()
	
	b.set_board(5)
	b.display_board()
	
	b.set_board(4)
	b.display_board()
	
	b.set_board(2)
	b.display_board()
	
	b.set_board(1)
	b.display_board()
	
	b.set_board(8)
	b.display_board()
	
	
	b.new_game()
	b.set_board(0)
	b.set_board(2)
	b.set_board(1)
	b.set_board(3)
	b.set_board(4)
	b.set_board(8)
	b.set_board(6)
	b.set_board(7)
	b.set_board(5)
	b.display_board()
