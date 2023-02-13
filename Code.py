def soma(a, b):
    for i in range (b+1):
        print('%d + %d = %d'%(a, i, i+a))
def subtracao(a, b):
    for i in range (b+1):
        print('%d - %d = %d'%(a, i, a-i))
def multiplicacao(a, b):
    for i in range (b+1):
        print('%d x %d = %d'%(a, i, i*a))
def divisao(a, b):
    for i in range (1, b+1):
        print('%d / %d = %f'%(a, i, a/i))
def operadoraritmetico(operador):
    if operador == 1:
        return soma
    elif operador == 2:
        return subtracao
    elif operador == 3:
        return multiplicacao
    elif operador == 4:
        return divisao
    
while True:
    print('Operadores aritméticos: \nSoma(1) \nSubtração(2) \nMultiplicação(3) \nDivisão(4) \nSaída(5)')
    operador = int(input('Informe o operador desejado: '))
    if (operador == 5):
        break;
    funcao = operadoraritmetico(operador)
    a = int(input('Digite um número inteiro do qual se deseja ver a tabuada: '))
    b = int(input('Digite um número inteiro, que atuará como limitante da tabuada: '))
    resultado = funcao(a, b)
    print(resultado)