#1615.py
#python 1615.py
#Напишите программу, которая выводит аргументы командной 
#строки в обратном порядке и не выводит имя программы.

import sys

print("Hello")

for i in reversed(sys.argv[ 1:]):
	print(i)
