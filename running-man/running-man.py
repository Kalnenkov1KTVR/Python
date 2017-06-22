import pygame, random
pygame.init()

def blitfunc():
    screen.blit( background, (0, 0) )
    screen.blit( platform, (platx, platy) )
    screen.blit( man, (x, y) )
    screen.blit( duck, (duckx, ducky) )
    pygame.display.flip()

platx = 400
platy = 1000

duckx = 700
ducky = 1000

screen = pygame.display.set_mode([800, 500])

back0 = pygame.image.load("back0.jpg")
back1 = pygame.image.load("back1.jpg")
back2 = pygame.image.load("back2.jpg")
back3 = pygame.image.load("back3.jpg")
back4 = pygame.image.load("back4.jpg")
back5 = pygame.image.load("back5.jpg")

right1 = pygame.image.load("right1.png")
right2 = pygame.image.load("right2.png")
right3 = pygame.image.load("right3.png")
left1 = pygame.image.load("left1.png")
left2 = pygame.image.load("left2.png")
left3 = pygame.image.load("left3.png")

platform = pygame.image.load("platform.png")

duck1l = pygame.image.load("duck1l.png")
duck2l = pygame.image.load("duck2l.png")
duck1r = pygame.image.load("duck1r.png")
duck2r = pygame.image.load("duck2r.png")         

background = back1
duck = duck1l

x = 0
y = 300
count = 0
pygame.key.set_repeat(1,1)
man = right1

blitfunc()

platmove = True
duckmove = True

running = True
while running:
    
    pygame.time.delay(3)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            count += 1
                
            man = right1
            blitfunc()
                
            if man == right1:
                if man == right1 and ( count % 2 == 0):    
                    man = right2
                blitfunc()
                                
                if man == right2 and ( count % 3 == 0):    
                    man = right3
                blitfunc()
                                                       
            x += 10
                
        if keys[pygame.K_LEFT]:
            count += 1
                
            man = left1
            blitfunc()
                
            if man == left1:
                if man == left1 and ( count % 2 == 0):    
                    man = left2
                blitfunc()
                            
                if man == left2 and ( count % 3 == 0):    
                    man = left3
                blitfunc()
                                                
            x -= 10
            
        if keys[pygame.K_UP]:
            ground = y
            while y > ground - 110:
                y -= 5
                blitfunc()
                if keys[pygame.K_RIGHT]:
                    man = right2
                    x += 3
                    blitfunc()
                if keys[pygame.K_LEFT]:
                    man = left1
                    x -= 3
                    blitfunc()

            while y < ground:
                y += 5
                blitfunc()
                if keys[pygame.K_RIGHT]:
                    man = right2
                    x += 3
                    blitfunc()
                if keys[pygame.K_LEFT]:
                    man = left1
                    x -= 3
                    blitfunc()
                
    if x > 800:
        x = -100
        if background == back1:
            background = back2
        elif background == back2:
            background = back3
        elif background == back3:
            background = back4
        elif background == back4:
            background = back5
        blitfunc()
    if x < -100:
        x = 800
        if background == back1:
            background = back0
        elif background == back2:
            background = back1
        elif background == back3:
            background = back2
        elif background == back4:
            background = back3
        elif background == back5:
            background = back4
        blitfunc()

    if background == back0 and x < (689-70):
        while y < 600:
            y += 10
            blitfunc()
        background = back1
        x = 0
        y = 300        
        blitfunc()
    
    if background == back2 and x > (324-30) and x < (423-70):
        while y < 600:
            y += 10
            blitfunc()
        background = back1
        x = 0
        y = 300        
        blitfunc()

    if background == back3 and ((x > 196-30 and x < 295-70) or (x > 492-30 and x < 591-70)):
        while y < 600:
            y += 10
            blitfunc()
        background = back1
        x = 0
        y = 300        
        blitfunc()

    if platmove == True:
        platx += 1
        if platx > 490:
            platmove = False
    else:
        platx -= 1
        if platx < 197:
            platmove = True
    blitfunc()
    
    if background == back4:
        platy = 389
    else:
        platy = 1000
                
    if background == back4 and (x > (196-30) and x < (591-70)):
        if (x > (platx-70) and x < (platx+70)):
            y = 300
            if platmove == True:
                x += 1
            else:
                x -= 1
        else:
            while y < 600:
                y += 10
                blitfunc()
            background = back1
            x = 0
            y = 300        
            blitfunc()
            
    if background == back5:  
        ducky = 335
    else:
        ducky = 1000

    if duckmove == True:
        duckx += 1
        if duckx > 740:
            duckmove = False
            duck = duck1l
    else:
        duckx -= 1
        if duckx < 5:
            duckmove = True
            duck = duck1r
    blitfunc()       

    if duck == duck1l:
        duck = duck2l
        blitfunc()
    if duck == duck2l:
        duck = duck1l
        blitfunc()
    if duck == duck1r:
        duck = duck2r
        blitfunc()
    if duck == duck2r:
        duck = duck1r
        blitfunc()
    
pygame.quit()
