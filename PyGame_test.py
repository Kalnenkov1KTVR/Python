import pygame, sys
from pygame.locals import *
pygame.init()

width = 640
height = 480
title = "PyGame Test"

screen = pygame.display.set_mode((width, height) ,0, 32)
pygame.display.set_caption(title)
background = ( 220, 230, 240 )

screen.fill( background )

offset = 0
while offset < 100 :
    pygame.draw.line( screen, (255, 255, 0), [100, 210+offset], [300, 210+offset], 5)
    offset += 10
        
pygame.draw.line( screen, (255, 0, 0), [150, 150], [100, 200], 3)
pygame.draw.line( screen, (255, 0, 0), [100, 200], [300, 200], 3)
pygame.draw.line( screen, (255, 0, 0), [150, 150], [250, 150], 3)
offset = 0
while offset < 110 :
    pygame.draw.line( screen, (255, 0, 0), [150+offset, 150], [200+offset, 200], 3)
    offset += 10

pygame.draw.rect( screen, (0, 255, 255), [225, 225, 50, 50], 3 )
    
pygame.draw.rect( screen, (255, 255, 255), [125, 225, 50, 75], 3 )
    
pygame.draw.rect( screen, (255, 155, 0), [200, 140, 15, 10], 3 )

pygame.draw.ellipse( screen, (0, 0, 0), [195, 120, 10, 10], 5 )
pygame.draw.ellipse( screen, (0, 0, 0), [190, 110, 15, 15], 5 )
pygame.draw.ellipse( screen, (0, 0, 0), [195, 100, 20, 20], 5 )
    
pygame.display.update() 
    
done = True
while done: 
    for event in pygame.event.get(): 
        if event.type == QUIT: 
            done = False
pygame.quit()
