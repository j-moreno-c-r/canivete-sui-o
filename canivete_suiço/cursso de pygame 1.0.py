import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480
x = largura/2
y = altura/2
#a = 60
#b = 30
tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("jogo de J.M")

relogio = pygame.time.Clock()


while True:
    relogio.tick(60)
    tela.fill((100, 100, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

            exit()
       
        """if event.type == KEYDOWN:
            if event.key == K_a:
              x = x - 20  
            if event.key == K_d:
              x = x + 20
            if event.key == K_s:
              y = y + 20
            if event.key == K_w:
              y = y - 20"""
    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
          x = x + 10
    if pygame.key.get_pressed()[K_w]:
           y = y - 10
    if pygame.key.get_pressed()[K_s]:
           y = y + 10


    pygame.draw.rect(tela, (200,200,0), (x, y,40,40)) 
    
    pygame.display.update()
 
    """pygame.draw.circle(tela, (0,120,120), (a, b), 40)
    if b >= altura:
        b = 0
    b = b+1"""
 
    #pygame.draw.line(tela, (255,255,0), (390, 0), (390, 600), 5)
    #pygame.display.update()