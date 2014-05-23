
siSoyCuadroMagico= [[2,7,6],
					[9,5,1],
					[4,3,8]]

noSoyCuadroMagico= [[1,2,3],
					[2,3,1],
					[1,3,2]]

def verCruz(ma,x,y,fin,suma,cont):
	if cont < fin:
		suma += ma[x][y]
		return verCruz(ma,x+1,y+1,fin,suma,cont+1)
	else:
		return suma 

def verCruzInv(ma,x,y,fin,suma,cont):
	if cont < fin:
		suma += ma[x][y]
		return verCruzInv(ma,x+1,y-1,fin,suma,cont+1)
	else:
		return suma 

def verEnX(ma,x,y,fin,suma):
	if x < fin:
		suma += ma[x][y]
		return verEnX(ma,x+1,y,fin,suma)
	else:
		return suma 

def verEnY(ma,x,y,fin,suma):
	if y < fin:
		suma += ma[x][y]
		return verEnY(ma,x,y+1,fin,suma)
	else:
		return suma 

def cuadroMagico(ma,x,y,suma,fin,aux):
	ver_inv = verCruzInv(siSoyCuadroMagico,0,fin-1,fin,0,0)
	ver_cruz = verCruz(siSoyCuadroMagico,0,0,fin,0,0)
	if ver_cruz == ver_inv:
		return cuadroMagico_aux(ma,0,0,ver_inv,fin,0)
	else:
		return False

def cuadroMagico_aux(ma,x,y,suma,fin,aux):  
	if y < fin:
		sumx = verEnX(ma,0,y,fin,0)
		if suma == sumx:
			return cuadroMagico_aux(ma,x,y+1,suma,fin,aux)
		else:
			return False
	elif x < fin:
		sumy = verEnY(ma,x,0,fin,0)
		if sumy == suma:
			return cuadroMagico_aux(ma,x+1,y,suma,fin,aux)
		else:
			return False
	return True

tamano = len(noSoyCuadroMagico)
tamano1 = len(siSoyCuadroMagico)
print("False->",cuadroMagico(noSoyCuadroMagico,0,0,0,tamano,0))
print("True->",cuadroMagico(siSoyCuadroMagico,0,0,0,tamano1,0))


''' 
print(verEnX(siSoyCuadroMagico,1,1,tamano,0))
print(verEnY(siSoyCuadroMagico,0,0,tamano,0))
print(verCruz(siSoyCuadroMagico,0,0,tamano,0,0))
print(verCruzInv(siSoyCuadroMagico,0,tamano-1,tamano,0,0))
'''


