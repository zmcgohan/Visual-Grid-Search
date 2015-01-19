from grid import Grid
from path_finders import GridSearchFinder, AStarSearchFinder
from node import Node
from path_finder_display import PathFinderDisplay
import pygame as pg
import sys
from time import sleep

WINDOW_SIZE = (750,750)

if __name__ == '__main__':
	my_grid = Grid(100,100,75)
	grid_search_finder = AStarSearchFinder(my_grid, (0, 0), (99,99))
	window = pg.display.set_mode(WINDOW_SIZE)
	path_display = PathFinderDisplay(window, grid_search_finder)
	currently_finding = True
	steps_taken = 0
	while 1:
		for event in pg.event.get():
			if event.type == pg.QUIT: sys.exit(0)
		if currently_finding:
			steps_taken += 1
			last_find = grid_search_finder.do_next()
			path_display.update()
		if last_find != 1 and steps_taken > 0:
			currently_finding = False
			print "Steps taken: {}".format(steps_taken)
			steps_taken = 0
			if last_find:
				path_display.display_path(last_find)
			else:
				print "No path found"
		sleep(.005)
