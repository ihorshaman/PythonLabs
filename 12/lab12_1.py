#Напишите объявление класса Rectangle (прямоугольник), который является производным от Square (квадрат),
#который, в свою очередь – производный от Shape(фигура). В классе Shape объявите следующие защищенные члены-данные :
#цвет линий фигуры и толщина ее линий  и напишите 2 конструктора - по умолчанию и с параметрами. 
#В классах Square и Rectangle объявите закрытые (защищенные)  члены-данные для хранения размеров каждой из фигур, 
#несколько конструкторов, вызывающих конструкторы базового класса, а также методы для вычисления площади и периметра фигур. 
#В классе Rectangle обязательно используйте перекрывание методов базового класса Square. 
#При необходимости добавьте в классы  методы доступа. Напишите главную программу,
#в которой выполните создание объектов-фигур различных типов и их обработку.

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
			return"Квадрат \n"

		else:
			return "Прямокутник \n"

class Rectauge(Suare):

	def print(self):
		print ("Колір: ")
		print (self.color)
		print ("Товщина ліній: ")
		return self.thickness

	def area(self):
		print ("Площа:")
		return self.length*self.width

	def perimeter(self):
		print ("Периметр:")
		return (self.length*2)+(self.width*2)


a, b = input("Введіть довжину й ширину: ").split()
c = input("Введіть колір: ")
d = input ("Введіть товщину ліній: ")

print ("\n")

r = Rectauge (str(c), int(d), int(a), int(b))

print (r.choice())
print (r.area())
print (r.perimeter())
print (r.print())
