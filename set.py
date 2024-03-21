import pygame
import func
import time

pygame.init()
screen = pygame.display.set_mode((700,700))
screen.fill(0)

class Arey:
	def __init__(self,w,h):
		self.w = w
		self.h = h
		self.data = []
		temp = []
		for i in range(self.h):
			temp.append(0)
		for i in range(self.w):
			self.data.append(temp.copy())

val = Arey(700,700)
iteration = Arey(700,700)
c = func.Complex(0,0)
gen = [0]
n = 20

for i in range(700):
	for j in range(700):
		val.data[i][j] = c.copy()

start = time.perf_counter()

for i in range(n):
	img = "{}.png".format(i+1)
	screen.fill(0)
	for x in range(700):
		for y in range(700):
			if iteration.data[x][y] == 0:
				val.data[x][y] = val.data[x][y].mult(val.data[x][y])
				val.data[x][y] = val.data[x][y].add(func.Complex((x-350)/175,(y-350)/175))

			if val.data[x][y].mod() >= 2:
				if iteration.data[x][y] == 0:
					iteration.data[x][y] = i

			c = iteration.data[x][y]*(255/n)
			pygame.draw.rect(screen,(c,c,c),(x,y,1,1))

	pygame.image.save(screen, img)

end = time.perf_counter()

print(end-start)
