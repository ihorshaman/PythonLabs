#Напишите программу для просмотра и редактирования объектов файла, 
#созданного в п.2, в режиме прямого доступа.

name = input("Введите Имя.фамилию.отчество: ")

name2 = (' '.join(name.split(' ')[:-1]))
name3 = (' '.join(name2.split(' ')[:-1]))

surname = (' '.join(name.split(' ')[:-1]))
surname2 = surname[surname.find(" ") + 1 : ]

patronymic = name[name.find(" ") + 1 : ]
patronymic2 = patronymic[patronymic.find(" ") + 1 : ]

print(name3)
print(surname2)
print(patronymic2)

l = [name3, surname2, patronymic2]

a = int(input(": "))

if a == 1:

	File = open('file3.txt', 'a')

	for item in l:

		s = str(item) + " "
		bt = s.encode()
		File.write(bt)

	File.close();

elif a == 2:
	L2 = []

	File = open('file3.txt', 'r')

	for ln in File:

		x = str(ln) 
		L2 = L2 + [x] 

	print("L2 =", L2)

	File.close();

elif a == 0:

	File = open('file3.txt', 'w')

	File.write("")

	File.close()
