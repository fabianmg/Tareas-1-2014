'''
funcion que retorna una tira con un "diamante" de orden n
'''

def trianguloy(a,c,d,s): # parte de abajo 
	if a == d:
		return ""
	if c == 1:	# reglon final
		print " "*d,"+"*c
		return trianguloy(a+1,c-2,d,s)
	else:   
		print " "+" "*a,""+"+"+ " "*s + "+" + " "*s + "+" 
		# se disminuye en 1 es espacio que hay entre los 3 "+" 
	return trianguloy(a+1,c-2,d,s-1)

def triangulox(a,c,d,s):    # parte de abajo 
	if a <= 0:
		print " "*a, "+"*(d*2+1)  # el medio del diamante 
		return trianguloy(a,c-2,d,s-1)
	if c == 1 or c == 3:	# reglon 1 o 2 ? 
		print " "*a,"+"*c
		return triangulox(a-1,c+2,d,s)
	else:   
		print " "*a,""+"+"+ " "*s + "+" + " "*s + "+"
		# se aumenta en 1 es espacio que hay entre los 3 "+" 
	return triangulox(a-1,c+2,d,s+1)

a = int(input("Digite un numero: "))
print(triangulox(a,1,a,1))
print "OK."

'''
Nota p: dejarlo en una sola funcion 
'''
