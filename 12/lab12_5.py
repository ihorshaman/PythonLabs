class Shape:

	def set(self, color, thickness, length, width):
		self._protected_member = color
		self._protected_member = thickness
		self._protected_member = length
		self._protected_member = width

	def __init__(self, c, th, l, w):
		self.color = c
		self.thickness = th
		self.length = l
		self.width = w	

class Suare(Shape):

	def choice(self):
		if self.length == self.width:
			return"Квадрат"

		else:
			return "Прямокутник "

class Rectauge(Suare):

	def print(self):
		return "Колір: " + self.color

	def print1(self):
		return "Товщина ліній: " + str(self.thickness)

	def area(self):
		return "Площа:" + str(self.length*self.width)

	def perimeter(self):
		return "Периметр:" + str((self.length*2)+(self.width*2))


a, b = input("Введіть довжину й ширину: ").split()
c = input("Ведіть колір: ")
d = input ("Введіть товщину ліній: ")

print ("\n")

r = Rectauge (str(c), int(d), int(a), int(b))

a = r.choice()
s = r.area()
p = r.perimeter()
b = r.print()
c = r.print1()

Shape1 = [a, s, p, b, c]

print (Shape1)

Shqpe1 = []
