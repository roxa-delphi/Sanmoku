import random
from Sanmoku_Player import *
from Sanmoku_Board import *

class Sanmoku_Player_QL1(Sanmoku_Player) :
	
	def __init__(self, name='', e=0.2, alpha=0.3) :
		if name == '' :
			self.name = 'QL1_' + str(Sanmoku_Player.num)
		else :
			self.name = name
		self.number = Sanmoku_Player.num
		Sanmoku_Player.num += 1
		self.history = []
		self.q     = {}
		self.e     = e
		self.alpha = alpha
		self.gamma = 0.9
		
	def select(self, board:Sanmoku_Board) :
		
		cur_board = board.board.copy()
		ava       = board.get_available()
		
		#print('turn=%d' %(board.turn))
		if random.random() < (self.e/(board.turn//10000+1)):
			i=random.randrange(len(ava))
			self.history.append([board.board.copy(), ava[i]])
			return ava[i]
			
		qs = [self.getQ(tuple(cur_board),p) for p in ava]
		maxQ= max(qs)
		print('qs=%s' %qs)

		if qs.count(maxQ) > 1:
			best_options = [i for i in range(len(ava)) if qs[i] == maxQ]
			i = random.choice(best_options)
		else:
			i = qs.index(maxQ)
			
		self.history.append([board.board.copy(), ava[i]])
		return ava[i]

	
	def getQ(self, state, act) :
		if self.q.get((state, act)) is None:
			self.q[(state, act)]= 1
		return self.q.get((state, act))

	def post_game(self, board:Sanmoku_Board) :
		
		if board.status == Sanmoku_Board.status_draw :
			print('%s draw' %(self.name))
		elif board.status == self.number :
			print('%s win' %(self.name))
		else :
			print('%s lose' %(self.name))
			
		
		print('%s history %s' %(self.name, self.history))
		
		#self.learn(self.last_board,self.last_move, 0, board)
		
		self.history = []
	
	def learn(self,s,a,r,fs):
		pQ=self.getQ(tuple(s.board),a)
		if fs.winner is not None:
			maxQnew=0
		else:
			maxQnew=max([self.getQ(tuple(fs.board),act) for act in fs.get_possible_pos()])
			self.q[(tuple(s.board),a)]=pQ+self.alpha*((r+self.gamma*maxQnew)-pQ)

