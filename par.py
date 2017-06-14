import random
mi_list=[]
for limite in range(0,20):
	n = random.randrange(0,100)
	mi_list.insert(0,n)


for x in range(len(mi_list)):
		print(mi_list[x])

print ('lista ordenada')
for m in range(len(mi_list)):
	if (mi_list[m])%2 ==0:
		mi_list.sort()
		print(mi_list[m])

for s in range(len(mi_list)):
	if (mi_list[s])%2 !=0:
		mi_list.sort()
		print(mi_list[s])
	