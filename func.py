import math

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
