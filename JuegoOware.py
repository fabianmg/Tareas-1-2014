# -*- coding: utf-8 -*-  
'''	 oware
 para windows :@
 alternativa 1  (idea 1, con 2 listas para cada jugador)
 open(nombre del archivo,modo)
'''
import os
import random 

#     0 1 2 3 4 5 6 -->
j2 = [4,4,4,4,4,4,0] # Esta sera la lista del jugador dos, 
j1 = [4,4,4,4,4,4,0] # jugador 1 
#     0 1 2 3 4 5 6 --> en el campo 6 se guardaran los puntos de los jugadores

'''
j2 = d.d('i',[4,4,4,4,4,4,0]) # jugador 2
j1 = d.d('i',[4,4,4,4,4,4,0]) # jugador 1
'''
movidas = 0 	# lleva la cuenta de movidas o jugadas 
x = 0 			# x almacena, en la funcion base(x,y) la eleccion del jugador 1 
y = 0 			# y almacena, en la funcion base(x,y) la eleccion del jugador 2 
				# se alamacena para llamar a la funcion convBases para el jugador 1
				# y convBasesy para el jugador 2. y convertir la base deseada por el jugador
				# su eleccion se guarada en x,y.  

j2aux = []		# estas dos listas (auxiliares) se usan para guardar las listas correspondientes al
j1aux = []		# jugador uno y dos. Convertidas a las bases anteriormente seleccionadas
'''
def Guardar(j1,j2,movidas):
	fileg= open('./owaa.txt')
	fileg.write(j1,'\n',j2,'\n',movidas)
	fileg.close() '''

def mapa(movidas,j1aux,j2aux): 	# esta funcion es la encargada de imprimir 'el tablero del juego'
    #Guardar(j1,j2,movidas)		# lo imprime con las lista (auxliares).
    #os.system('clear')
    ###os.system('cls')
    print("                        Oware")
    print("       ┌------------------┐   ┌------------------┐")
    print("       |Jugador 1 %3d     |   |  Jugador 2 %3d   |" %(j1[6], j2[6]))
    print("       └------------------┘   └------------------┘")
    print("Movida: ", movidas )   # numero de movidas en el juego...
    print("	  6        5       4      3        2       1 ")	
    print("	┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐")
    print("	| ",j2aux[5]," ",j2aux[4],"  ",j2aux[3],"  ",j2aux[2],"  ",j2aux[1],"  ",j2aux[0])
    print("	└-----┘ └-----┘ └-----┘ └-----┘ └-----┘ └-----┘")
    print("	┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐")
    print("	| ",j1aux[0],"  ",j1aux[1],"  ",j1aux[2],"  ",j1aux[3],"  ",j1aux[4]," ",j1aux[5])
    print("	└-----┘ └-----┘ └-----┘ └-----┘ └-----┘ └-----┘")
    print("	    1       2      3       4       5       6")
    return " " 

def error(lugar): # si comete el mismo error muchas veces seguidas --->BSOD<---
	os.system('cls')
	os.system('color 1f')
	if not isinstance(lugar,int):

		print("	Se ha encontrado un problema y Windows ha sido apagado para evitar daños al equipo")
		print("	El probema parece estar originado por el siguiente archivo: Progra Oware. type(Oware) = USB ")
		print("	Ah ingresado un caracter no valido, por favor ingrese solo numeros")
		print("	Si esta es la primera vez que ve esta pantalla de error de detención, reinicie su equipo. ") 
		print("	Si los problemas continúan, deshabilite o elimine cualquier hardware o software de capa 8.") 
		print(" Deshabilite las opciones de memoria de la BIOS como caché o vigilancia. ")
		print(" Si necesita utilizar el modo a prueba de errores para quitar o deshabilitar componentes, ")
		print("	reinicie su equipo, presione F8 para seleccionar opciones de inicio avanzadas y, a continuación,")
		print(" seleccione Modo a prueba de errores.")
		print(" ")
		print("		  6        5       4      3        2       1 ")	
		print("		┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐")
		print("		| %3d | | %3d | | %3d | | %3d | | %3d | | %3d |" %(j2[5], j2[4], j2[3], j2[2], j2[1], j2[0]))
		print("		└-----┘ └-----┘ └-----┘ └-----┘ └-----┘ └-----┘")
		print("		┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐ ┌-----┐")
		print("		| %3d | | %3d | | %3d | | %3d | | %3d | | %3d |" %(j1[0], j1[1], j1[2], j1[3], j1[4], j1[5]))
		print("		└-----┘ └-----┘ └-----┘ └-----┘ └-----┘ └-----┘")
		print("		    1       2      3       4       5       6")
		print(" Eliga una posicion valida!!! ")
		lugar = input("Posicion: " )
		return error(lugar)
	else:
		return lugar
			
