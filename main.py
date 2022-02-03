import os
import sys

os.chdir(sys.path[0])
sys.path.insert(1, "P://Python Projects/assets/")

from GUI import *


allShapes = []


cellSize = 26


class Cell:
	def __init__(self, pos, size, color):
		self.pos = pos
		self.size = size
		self.backgroundColor = color
		self.borderColor = black
		self.rect = pg.Rect(self.pos[0], self.pos[1], self.size, self.size)

	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, self.rect)
		DrawRectOutline(self.borderColor, self.rect)


class Grid:
	def __init__(self, rect, size):
		self.rect = pg.Rect(rect)
		self.size = size

		self.CreateGrid()

	def CreateGrid(self):
		self.grid = [[Cell(self.GetPosFromIndex(x, y), self.size, lightBlack) for x in range(self.rect.w // self.size)] for y in range(self.rect.h // self.size)]

	def Draw(self):
		DrawRectOutline(black, (self.rect.x - 1, self.rect.y - 1, self.rect.w - (self.rect.w % self.size) + 2, self.rect.h - (self.rect.h % self.size) + 2))

		for row in self.grid:
			for cell in row:
				cell.Draw()

	def GetPosFromIndex(self, i, j):
		return self.rect.x + (i * self.size), self.rect.y + (j * self.size)

	def GetIndexFromPos(self, x, y):
		return (x - self.rect.x) // self.size, (y - self.rect.y) // self.size


# change how each sub cube is create for each shape maybe make new class
class Cube(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)

	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y + self.size, self.rect.w, self.rect.h))


class Line(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)
	
	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size * 3, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size * 3, self.rect.w, self.rect.h))


class RightL(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)
	
	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y + self.size * 2, self.rect.w, self.rect.h))


class LeftL(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)
	
	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x - self.size, self.rect.y + self.size * 2, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x - self.size, self.rect.y + self.size * 2, self.rect.w, self.rect.h))


class T(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)
	
	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size * 2, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size * 2, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y + self.size, self.rect.w, self.rect.h))


class LeftZ(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)
	
	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size * 2, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size * 2, self.rect.y + self.size, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y + self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y + self.size, self.rect.w, self.rect.h))


class RightZ(Cell):
	def __init__(self, pos, size):
		super().__init__(pos, size, color=shapeColors[type(self)])

		AddToListOrDict([allShapes], self)
	
	def Draw(self):
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size, self.rect.y - self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size, self.rect.y - self.size, self.rect.w, self.rect.h))
		pg.draw.rect(screen, self.backgroundColor, (self.rect.x + self.size * 2, self.rect.y - self.size, self.rect.w, self.rect.h))
		DrawRectOutline(self.borderColor, (self.rect.x + self.size * 2, self.rect.y - self.size, self.rect.w, self.rect.h))


shapeColors = {
	Cube: yellow,
	Line: lightBlue,
	LeftL: pink,
	RightL: orange,
	T: lightRed,
	LeftZ: green,
	RightZ: magenta,
	}


Cube((10, 10), cellSize)
Line((10, 80), cellSize)
RightL((10, 200), cellSize)
LeftL((110, 200), cellSize)
T((10, 300), cellSize)
LeftZ((110, 380), cellSize)
RightZ((10, 406), cellSize)

gridSize = [300, 700]
g = Grid((width // 2 - (gridSize[0] // 2) + cellSize // 2, height // 2 - (gridSize[1] // 2) + cellSize // 2, gridSize[0], gridSize[1]), cellSize)



def DrawLoop():
	screen.fill(darkGray)

	DrawAllGUIObjects()

	g.Draw()

	for shape in allShapes:
		shape.Draw()

	pg.display.update()


def HandleEvents(event):
	HandleGui(event)


def Update():
	pass

while running:
	clock.tick_busy_loop(fps)
	deltaTime = clock.get_time()
	for event in pg.event.get():
		if event.type == pg.QUIT:
			running = False
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_ESCAPE:
				running = False

		HandleEvents(event)

	Update()

	DrawLoop()
