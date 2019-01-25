#!/usr/bin/env python3

""""Programa que lista os números primos até um valor especificado."""

# Definição de número primo: um número é primo quando o resto da divisão dele por ele mesmo e por um for zero
# Pela definição acima, iremos excluir a divisão por um e pelo próprio número, pois resultam em resto zero.
# Dividiremos por todos os valores entre o número a ser testado e um. Por esta razão, iniciaremos dividindo por 2
# até n-1.

k = int(input('Entre com o limite superior para a lista de primos:'))  # Pede-se para inserir um valor inteiro


def isprime(x):
    prime = True
    y = 2
    if x == 0 or x == 1:  # Zero e um não são por definição primos.
        prime = False
    else:
        while y < x and prime == True:
            if x % y == 0:  # Enquanto o resto não for zero o número é primo. Se o resto for zero, o número deixa de ser primo.
                prime = False  # se não for primo, sai da condição de looping
            y += 1

    if prime == True:
        print('O número',x,' é primo.')
    return

def list_primes(k): # O argumento da função é o número que especifica o limite superior da listagem
    for x in range(k): # looping que toma valores inteiros, testando-os a sua primalidade, até o limite superior k
        isprime(x)

list_primes(k) #Chama a função list_primes e imprime na tela a lista de primos.