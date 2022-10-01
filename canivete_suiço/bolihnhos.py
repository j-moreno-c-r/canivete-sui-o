
def contador():
    iniciar = input("quer iniciarao programa? s/n (para fechar digite 69)")
    while iniciar != "n" or 69:
        valor = int(input("quantos bolinhos você comeu? "))
        if valor < 10 and valor > 0:
            print(f"o numero de bolinhos foi: {valor}")
        if valor > 10 or valor == 10 :
            print("o numero de bolinhos foi : muitos")
        if valor == 69: 
             break
# se o valor dos bolinho for maior ou igual a 10 deve ser retoranado muitos, e não o valor.
        

contador()
""" dado um  contador inteiro do numero de donuts, retorne uma string 
com o formato number of donuts: <cont> onde?<count> é o numero 
recebido. entretanto, se o contador for 10 ou mais, use a palavra many 
ao inves  do contador """