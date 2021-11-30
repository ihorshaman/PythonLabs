#5.	Напишите программу, предлагающую пользователю ввести его фамилию, 
#имя и отчество , а затем выводящую эти сведения в текстовый файл.

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
patronymic =input("Введите очество: ")

l = [name, surname, patronymic]

File = open('file.txt', 'w')

for index in l:

	File.write(index + '\n')

File.close()
