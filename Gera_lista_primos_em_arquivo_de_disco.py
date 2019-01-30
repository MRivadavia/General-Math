#!/usr/bin/env python3

""""Programa que lista os números primos até um valor especificado e grava em disco a lista."""

# Definição de número primo: um número é primo quando o resto da divisão dele por ele mesmo e por um for zero
# Pela definição acima, iremos excluir a divisão por um e pelo próprio número, pois resultam em resto zero.
# Dividiremos pelos valores entre (n-1)/2 o número a ser testado e um. Por esta razão, iniciaremos dividindo por 2
# até (n-1)/2.
#print('Lista de Maior velocidade.')

# file=open('primos.txt','w')

k = int(input('Entre com o limite superior para a lista de primos:'))  # Pede-se para inserir um valor inteiro
lista_primos = '' #string em que será armazenada a lista de primos.

def isprime(x):
    global lista_primos,z #variáveis globais
    prime = True
    y = 2
    if x == 0 or x == 1:  # Zero e um não são por definição primos.
        prime = False
    else:

        j=(x-1)/2
        if x == 4:
            prime=False
        else:
            while y < j and prime == True:
                if x % y == 0:  # Enquanto o resto não for zero o número é primo. Se o resto for zero, o número deixa de ser primo.
                    prime = False  # se não for primo, sai da condição de looping
                y += 1

    if prime == True:
        print('O número',x,' é primo.')
        lista_primos=lista_primos+' '+str(x) #acrescenta a string números primos

    if (x<=k):#criação de arquivo dos números primos
        file=open('primos.txt', 'w') #abre um arquivo txt com o nome: primos.txt e grava
        z='Listagem de números primos até o valor de'+' '+str(k)
        file.write(z+'\n') # grava primeira linha do arquivo primos.txt
        file.write('\n') #grava uma linha em branco no arquivo primos.txt
        file.write(lista_primos) #grava no arquivo primos.txt a lista de primos
        file.close() #fecha arquivo primos.txt

    return

def list_primes(k): # O argumento da função é o número que especifica o limite superior da listagem
    # for x in range(k): # looping que toma valores inteiros, testando-os a sua primalidade, até o limite superior k
    #     isprime(x)
    x=0
    for x in range(5):
        isprime(x)
        if x==4:
            x=5

    if x >= 5:
        while x < k:
            isprime(x)
            x += 2

list_primes(k) #Chama a função list_primes e imprime na tela a lista de primos.
