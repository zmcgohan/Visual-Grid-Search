from grid import Grid
from path_finders import GridSearchFinder
from node import Node

if __name__ == '__main__':
	my_grid = Grid(10, 10)
	print my_grid
	grid_search_finder = GridSearchFinder(my_grid, (1, 1), (5, 5))
	last_find = grid_search_finder.do_next()
	while last_find == 1:
		last_find = grid_search_finder.do_next()
	if last_find:
		my_grid.display_path(last_find)
	else:
		print "Could not find path."
