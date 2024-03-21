import math

class Vector:
	def __init__(self,x,y):
		self.x = x
		self.y = y
	def add(self,v):
		self.x += v.x
		self.y += v.y
	def sub(self,v):
		self.x -= v.x
		self.y -= v.y
	def dot(self,v):
		return self.x*v.x + self.y*v.y
	def mult(self,s):
		self.x *= s
		self.y *= s
	def div(self,s):
		if s == 0:
			return 0
		self.x /= s
		self.y /= s
	def mag(self):
		return math.sqrt(self.x*self.x + self.y*self.y)
	def setmag(self,m):
		self.div(self.mag())
		self.mult(m)
	def angle(self):
		return math.atan2(self.y,self.x)

class Complex:
	def __init__(self,r,i):
		self.r = r
		self.i = i
	def add(self,c):
		return Complex(self.r+c.r , self.i+c.i)
	def sub(self,c):
		return Complex(self.r-c.r , self.i-c.i)
	def mults(self,s):
		return Complex(self.r*s , self.i*s)
	def divs(self,s):
		if s == 0:
			return 0
		return Complex(self.r/s , self.i/s)
	def mult(self,c):
		return Complex(self.r*c.r - self.i*c.i , self.r*c.i + self.i*c.r)
	def div(self,c):
		a = c.mod()
		if a == 0:
			return 0
		return Complex((self.r*c.r + self.i*c.i)/a , (self.i*c.r - self.r*c.i)/a)
	def mod(self):
		return math.sqrt(self.r*self.r + self.i*self.i)
	def conjugate(self):
		return Complex(self.r,-self.i)
	def arg(self):
		return math.atan2(self.i,self.r)
	def copy(self):
		return Complex(self.r,self.i)
