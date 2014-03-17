######################################
# Imprime diamante segun dimension n #
# Por Kenneth Callow, ITCR           #
######################################

def linea(n,x):
    if(x==0):
        print(' '*n+'*')
    else:
        print(' '*(n-x)+'*'+' '*(x-1)+'*'+' '*(x-1)+'*')

def diamante(n):
    for x in range(0,n):
        linea(n,x)
    print('*'*(2*n+1))
    for x in range(0,n):
        linea(n,n-x-1)
