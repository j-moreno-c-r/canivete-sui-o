import os


def main():
    print("Olá mundo!")
    print("Esta é a saudação de alice.")
    print("Esta é a saudaçõ\'es do bob.")

    foo(5, 10)

    print("=" * 10)
    teste = "o diretório de trabalho atual é"
    print(teste + os.getcwd())

 
    comidas =  ["maçãs", "laranjas", "chocolates"]

    for comida in comidas:
        print("eu gosto de comer", comida)
    
    print("conte até dez:")
    for i in range(1, 11):
        print(i)

def foo(a, b ):
    valor = a + b

    print("%s mais %s é igual a %s" % (a, b, valor))

    if valor < 50:
        print("foo")
    elif (valor  >= 50) and ((a == 42) or (b == 24)):
         print("bar")
    else:
        print("moo")
    """uma string multi_line, mas também pode ser um comentário multi_line"""

    return valor #essa é a unica linha de comentário


if __name__ == "__main__":
    main()
    #versão em português do código de Henrique Bastos do welcome to the django.
