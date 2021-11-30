#Напишите программу, предлагающую пользователю ввести  с к
#лавиатуры его фамилию, имя и отчество как единое целое, 
#а затем выводящую их на экран.

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
