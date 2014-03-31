#PALINDROMO##v0.0############################

def cont(num):
	if num == 0:
		return 0
	else:
		return 1 + cont(num//10)

def pal(num,c):
	if c == 0:
		return 0
	else:
		return (num%10)*(10**(c-1)) + pal(num//10,c-1)

def pali(a):
	if a == pal(a,cont(a)):
		return 'es PALINDROMO'
	else:
		return 'No es PALINDROMO'

print (pali(int(input("Digite un numero: "))))
