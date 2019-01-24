#!/usr/bin/env python3

""""Programa para testar a primalidade de um número se é primo ou não."""

#Definição de número primo: um número é primo quando o resto da divisão dele por ele mesmo e por um for zero
#Pela definição acima, iremos excluir a divisão por um e pelo próprio número, pois resultam em resto zero.
#Dividiremos por todos os valores entre o número a ser testado e um. Por esta razão, iniciaremos dividindo por 2
#até n-1.

x=int(input('Entre com um número inteiro:')) #Pede-se para inserir um valor inteiro
prime=True
y=2
if x==0 or x==1:# Zero e um não são por definição primos.
    prime=False
else:
    while y < x and prime == True:
        print(y)
        if x % y == 0: #Enquanto o resto não for zero o número é primo. Se o resto for zero, o número deixa de ser primo.
            prime = False #se não for primo, sai da condição de looping
        y += 1

if prime == False:
    print(x, ' não é primo')
else:
    print(x, ' é primo')