def finjuego(vect):	# funcion para comprabar si un jugador (las lista j1 o 2j)
					# se quedo sin semillas
	'''
		Un vector nulo es aquel en que todos sus elementos son igual a cero 
		funcion para saber si un jugador se queda sin semillas!
	'''
	if len(vect) == 0: 	# cuando el tamaño del vector es 0, retorna true 
		return True
	elif vect[0] == 0:	# si la cabeza del vector es = a 0 
		return finjuego(vect[1:]) 	# retorna la misma funcion (recursiva) con la cola del vector
	else:				# en caso de que la cabeza no sea 0 
		return False 		# retorna false 

def ganador(x):  		# comprueba si hay ganador  
	os.system('clear')	# se limpia la terminal o el 'cmd'
	if j1[6]>24:	
		print("El jugador 1 es el ganador, con ",j1[6]," semillas.")
		return False
	if j2[6]>24:	
		print("El jugador 2 es el ganador, con ",j2[6]," semillas.?")
		return False
	if finjuego(j1[:-1]) and x == 1:
		print(mapa(movidas+1,j1aux,j2aux))
		if j1[6]>j2[6]:
			print("El jugador 1 es el ganador, con ",j1[6]," semillas.")
			return False
		else:
			print("El jugador 2 es el ganador, con ",j2[6]," semillas.?")
			return False
	elif finjuego(j2[:-1]) and x == 2:
		print(mapa(movidas+1,j1aux,j2aux))
		if j1[6]>j2[6]:
			print("El jugador 1 es el ganador, con ",j1[6]," semillas.")
			return False
		else:
			print("El jugador 2 es el ganador, con ",j2[6]," semillas.?")
			return False
	else:
		return True

def validarLugar(lugar,jugador):
	if jugador[lugar] != 0:
		return True
	else:
		return False
''''''
def mismoJugador(vect1,vect2,a):  # a se utiliza como contador // cp de tareas pasadas 
	if len(vect2) == a:  # cuando |a| tiene el mismo valor que 
		return True 		# el tamaño del vector retorna el True
	elif vect1[a] ==  vect2[a]:		# sii las posiciones |a| de ambos vectores son iguales
		return mismoJugador(vect1,vect2,a+1)		# retorna la misma funcion con (a+1)
	else:				# en caso de que posiciones |a| de ambos vectores no son iguales
		return False 
''''''
def puntos(lugar,jugador,ptsGanados):
	if jugador[lugar] == 3 or jugador[lugar] == 2:
		print('lugar--->',lugar,"-->",jugador)
		ptsGanados[6] = ptsGanados[6]+jugador[lugar]
		jugador[lugar] = 0
		#if jugador[lugar-1] == 3 or jugador[lugar-1] == 2:
		#	ptsGanados[6] = ptsGanados[6]+ jugador[lugar-1]
		#	jugador[lugar] = 0
	if jugador[lugar-1] == 3 or jugador[lugar-1] == 2:
		print('lugar--->',lugar-2,"-->",jugador)
		return puntos(lugar-1,jugador,ptsGanados)
	return " "

