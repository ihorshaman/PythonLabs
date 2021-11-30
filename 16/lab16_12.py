#Напишите программу, создающую в цикле несколько 
#объектов этого класса в стеке (свободной памяти). 
#Запишите эти объекты последовательно в 
#двоичный файл, пользуясь методами класса.

class Person:

	def set(self, name, age, salary):

		self._protected_member = name
		self._protected_member = age
		self._protected_member = salary


	def __init__(self, name, age, salary):

		self.name = name
		self.age = age
		self.salary = salary

	def print(self):

		return (self.name, self.age, self.salary)

	def write(self):

		l = [self.name, self.age, self.salary]

		File = open('File2.bin', 'ab')

		for item in l:

			s = str(item) + " "
			bt = s.encode()
			File.write(bt)

		y = "\n"
		yt = y.encode()
		File.write(yt)
		File.close();


x = int(input(": "))

l = []

for i in range(x):

	print("№", i+1)
	name = input("name: ")
	age = input("age: ")
	salary = int(input("salary: "))

	pr1 = Person(name, age, salary)

	pr1.write()

if (x == 0):
	File = open('File2.bin', 'wb')

	y = "\n"
	yt = y.encode()
	File.write(yt)

	File.close();
