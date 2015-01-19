from random import random
from math import sqrt

VOID = 0
TRAVELABLE = 1
DEFAULT_LAND_CHANCE = 75

class Grid:
	def __init__(self, width, height, land_chance=DEFAULT_LAND_CHANCE, filename=None):
		self.grid = []
		if filename is None:
			self.grid = [[1 if random() <= land_chance / 100.0 else 0 for col in xrange(width)] for row in xrange(height)]
		else:
			with open(filename) as f:
				for line in f:
					self.grid.append([])
					for c in [c for c in line if c != '\n']:
						if c == '0':
							self.grid[len(self.grid)-1].append(VOID)
						elif c == '.':
							self.grid[len(self.grid)-1].append(TRAVELABLE)
	def __str__(self):
		return_str = ""
		for row in self.grid:
			for spot in row:
				if spot == VOID:
					return_str += '  '
				elif spot == TRAVELABLE:
					return_str += '. '
			return_str += '\n'
		return return_str
	def get_adjacent_spots(self, pos):
		row = pos[0]
		col = pos[1]
		adjacent_spots = []
		if row-1 >= 0 and self.grid[row-1][col] == TRAVELABLE: adjacent_spots.append((row-1, col))
		if col+1 < len(self.grid[0]) and self.grid[row][col+1] == TRAVELABLE: adjacent_spots.append((row, col+1))
		if row+1 < len(self.grid) and self.grid[row+1][col] == TRAVELABLE: adjacent_spots.append((row+1, col))
		if col-1 >= 0 and self.grid[row][col-1] == TRAVELABLE: adjacent_spots.append((row, col-1))
		return adjacent_spots
	def display_path(self, end_node):
		display_str = [[' ' if spot==VOID else '.' for spot in row] for row in self.grid]
		cur_node = end_node
		display_str[cur_node.pos[0]][cur_node.pos[1]] = '+'
		while cur_node.parent is not None:
			cur_node = cur_node.parent
			display_str[cur_node.pos[0]][cur_node.pos[1]] = '+'
		display_str = '\n'.join([' '.join([spot for spot in row]) for row in display_str])
		print display_str
	def get_distance(self, start_pos, end_pos):
		"""Calculates the distance between two points."""
		return sqrt((start_pos[1]-end_pos[1])**2 + (start_pos[0]-end_pos[0])**2)
