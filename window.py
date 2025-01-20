from tkinter import Tk, BOTH, Canvas

class Window():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.title = "Maze Solver"
		self.__root = Tk()
		self.__root.title(self.title)
		self.canvas = Canvas(self.__root, width=self.width, height=self.height)
		self.canvas.pack(fill=BOTH)
		self.running = False
		self.__root.protocol("WM_DELETE_WINDOW", self.close)

	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()

	def wait_for_close(self):
		self.running = True
		while self.running:
			self.redraw()

	def close(self):
		self.running = False

	def draw_line(self, line, color):
		line.draw(self.canvas, color)