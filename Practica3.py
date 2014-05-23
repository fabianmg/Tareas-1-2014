'''
Práctica de Ordenamientos, Vectores y Matrices.
'''



no=[[2,7,6],
	[9,5,1],
	[4,3,8]]


si=[[2,0,0],
	[9,5,0],
	[4,3,3]]

sii= [	[2,0,0,0],
		[9,5,0,0],
		[4,3,3,0],
		[4,3,1,1]]

sii2= [	[2,1,2,5],
		[0,5,5,6],
		[0,0,3,1],
		[0,0,0,2]]

noo= 	[[2,0,0,0],
		[9,5,0,5],
		[4,3,3,0],
		[4,3,0,0]]
#http://tutorias.co/wp-content/uploads/2013/04/crearMatrizTriangularInferiorPython.jpg


def matriz_tri(ma,ini,fin,x,y,conty):
	'''
	matriz1 triangular 
	'''
	if y <= fin:
		if y >= conty:
			if ma[x][y] != 0:
				#print ("hola! no es triangular 1")
				return matriz_tri_aux(ma,ini,fin,0,0,0)	
		return matriz_tri(ma,ini,fin,x,y+1,conty)	
	elif x < fin:
		return matriz_tri(ma,ini,fin,x+1,0,conty+1)	
	else:
		print ("hola! es triangular inferior superior. ")
		return True 

def matriz_tri_aux(ma,ini,fin,x,y,conty):
	if y <= fin:
		if y < conty:
			if ma[x][y] != 0:
				print ("hola! no es triangular. ")
				return False
		return matriz_tri_aux(ma,ini,fin,x,y+1,conty)	
	elif x < fin:
		return matriz_tri_aux(ma,ini,fin,x+1,0,conty+1)	
	else:
		print ("hola! es triangular superior.")
		return True 

#matriz_tri(sii2,0,len(sii2)-1,0,0,1)


'''
tranpuesta de una matriz	
	[	[1,2],		[	[1,3,5],			
		[3,4],			[2,4,6]		]
		[5,6] ]
'''

matriz1 = [	[1,2],	#  [[1,3,5],
			[3,4],	#	[2,4,6]]
			[5,6] ]

  
def transpuesta(ma,trans,transAux,x,y,fin,finy):
		if x < fin:
			trans += [ma[x][y]]	
			return transpuesta(ma,trans,transAux,x+1,y,fin,finy)
		elif y < finy:
			transAux += [trans]
			return transpuesta(ma,[],transAux,0,y+1,fin,finy)
		else:
			return transAux + [trans]

#print(transpuesta(matriz1,[],[],0,0,len(matriz1),len(matriz1[0])-1))







######################

# Búsqueda  secuencial en lista
def busqueda_secuencial(lista, elem):
	return busqueda_secuencial_aux(lista, elem, 0, len(lista))

def busqueda_secuencial_aux(lista, elem, indice, largo):
	if indice == largo:
		return -1
	elif lista[indice] == elem:
		return indice
	else:
		return busqueda_secuencial_aux(lista, elem, indice+1, largo)

# Búsqueda  binaria en lista
def busqueda_binaria(lista, elem):
	return busqueda_binaria_aux(lista, elem, 0, len(lista))

def busqueda_binaria_aux(lista, elem, inicial, final):
	if final < inicial or inicial == len(lista):
		return -1
	mitad = (inicial + final) // 2
	if lista[mitad] == elem:
		return mitad
	elif lista[mitad] > elem:
		return busqueda_binaria_aux(lista, elem, inicial, mitad - 1)
	else:
		return busqueda_binaria_aux(lista, elem, mitad + 1, final)

print(busqueda_binaria([1,2,5,8,6,4],2))

lista_desorden = [22,5,13,9,-8,7,8,-6,15,-4,4,8,4,3,2,1,0,21]


# Ordenamiento: Burbuja

def burbu(lista,ini,fin,swap):
	if ini < fin:
		if lista[ini] > lista[ini+1]:
			temp = lista[ini]
			lista[ini] = lista[ini+1]
			lista[ini+1] = temp
			swap = True
		return burbu(lista,ini+1,fin,swap)
	elif swap == True:
		return burbu(lista,0,fin,False)
	else:
		return lista


#lista_desorden = [12,5,-1,4,3,2,1,0,-5]
#print(burbu(lista_desorden,0,len(lista_desorden)-1,False))


# Ordenamiento: seleccion

def seleccion(lista,indice,ini,fin,menor):
	if ini < fin:
		if lista[menor] > lista[ini+1]:
			menor = ini+1
		return seleccion(lista,indice,ini+1,fin,menor)
	elif lista[menor] <= lista[indice] and indice < fin:
		temp = lista[menor]
		lista[menor] = lista[indice]
		lista[indice] = temp
		indice +=1
		return seleccion(lista,indice,indice,fin,indice)
	return lista

#print(seleccion(lista_desorden,0,0,len(lista_desorden)-1,0))


# Ordenamiento:	quicksort

def quicksort(lista):
	if len(lista) == 1 or len(lista) == 0:
		return lista
	part = partir(lista)
	print(part)
	return quicksort(part[2]) + part[1] + quicksort(part[0])

def partir(lista):
	return partir_aux(lista,lista[0],0,len(lista),[],[],[])

def partir_aux(lista,pivote,ini,fin,may,igu,men):
	if ini == fin:
		return may,igu,men
	elif lista[ini] > pivote:
		may += [lista[ini]]
		return partir_aux(lista,pivote,ini+1,fin,may,igu,men)
	elif lista[ini] == pivote:
		igu += [lista[ini]]
		return partir_aux(lista,pivote,ini+1,fin,may,igu,men)
	else:
		men += [lista[ini]]
		return partir_aux(lista,pivote,ini+1,fin,may,igu,men)

# print("quicksort ",quicksort(lista_desorden))



def unirListas(lista1,lista2,ini1,fin1,ini2,fin2,union):
	if ini1 < fin1:
		if not lista1[ini1] in union:
			union += [lista1[ini1]]
		return  unirListas(lista1,lista2,ini1+1,fin1,ini2,fin2,union)

	elif ini2 < fin2:
		if not lista2[ini2] in lista1:
			if not lista2[ini2] in union:	
				union += [lista2[ini2]]
		return unirListas(lista1,lista2,ini1,fin1,ini2+1,fin2,union)
	return union

list_uno = [3,8,8,5,7]
list_dos = [4,2,5,6,7,2,3,4]
#print(unirListas(list_uno,list_dos,0,len(list_uno),0,len(list_dos),[]))

