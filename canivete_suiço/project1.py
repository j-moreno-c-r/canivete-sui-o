def linha():
  print("_:"*25)
  #nj recebe nome do jogador
  # nk = numero de kills 

def jogador(nj = ("anom") , nk = 0 ):
 
  nj = "anom"
  nk = 0
  
  nj = input("nome do jogador:")
  nk = input("inimigos abatidos(quantidade):")
  print(f"O P.J {nj} matou {nk} ininmigos!!!")



#programa_principal
linha()
jogador()
linha()

