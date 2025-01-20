from point import Point

class Cell():
	def __init__(self, has_left_wall, has_right_wall, has_top_wall, has_bottom_wall, x1, y1, x2, y2, win):
		self.has_left_wall = has_left_wall
		self.has_right_wall = has_right_wall
		self.has_top_wall = has_top_wall
		self.has_bottom_wall = has_bottom_wall
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.win = win

	def draw(self):
		if self.has_left_wall:
			self.win.draw_line(Point(self.x1, self.y1, self.x1, self.y2), "black")
		if self.has_right_wall:
			self.win.draw_line(Point(self.x2, self.y1, self.x2, self.y2), "black")
		if self.has_top_wall:
			self.win.draw_line(Point(self.x1, self.y1, self.x2, self.y1), "black")
		if self.has_bottom_wall:
			self.win.draw_line(Point(self.x1, self.y2, self.x2, self.y2), "black")