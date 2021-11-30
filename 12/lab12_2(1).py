#Напишите объявления для следующих диаграмм классов, включив в него члены-данные,
#конструкторы по умолчанию и с параметрами ,
#методы доступа, методы ввода-вывода для клавиатуры и экрана и т.д. :
#Студент : номер,  фамилия, пол --> Заочник : место работы, должность

class Student:

	def set(self, number, sex, surname):
		self._protected_member = number
		self._protected_member = sex
		self._protected_member = surname


	def __init__(self, number, sex, surname):
		self.number = number
		self.sex = sex
		self.surname = surname

	def print(self):
		print("\n")
		print ("Номер:", self.number)
		if self.sex == 1:
			print ("Пол: мужской")		
		else:
			print ("Пол: женский")
		print ("Фамилия:")
		return self.surname


class extraStudent(Student):

	def set(self, position, job):
		self._protected_member = position
		self._protected_member = job

	def __init__(self, position, job):
		self.position = position
		self.job = job

	def print1(self):
		print("Место работы: ")
		print(self.position)
		print("Должность: ")
		return self.job

a = input ("Номер: ")
b = input ("Фамилия: ")
c = input ("Пол (1 если мужской, 0 если женский): ")
d = input ("Заочник?: 1 если да, 0 если нет: ")

if int(d) == 1:
	x = input ("Место работы: ")
	y = input ("Должность: ")

	st = Student(int(a), int(c), str(b))
	ex = extraStudent(str(x), str(y))

	print (st.print())
	print (ex.print1())

else:
	st = Student(int(a), int(c), str(b))
	print (st.print())
