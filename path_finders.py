import Queue
from node import Node

class PathFinder(object):
	def __init__(self, grid, start_pos, end_pos):
		self.grid = grid
		self.start_pos = start_pos
		self.end_pos = end_pos

class GridSearchFinder(PathFinder):
	def __init__(self, grid, start_pos, end_pos):
		super(GridSearchFinder, self).__init__(grid, start_pos, end_pos)
		self.past_nodes = []
		self.frontier = Queue.Queue()
		self.frontier.put(Node(start_pos))
	def do_next(self):
		if self.frontier.empty(): return False
		cur_node = self.frontier.get()
		if cur_node.pos == self.end_pos: return cur_node
		for pos in self.grid.get_adjacent_spots(cur_node.pos):
			if pos not in self.past_nodes:
				self.past_nodes.append(pos)
				self.frontier.put(Node(pos, cur_node))
		return 1
	def get_frontier_positions(self):
		frontier_positions = []
		for i in xrange(self.frontier.qsize()):
			node = self.frontier.get()
			frontier_positions.append(node.pos)
			self.frontier.put(node)
		return frontier_positions

class AStarSearchFinder(PathFinder):
	def __init__(self, grid, start_pos, end_pos):
		super(AStarSearchFinder, self).__init__(grid, start_pos, end_pos)
		self.past_nodes = []
		self.frontier = []
		self.frontier.append(Node(start_pos))
	def do_next(self):
		if len(self.frontier) == 0: return False
		cur_node = self.frontier[0]
		lowest_distance = self.grid.get_distance(self.frontier[0].pos, self.end_pos)
		for node in self.frontier:
			cur_dist = self.grid.get_distance(node.pos, self.end_pos)
			if cur_dist < lowest_distance:
				lowest_distance = cur_dist
				cur_node = node
		for node in xrange(len(self.frontier)):
			if cur_node == self.frontier[node]:
				del self.frontier[node]
				break
		if cur_node.pos == self.end_pos: return cur_node
		for pos in self.grid.get_adjacent_spots(cur_node.pos):
			if pos not in self.past_nodes:
				self.past_nodes.append(pos)
				self.frontier.append(Node(pos, cur_node))
		return 1
	def get_frontier_positions(self):
		return [node.pos for node in self.frontier]
