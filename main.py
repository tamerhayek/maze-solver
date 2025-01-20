from window import Window
from point import Point

win = Window(800, 600)

win.draw_line(Point(100, 200, 200, 200), "red")
win.draw_line(Point(200, 200, 200, 100), "red")
win.draw_line(Point(200, 100, 100, 100), "red")
win.draw_line(Point(100, 100, 100, 200), "red")

win.wait_for_close()