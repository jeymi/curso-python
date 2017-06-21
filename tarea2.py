import random
lista=[]
for l in range(0,4):
	n= random.randrange(0,100)
	lista.insert(0,n)

for x in range(len(lista)):
	print("numeros generados")
	print(lista[x])
	print("primero y segindo numero")
	print(lista[0,4])






