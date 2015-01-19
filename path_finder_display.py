import pygame as pg

class PathFinderDisplay:
	def __init__(self, surface, path_finder):
		self.surface = surface
		self.path_finder = path_finder
		self.create_spots()
	def create_spots(self):
		self.spots = []
		spot_width = self.surface.get_width() / len(self.path_finder.grid.grid[0])
		spot_height = self.surface.get_height() / len(self.path_finder.grid.grid)
		for i in xrange(len(self.path_finder.grid.grid)):
			temp = []
			for j in xrange(len(self.path_finder.grid.grid[0])):
				temp_rect = pg.Rect(spot_width * len(temp), spot_height * len(self.spots), spot_width, spot_height)
				temp.append(temp_rect)
			self.spots.append(temp)
	def display_path(self, start_node):
		cur_node = start_node
		pg.draw.rect(self.surface, (0,200,0), self.spots[cur_node.pos[0]][cur_node.pos[1]])
		while cur_node.parent is not None:
			cur_node = cur_node.parent
			pg.draw.rect(self.surface, (0,255,0), self.spots[cur_node.pos[0]][cur_node.pos[1]])
		pg.draw.rect(self.surface, (0,200,0), self.spots[cur_node.pos[0]][cur_node.pos[1]])
		pg.display.flip()
	def update(self):
		for row in xrange(len(self.path_finder.grid.grid)):
			for col in xrange(len(self.path_finder.grid.grid[row])):
				color = (255,255,255) if self.path_finder.grid.grid[row][col] == 1 else (0,0,0)
				pg.draw.rect(self.surface, color, self.spots[row][col])
		for node in self.path_finder.past_nodes:
			pg.draw.rect(self.surface, (150,255,255), self.spots[node[0]][node[1]])
		for pos in self.path_finder.get_frontier_positions():
			pg.draw.rect(self.surface, (255,150,255), self.spots[pos[0]][pos[1]])
		pg.draw.rect(self.surface, (200,0,0), self.spots[self.path_finder.start_pos[0]][self.path_finder.start_pos[1]])
		pg.draw.rect(self.surface, (200,0,0), self.spots[self.path_finder.end_pos[0]][self.path_finder.end_pos[1]])
		pg.display.flip()
