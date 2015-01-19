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
		self.past_nodes = set()
		self.frontier = Queue.Queue()
		self.frontier.put(Node(start_pos))
	def do_next(self):
		if self.frontier.empty(): return False
		cur_node = self.frontier.get()
		if cur_node.pos == self.end_pos: return cur_node
		for pos in self.grid.get_adjacent_spots(cur_node.pos):
			if pos not in self.past_nodes:
				self.past_nodes.add(pos)
				self.frontier.put(Node(pos, cur_node))
		return 1