def mover1(lugar,semillas,jugador,x,actual):
	if x == 0:   				# x es 0 solo la primera vez que entra a la func
		jugador[lugar] = 0 		# si x es 0 el lugar elegido por el jugador se pondra en 0(semillas) 
		#x = 1 					# para luego continuar con las distribucion de semillas
	if semillas == 0:					# cuando semillas es 0. Es por que se repartieron todas (al contrario de) 
										# de las agujas del reloj
		if mismoJugador(actual,j1,1):#si el jugador acutal es el uno (j1) 
			puntos(lugar,j2,j1) 	 #comprueba si gana puntos o no, llamando a la funcion putos   
		else:							# y se le asignaran al j1, si es que los gana
			puntos(lugar,j1,j2) 	# puntos para el jugador 2
		return True 		# me saca de la funcio. Retornando True 
	elif lugar < 5: 
		lugar += 1 	
		jugador[lugar] += 1  			
		semillas -= 1
		#print(semillas)
		return  mover1(lugar,semillas,jugador,1,actual)
	elif mismoJugador(jugador,j1,1):
		return mover1(-1,semillas,j2,1,actual)
	else: 
		return mover1(-1,semillas,j1,1,actual)

def noHaySemillas(semillas,jugador,lugar)	:
	#mapa($movidas)
	if semillas == 0:
		print("	,__, Eliga una ")
		print("	(oo)____  posicion con semillas: ")
		print("	(__)    )\ ")
		print("	   ||''|| * ")
		lugar = int(input("posicion: " ))
		return noHaySemillas(jugador[lugar-1],jugador,lugar)
	else:
		return lugar

