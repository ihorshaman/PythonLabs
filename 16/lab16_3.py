#Напишите программу, выполняющую различные вычисления и  
#выводящую  значений с применение методов форматирования, 
#манипуляторов и флагов объекта cout.

x = int(input("x: "))
y = int(input("y: "))

z = x * y

product = ('Добуток: {}'.format(z))

print(product)
print(product.lower())
print(product.upper())
print(product.title())
