# tarea 3, rev 0.1

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
	if len(vect) == 0:
		return True
	elif vect[0] == 0:
		return vectorNull(vect[1:])
	else:
		return False

'''
print ('Si es nulo: (true) ', vectorNull(soyVectorNull)) 
print ('No es nulo: (false) ', vectorNull(noSoyVectorNull)) 
'''

def vectoresIguales(vect1,vect2,a):
	if len(vect1) == a:  
		return True
	elif vect1[a] ==  vect2[a]:
		return vectoresIguales(vect1,vect2,a+1)
	else:
		return False
'''
if vectoresIguales(VectorA,VectorB,0):
	print ("Los vectores son iguales")
else:
	print ("Los vectores No son iguales")	
'''

def sumaVectores(vect1,vect2,a,vectZ):  # como se hace recursividad con cola
	if len(vect1) == a:  				# y que el code queda bonito
		return vectZ
	else:
		vectZ[a] = vect1[a]+vect2[a]
		return sumaVectores(vect1,vect2,a+1,vectZ)

#print (sumaVectores(VectorA,VectorC,0,VectorA))

def restaVectores(vect1,vect2,a,vectZ):  
	if len(vect1) == a:  				
		return vectZ
	else:
		vectZ[a] = vect1[a]-vect2[a]
		return restaVectores(vect1,vect2,a+1,vectZ)

#print (restaVectores(VectorA,VectorC,0,VectorA))


def producEscalar(vect1,e):
	if len(vect1) == 0:  				
		return []
	else:
		return [vect1[0]*e] + producEscalar(vect1[1:],e)

# escalar = int(input('Ingrese el numero escalar: '))
# print ('El produc escalar es: ', producEscalar(VectorA,escalar))



def producVector(vect1,vect2):
	if len(vect1) == 0:  				
		return  0
	else:
		return (vect1[0]*vect2[0]) + producVector(vect1[1:],vect2[1:])

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