'''''converciones'''''''''
def toBin(n):
    if n == 0:
        return str(0)
    if n//2==0:
        return str(1)
    else:
        return str(toBin(n//2))+str(n%2)

def toOctal(n):
    if n == 0:
        return str(0)    
    if n//8==0:
        return str(n%8)
    else:
        return str(toOctal(n//8))+str(n%8)  

def toHex(n):
    if   n%16==10:
        return  str(toHex(n//16))+ 'A' 
    elif n%16==11:
        return  str(toHex(n//16))+ 'B' 
    elif n%16==12:
        return  str(toHex(n//16))+ 'C'
    elif n%16==13:
        return  str(toHex(n//16))+ 'D'
    elif n%16==14:
        return  str(toHex(n//16))+ 'E'
    elif n%16==15:
        return  str(toHex(n//16))+ 'F'
    elif n//16==0:
        return str(n%16)
    else:
        return str(toHex(n//16))+str(n%16)

def hexa(arreglo):
    if arreglo == []:
        return []
    else:
        return ['0x'+(toHex(arreglo[0]))] + hexa(arreglo[1:])

def bina(arreglo):
    if arreglo == []:
        return []
    else:
        return ['0b'+(toBin(arreglo[0]))] + bina(arreglo[1:])

def octal(arreglo):
    if arreglo == []:
        return []
    else:
        return ['0o'+(toOctal(arreglo[0]))] + octal(arreglo[1:])

'''
print(hexa([1,2,3,4,999]))
print(bina([1,2,3,4,255]))
print(octal([1,2,3,4,255]))
'''
'''''converciones''''end'''

def validarNum(lugar):
	print("	,__, Digite solo ")
	print("	(oo)____  :   numeros ")
	print("	(__)    )\ ")
	print("	   ||''|| * ")
	lugar  = input("Eliga una la posicion a mover: ")
	if not lugar.isdigit():
			lugar = validarNum(lugar)
	return lugar 

def convBases(x,y,j1aux,j2aux):
	if x == 1:
		j1aux = bina(j1[0:6])
	elif x == 2:
		j1aux = octal(j1[0:6])
	elif x == 3:
		j1aux = hexa(j1[0:6])
	return j1aux

def convBasesy(x,y,j1aux,j2aux):
	if y == 1:
		j2aux = bina(j2[0:6])
	elif y == 2:
		j2aux = octal(j2[0:6])
	elif y == 3:
		j2aux = hexa(j2[0:6])
	return j2aux

def Juego(j1,j2,movidas,j1aux,j2aux,x,y,z):
	#x = 1
	#os.system('COLOR 2a')

	if z == 1:
		if ganador(1):  # true, no hay ganador 
			j1aux = convBases(x,y,j1aux,j2aux)
			j2aux = convBasesy(x,y,j1aux,j2aux)
			print('1  ',j1aux,'j2   ',j2aux)
			#movida +=1
			print(mapa(movidas,j1aux,j2aux)) # imprime el mapa y las mov,j1aux,j2auxidas aumentan en 1
			print("Jugador 1 eliga  la posicion a mover")
			
			lugar = input("Posicion:  ")
			
			if not lugar.isdigit():
				lugar = validarNum(lugar)
			lugar = int(lugar)

			if j1[lugar-1] == 0:
				lugar = noHaySemillas(j1[lugar-1],j1,lugar)
				
			mover1(lugar-1,j1[lugar-1],j1,0,j1)
		
		else:
			return True
		z = 2
	if z==2:
		if ganador(2):	 # true, no hay ganador 	
			#os.system('COLOR 21')
			movidas += 1
			#j1aux = j1[0:6]
			#j2aux = j2[0:6]

			j1aux = convBases(x,y,j1aux,j2aux)
			j2aux = convBasesy(x,y,j1aux,j2aux)
			print(mapa(movidas,j1aux,j2aux)) # imprime el mapa y las movidas aumentan en 1
			print("Jugador 2 eliga  la posicion a mover ")
			
			lugar = input("Posicion:  ")

			if not lugar.isdigit():
				lugar = validarNum(lugar)
			lugar = int(lugar)

			if j2[lugar-1] == 0:
				lugar = noHaySemillas(j2[lugar-1],j2,lugar)	
			mover1(lugar-1,j2[lugar-1],j2,0,j2)
			return Juego(j1,j2,movidas+1,j1aux,j2aux,x,y,1)
		else:	
			return True

def bases(x,y):
        print('		bla bla bla bla bla bla bla bla 	')
        print('1. Base predefinida para todo el tablero. ')
        print('2. Base definida por jugador(Al azar)')
        x = int(input('Eliga una opcion: '))
        if x == 1:
                print('		Bases:')
                print('1. Binario.')
                print('2. Octal.')
                print('3. Hexadecimal')
                x = int(input('Jugador uno eliga una opcion: '))
                print('		Bases:')
                print('1. Binario.')
                print('2. Octal.')
                print('3. Hexadecimal')
                y = int(input('Jugador dos eliga una opcion: '))
        elif x == 2:
                x = random.randint(1,4) 
                y = random.randint(1,4)
        else:
                print('eliga una pocision valida: ')
                base(x,y)
        quienJuega = random.randint(1,2)   
        Juego(j1,j2,movidas,j1aux,j2aux,x,y,quienJuega)


bases(x,y)



'''
error color  1f
cont = 25
while cont != 0:
	print(" ")
	cont = cont-1
fondo letra
 0 = Negro       8 = Gris
 1 = Azul        9 = Azul claro
 2 = Verde       A = Verde claro
 3 = Aguamarina  B = Aguamarina claro
 4 = Rojo        C = Rojo claro
 5 = Púrpura     D = Púrpura claro
 6 = Amarillo    E = Amarillo claro
 7 = Blanco      F = Blanco brillante
'''
# -*- coding: utf-8 -*-  
'''	 oware
 para windows :@
 alternativa 1  (idea 1, con 2 listas para cada jugador)
 open(nombre del archivo,modo)
'''
