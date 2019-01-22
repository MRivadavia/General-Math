
#import math
""""Formula de Baskara"""

def baskara(a,b,c):
    x_1=(-b+(b**2-4*a*c)**(1/2))/2*a
    x_2=(-b-(b**2-4*a*c)**(1/2))/2*a
    print('Os valores das raízes da equação são:',x_1,'e',x_2)
    return

print("Encontrando as raízes reais de uma equação de segundo grau")
print()
a=int(input('Entre com o valor de a:'))
print()
b=int(input('Entre com o valor de b:'))
print()
c=int(input('Entre com o valor de c:'))

baskara(a,b,c)
