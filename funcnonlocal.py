x = 50
def funcOuter():
	x = 2
	print('x equal', x)

	def funcInner():
		x = 5

	funcInner()
	print('local x now is', x)

funcOuter()
