#3.	Измените классы Shape->Square->Rectangle из предыдущего задания на виртуальные.
#Для этого добавьте в класс Shape пустые методы для вычисления площади и периметра и 
#перекройте их виртуальными методами в производных классах. 
#Не забудьте также и про виртуальные деструкторы

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

	def perimeter(self):
		print ("Площа:")
		return self.length*self.width

	def area(self):
		print ("Периметр:")
		return (self.length*2)+(self.width*2)
		

class Suare(Shape):

	def choice(self):
		if self.length == self.width:
			return"Квадрат \n"

		else:
			return "Прямокутник \n"

class Rectauge(Suare):

	def print(self):
		print ("Колір: ")
		print (self.color)
		print ("Товщина ліній: ")
		return self.thickness

	def usesarea(self):
		
		return self.area

	def usesperimert(self):
		return self.perimeter


a, b = input("Введіть довжину й ширину: ").split()
c = input("Введіть колір: ")
d = input ("Введіть товщину ліній: ")

print ("\n")

r = Rectauge (str(c), int(d), int(a), int(b))

print (r.choice())
print (r.area())
print (r.perimeter())
print (r.print())
