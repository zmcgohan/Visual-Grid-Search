class Node:
	def __init__(self, pos, parent=None):
		self.parent = parent
		self.pos = pos
		self.cost = parent.cost + 1 if parent is not None else 0
	def __str__(self):
		node_str = "({}, {})".format(*self.pos)
		cur_node = self
		while cur_node.parent is not None:
			node_str += "->({}, {})".format(*cur_node.parent.pos)
			cur_node = cur_node.parent
		return node_str
