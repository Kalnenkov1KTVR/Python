import pygame, sys, random
pygame.init()

def drawTarget(x, y):
    pygame.draw.circle(screen, [255,0,0], [x, y], 10, 0)  
 
screen = pygame.display.set_mode([800, 600])
background = pygame.image.load("cloud-example.jpg")
background = pygame.transform.scale(background, (800, 600)).convert()
window = pygame.Surface((800, 600))

fuel = 500
score = 0
count = 25
targets = []
for i in range (count):
    targetx = random.randint(50, 750)
    targety = random.randint(100, 550)
    targets.append([targetx, targety])

class Menu:
    def __init__(self, points = [370, 260, 'Point', (120, 20, 120), (250, 250, 20), 0]):
        self.points = points
    def render(self, surface, font, num_point):
        for i in self.points:
            if num_point == i[5]:
                surface.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                surface.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))
    def menu(self):
        running = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(0, 1)
        pygame.mouse.set_visible(True)
        point = 0
        
        while running:
            window.fill((50, 150, 250))

            mp = pygame.mouse.get_pos()
            for i in self.points:
                if mp[0]>i[0] and mp[0]<i[0]+155 and mp[1]>i[1] and mp[1]<i[1]+10:
                    point = i[5]
            self.render(window, font_menu, point)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_UP:
                        if point > 0:
                            point -= 1
                    if event.key == pygame.K_DOWN:
                        if point < len(self.points)-1:
                            point += 1
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if point == 0:
                        running = False
                    elif point == 1:
                        pygame.quit()
                        sys.exit()
               
            screen.blit(window, (0, 0))
            pygame.display.flip()

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
    def render(self):
        screen.blit(self.bitmap,(self.x, self.y))
        
def Intersect(s1_x, s2_x, s1_y, s2_y):
    if ((s1_x > s2_x-48) and (s1_x < s2_x+48) and (s1_y < s2_y-33) and (s1_y < s2_y+33)):
        return 1
    else:
        return 0

red = Sprite(10, 267, "redr.png")
blu = Sprite(704, 267, "blul.png")
bgoleft = True
bgodown = True

points = [(370, 260, 'Play', (120, 20, 120), (250, 250, 20), 0),
          (370, 320, 'Quit', (120, 20, 120), (250, 250, 20), 1)]

game = Menu(points)
game.menu()
               
running = True
pygame.key.set_repeat(1, 1)

while running:
        
    if red.x > 704:
        red.x = 704

    if red.x < 0:
        red.x = 0

    if red.y > 534:
        red.y = 534

    if red.y < 0:
        red.y = 0

    if bgoleft == True:
        blu.x -= 1
        if blu.x < 0:
            bgoleft = False
            blu = Sprite(blu.x, blu.y, "blur.png")
    else:
        blu.x += 1
        if blu.x > 704:
            bgoleft = True
            blu = Sprite(blu.x, blu.y, "blul.png")

    if bgodown == True:
        blu.y += 1
        if blu.y > 534:
            bgodown = False
    else:
        blu.y -= 1
        if blu.y < 0:
            bgodown = True

    fuel -= 1
    if fuel == 0:
        print( "Out of fuel!" )
        #game.menu()
        running = False

    if Intersect(blu.x, red.x, blu.y, red.y) == 1:
        pygame.draw.rect(screen, [255,0,0], [red.x, red.x-96, red.y, red.y-66], 0)
        pygame.display.flip()
        print( "red.x, blu.x, red.y, blu.y:", red.x, blu.x, red.y, blu.y )
        print( "BOOM! Ne osobo umno stalkivatsa s drugim samoletom." )
        #game.menu()
        running = False
    
    screen.blit(background, (0, 0))

    if score == count: 
        print("All *thingies* are collected.")
        running = False
    else:  
        for target in targets:
            if abs(target[0] - red.x) < 96 and abs(target[1] - red.y) < 66:
                targets.remove(target)
                score += 1
                fuel += 100
     
    for target in targets:
        drawTarget(target[0], target[1])
        
    red.render()
    blu.render()
    pygame.display.flip()   
    pygame.time.delay(3)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        red.y -= 1
    if keys[pygame.K_DOWN]:
        red.y += 1
    if keys[pygame.K_LEFT]:
        red.x -= 2
        red = Sprite(red.x, red.y, "redl.png")
    if keys[pygame.K_RIGHT]:
        red.x += 2
        red = Sprite(red.x, red.y, "redr.png")
    if keys[pygame.K_ESCAPE]:
        game.menu()
        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(False)
        
pygame.quit()
