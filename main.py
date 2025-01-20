from window import Window
from cell import Cell

win = Window(800, 600)

cells = []

for i in range(10):
	for j in range(10):
		cells.append(Cell(True, True, True, True, i * 80, j * 60, (i + 1) * 80, (j + 1) * 60, win))

for cell in cells:
	cell.draw()

win.wait_for_close()