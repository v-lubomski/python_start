x = 'from global'
def funcOuter():
	nonlocal x
	print('to funcOuter', x) 
	x = 'from funcOuter'

	def funcInner():
		nonlocal x
		print('to funcInner', x)
		x = 'from funcInner'

		def funcDNO():
			nonlocal x
                	print('to funcDNO', x)
                	x = 'from funcDNO'

#проверить работу функций внутри функций
