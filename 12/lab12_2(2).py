#Напишите объявления для следующих диаграмм классов, включив в него члены-данные,
#конструкторы по умолчанию и с параметрами ,
#методы доступа, методы ввода-вывода для клавиатуры и экрана и т.д. :
#Транспорт : номер, год выпуска, марка:
#Автомобиль : максимальная скорость
#Автобус : число посадочных мест

class Transport:

	def set(self, number, date, mark):
		self._protected_member = number
		self._protected_member = date
		self._protected_member = mark


	def __init__(self, number, date, mark):
		self.number = number
		self.date = date
		self.mark = mark

	def print(self):
		print("\n")
		print ("Номер:", self.number)
		print ("Год выпуска: ", self.date)
		print ("Марка: ")
		return self.mark


class Car(Transport):

	def set(self, speed):
		self._protected_member = speed

	def __init__(self, sp):
		self.speed = sp

	def print1(self):
		print("Максимальная скорость: ")
		return (str(self.speed) +  " км/час")

class Bus(Transport):

	def set(self, seats):
		self._protected_member = seats

	def __init__(self, st):
		self.seats = st

	def print2(self):
		print("Число посадочных мест: ")
		return self.seats

a = int(input ("Номер: "))
b = int(input ("Год выпуска: "))
c = str(input ("Марка: "))
d = int(input ("Если машина = 1, если автобус = 0: "))

Tr = Transport(a, b, c)

if int(d) == 1:

	x = int(input ("Максимальная скорость: "))
	print (Tr.print())
	Cr = Car(x)
	print (Cr.print1())

else:
	y = int(input ("Число посадочных мест: "))
	print (Tr.print())
	Bs = Bus(y)
	print (Bs.print2())
