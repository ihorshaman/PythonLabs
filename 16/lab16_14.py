#Введите ФИО, возраст, вес одной строкой в символьный массив 
#и  затем в программе получите отдельные переменные и выведите их на экран.
#Используйте классы внутреннего ввода-вывода языка С++.

name = input("Введите Имя.фамилию.отчество.возраст.вес: ")

l = name.split()

for line in l:

	print(line)
