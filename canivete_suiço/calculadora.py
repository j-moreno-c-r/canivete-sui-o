
from math import sqrt

num1 = int(input("Digite um numero:"))
opção1 = int(input("""Você quer:
[1] transformar esse numero em outro tipo.
[2] fazer uma conta de mais de um numero, digitar mais um para a operação.
[3] fazer uma conta apenas com esse numero 
[4] para fechar o programa : """))

# "op" é o nome de variavel que eu usei para opção secundaria!!!


if opção1 == 1:
        op2 = int(input('''Você quer transferir seu numero para : 
            [1]  BINÁRIO
            [2]  OCTAL
            [3]  HEXADECIMAL
            sua opção: '''))   

        if op2 == 1:
            (print(f"O resultado da conversão é {(bin(num1))}"))
        if op2 == 2:
                (print(f"O resultado da conversão é {(oct(num1))}"))
        if op2 == 3:
                (print(f"O resultado da conversão é {(hex(num1))}"))

if opção1 == 2:
        num2 = float(input("Digite  um outro numero:"))
        op3 = int(input("""Você quer:
        [1] somar os dois numeros
        [2] subtrair o SEGUNDO do PRIMEIRO
        [3] subtrairo PRIMEIRO do SEGUNDO
        [4] dividir o SEGUNDO pelo PRIMEIRO
        [5] dividir o PRIMEIRO pelo SEGUNDO
        [6] multiplicar os numeros"""))

        if op3 == 1:
                print(f"o resultado é de : {num1+num2}")

        if op3 == 2:
                print(f"o resultado é: {num1 - num2}")
        if op3 == 3:
                print(f"o resultado é de : {num2 - num1}")
        if op3 == 4:
                print(f"o resultado é de : {num1/num2}")
        if op3 == 5:
                print(f"o resultado é de : {num2/num1}")
        if op3 == 6:
                print(f"o resultado é de : {num1 * num2}")

if opção1 == 3:
        op3 = int(input("""Você quer realizar qual da seguintes operações:
        [1] raiz quadrada do primeiro numero
        [2] primeiro numero elevado ao quadrado
        [3] elevado ao cubo  """))
        if op3 == 1:
            print(f"o resultado é de : {sqrt(num1)}")
        if op3 == 2:
            print(f"o resultado é de : {num1 * num1}")
        if op3 == 3:
            print(f"o resultado é de: {num1*num1*num1}")
if opção1 == 4:
        print("programa fechado adeus!")