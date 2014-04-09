'''
Fabian Monge - tarea 3 - ITCR 
'''

import array;

'''
  - es_vector
  - vector_nulo
  - vectores_iguales
  - suma_vectores
  - resta_vectores
  - producto_escalar
  - producto_vectores
'''

soyVector = array.array('i',[1,2,3])
noSoyVector = 'no es vector'
soyVectorNull = array.array('i',[0,0,0,0])
noSoyVectorNull = array.array('i',[1,0,5,0])
VectorA = array.array('i',[1,2,3])
VectorB = array.array('i',[1,2,3])
VectorC = array.array('i',[4,5,6])



def esVector(vect):  
	# funcion para saber si vect es un vector
	if not isinstance(vect, array.array):
		return False
	else:
		return True 
'''
if esVector(noSoyVector):    # prueba la funcion de esVector, caso false
	print ("Si es un vector")
else:
	print ("No es un vector")

if esVector(soyVector):    # prueba la funcion de esVector, caso true 
	print ("Si es un vector")
else:
	print ("No es un vector")
'''



def vectorNull(vect):
	'''
		Un vector nulo es aquel en que todos sus elementos son igual a cero 
		funcion para saber si un Vector es nulo o no!
	'''
	if len(vect) == 0: 	# cuando el tamaño del vector es 0, retorna true 
		return True
	elif vect[0] == 0:	# si la cabeza del vector en = a 0 
		return vectorNull(vect[1:]) 	# retorna la misma funcion (recursiva) con la cola del vector
	else:				# en caso de que la cabeza no sea 0 
		return False 		# retorna false 


print ('Caso vector null: ')

if vectorNull(soyVectorNull):   # pruebas funcion vectorNull  
	print ('El vector es nulo')
else:
	print('El vector no es nulo')

print ('Caso vector no es null: ')

if vectorNull(noSoyVectorNull):
	print ('El vector es nulo')
else:
	print('El vector no es nulo')




def vectoresIguales(vect1,vect2,a):  # a se utiliza como contador 
	'''
		Dos vectores son iguales si tienen los
		mismos elementos en la misma posición
	'''
	if len(vect1) == a:  # cuando |a| tiene el mismo valor que 
		return True 		# el tamaño del vector retorna el True
	elif vect1[a] ==  vect2[a]:		# sii las posiciones |a| de ambos vectores son iguales
		return vectoresIguales(vect1,vect2,a+1)		# retorna la misma funcion con (a+1)
	else:				# en caso de que posiciones |a| de ambos vectores no son iguales
		return False 		# retorna false xq no se cumple la igualdad

'''  prueba de la funcion vectoresIguales 
if vectoresIguales(VectorA,VectorB,0):
	print ("Los vectores son iguales")
else:
	print ("Los vectores No son iguales")	
'''

def sumaVectores(vect1,vect2,a,vectZ):  # Profe!! como se hace recursividad con cola
	if len(vect1) == a:  				# y que el codigo queda bonito?? :(
		return vectZ
	else:
		vectZ[a] = vect1[a]+vect2[a]   # suma los vectores 1 y 2 en el vector Z
		return sumaVectores(vect1,vect2,a+1,vectZ)		

#print (sumaVectores(VectorA,VectorC,0,VectorA))

def restaVectores(vect1,vect2,a,vectZ):  
	if len(vect1) == a:  	# |a| es para saber cuando ya resto todos los valores de un vector
		return vectZ
	else:
		vectZ[a] = vect1[a]-vect2[a]
		return restaVectores(vect1,vect2,a+1,vectZ)

#print (restaVectores(VectorA,VectorC,0,VectorA))


def producEscalar(vect1,e):  
	'''
	Multiplicar todos los elementos de 1 vector por 1 número (escalar)
	e = escalar
	V = [ v0, v1, v2, ..., vn-1 ]
	V * e = [ v0 * e, v1 * e, v2 * e ..., vn-1 * e]
	'''
	if len(vect1) == 0:  				
		return []
	else:
		return [vect1[0]*e] + producEscalar(vect1[1:],e) 
	#	se multiplica la cabeza por e 
		#	y se suma la funcion recursica (con la cola de vetor)

# escalar = int(input('Ingrese el numero escalar: '))	# pide o lee un numero que se cuarda
														# en la variable escalar
# print ('El produc escalar es: ', producEscalar(VectorA,escalar))
					# imprime el resulatado de producEscalar



def producVector(vect1,vect2):
	'''
	La multiplicación de vectores produce un único número como resultado
	V = [ v0, v1, v2, ..., vn-1 ]
	W = [ w0, w1, w2, ..., wn-1 ]
	V * W = Σ vi * wi (desde i =0, hasta n - 1)
	V * W = v0 * w0 + v1 * w1 + v2 * w2 + ... + vn-1 * wn-1
	'''
	if len(vect1) == 0:  				
		return  0
	else:
		return (vect1[0]*vect2[0]) + producVector(vect1[1:],vect2[1:])
		# retorna la  multiplicacion la la cabeza de ambos vecores  y lo suma (concatena) a la
			# misa funcion recursiva 

#print ('El produc vector es: ', producVector(VectorA,VectorC))



'''
  ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
╋╋┏━━━┓╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
╋╋┃┏━━┛╋╋╋╋┃┃╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
╋╋┃┗━━┓┏━━┓┃┗━┓┏┓┏━━┓┏━━┓╋╋╋
╋╋┃┏━━┛┃┏┓┃┃┏┓┃┣┫┃┏┓┃┃┏┓┃╋╋╋
╋╋┃┃╋╋╋┃┏┓┃┃┗┛┃┃┃┃┏┓┃┃┃┃┃╋╋╋
╋╋┗┛╋╋╋┗┛┗┛┗━━┛┗┛┗┛┗┛┗┛┗┛╋╋╋
  ╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋╋
'''
