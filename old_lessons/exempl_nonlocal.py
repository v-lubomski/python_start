def funcOuter(): #Уровень вложенности - 1
	x = 333 #Переменная у1

	def funcInner(): #Уровень вложенности - 2
		nonlocal x #Теперь переназначить  переменную у2 получится, так как переменная у1
			   #больше не ссылается на у0
		x = 666 #Переменная у2

		def funcDNO():
			nonlocal x
			x = 777

		funcDNO()

	funcInner()
	print(x)

funcOuter()
