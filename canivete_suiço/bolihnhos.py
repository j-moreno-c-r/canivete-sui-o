
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
        

contador()
