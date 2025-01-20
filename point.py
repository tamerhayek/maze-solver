class Point():
	def __init__(self, x1, y1, x2, y2):
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2

	def draw(self, canvas, color):
		canvas.create_line(self._x1, self._y1, self._x2, self._y2, fill=color, width=2)