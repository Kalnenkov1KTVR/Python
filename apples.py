import pygame, sys, random
pygame.init()

def drawApple(x, y):
    pygame.draw.circle(screen, [192,0,0], [x, y], 20, 0) 
    pygame.draw.line(screen, [0,0,0], [x, y-10], [x+10, y-30], 5) 

def drawPlayer(x, y):
    pygame.draw.circle(screen, [34,177,76], [x, y], size, 0)
    
screen = pygame.display.set_mode([800, 600])
pygame.display.set_caption("Yablozhor v0.7") 
score = 0
ountearv = random.randint(25, 75)

ounad = []
for i in range (ountearv):
    ounx = random.randint(50, 750)
    ouny = random.randint(100, 550)
    ounad.append([ounx, ouny])

size = 20
distance = 30

x = 50
y = 50
clock = pygame.time.Clock()

pygame.key.set_repeat(1,10)

running = True 
while running:

    step = random.randint(1, 3)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False       
        
    keys = pygame.key.get_pressed() #rabotaet dvigenie po diagonali
    if keys[pygame.K_LEFT]:
        x -= step
    if keys[pygame.K_RIGHT]:
        x += step
    if keys[pygame.K_UP]:
        y -= step
    if keys[pygame.K_DOWN]:
        y += step        

    if x > 800:
        x = 0

    if x < 0:
        x = 800

    if y > 600:
        y = 0

    if y < 0:
        y = 600
        
    screen.fill([255, 255, 255])
                       
    if score == ountearv: 
        print("Fl-AWWW-less ZHIROVICTORY!")
        running = False
    else:  
        for oun in ounad:
            if abs(oun[0] - x) < distance and abs(oun[1] - y) < distance:
                ounad.remove(oun)
                score += 1
                size += 2
                distance += 1
                print( "Apple:", oun[0], oun[1], "Player:", x, y )
     
    for oun in ounad:
        drawApple(oun[0], oun[1])

    
        
    pygame.time.delay(5)
    drawPlayer(x, y)
    pygame.display.flip()
    clock.tick(200)
        
pygame.quit()











