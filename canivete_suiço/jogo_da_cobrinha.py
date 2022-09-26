from re import X
import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 1000 
altura = 700#proporções da tela
x_cobra = largura/2
y_cobra = altura/2 # area inicial do quadrado
velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40 , 600)
y_maca = randint(50, 430 )#para randomizar as novas posições pós impacto do outro quadrado
pontos = 0
fonte = pygame.font.SysFont( "ink free", 40,True, True )#parametros para o texto
#respectivamente fonte,tamanho,negrito,itálico




tela = pygame.display.set_mode((largura, altura))#gera a tela

pygame.display.set_caption("jogo de J.M")#gera o título

relogio = pygame.time.Clock()#controle de movimento

list_cobra = []#salva o resulatado da armzenagem de fora do loop
comprimeto_inicial = 10
morreu =  False
def aumenta_cobra(list_cobra):
    for XeY in list_cobra:
        pygame.draw.rect(tela, (0,250,0), (XeY[0], XeY[1], 20, 20))#rastros da cobra



def reiniciar_jogo():
  global pontos,comprimento_inicial,x_cobra,y_cobra,saalist_cabeca,x_maca,y_maca,morreu
  pontos = 0 
  comprimento_inicial = 5
  x_cobra = int(largura/2)
  y_cobra = int(altura/2)
  lista_cobra = []
  list_cabeca = []
  x_maca = randint(40 , 600)
  y_maca = randint(50, 430 )


  morreu = False




while True:
    relogio.tick(30)#controle de movimento e velocidade do movimento
    tela.fill((100, 100, 100))#loop da tela
    mensagem = f"pontos: {pontos}"#string do texto
    texto_formatado = fonte.render(mensagem, True, (200,0,0))#parametros para o texto final
    #respectivamente a mensagem,função que define o pixelamento do texto(v,f), cor

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            exit()

        if event.type == KEYDOWN:

            if event.key == K_a:
              if x_controle == velocidade:
                 pass#impede ue a cabeça se teletransporte para a ponta oposta
              else: 
                x_controle = -velocidade 
                y_controle = 0

            if event.key == K_d:
              if  x_controle == -velocidade:
                pass
              else:
                x_controle =  velocidade 
                y_controle = 0

            if event.key == K_s:
             if  y_controle == -velocidade:
                pass
             else:
                y_controle=   velocidade 
                x_controle = 0

            if event.key == K_w:
              if  y_controle == velocidade:
                pass
              else:
                y_controle =  -  velocidade 
                x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra,30,30))#gera o quadrado 1 sua dimensões e cores
    
    maca = pygame.draw.rect(tela, (250,0, 100), (x_maca,y_maca,30,30)) #gera o quadrado 2 sua dimensões e cores
    
    if cobra.colliderect(maca):
       x_maca = randint(40 , 600)
       y_maca = randint(50 , 430)#gera o resultado do random da colisão
       pontos = pontos + 1 #contador do texto
       comprimeto_inicial = comprimeto_inicial + 1

    list_cabeca = []
    list_cabeca.append( x_cobra)
    list_cabeca.append(y_cobra)

    list_cobra.append(list_cabeca)#rastro da cobra]

    if list_cobra.count(list_cabeca)> 1:
      fonte2 = pygame.font.SysFont("ink free", 40,True, True )
      mensagem = "game over!!! pressione a tecla "r" para reiniciar"
      texto_formatado = fonte2.render(mensagem,True, (0,0,0))
      ret_texto = texto_formatado.get_rect()
      morreu = True
      while morreu:
        tela.fill((255,255,255))
        for event in pygame.event.get():
          if event.type == QUIT:
            exit()
          if event.type == KEYDOWN:
            if event.key == K_r:
              reiniciar_jogo()

        ret_texto.center = (largura//2, altura//2)
        tela.blit(texto_formatado,(ret_texto))
        pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
       y_cobra = altura
    if y_cobra > altura:
      y_cobra = 0
   
    

    if len(list_cobra) > comprimeto_inicial:
        del list_cobra[0]
    aumenta_cobra(list_cobra)

    tela.blit(texto_formatado,(400, 40))
    pygame.display.update()#gera o loop total
 