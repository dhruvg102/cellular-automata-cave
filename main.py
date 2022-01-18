import pygame, sys, random
import numpy as np

screenW = 1200
screenH = 800
rez = 5
threshold = 50
BLACK = (0,0,0)
WHITE = (200,200,200)
W = int(screenW/rez)
H = int(screenH/rez)

def genmap():
    grid = []
    i, j = 0, 0
    while i < screenW/rez:
        a = []
        while j < screenH/rez:
            if random.randint(0,100) > threshold:
                color = BLACK
            else:
                color = WHITE
            a.append(color)
            #pygame.draw.rect(screen, color, (i * rez, j * rez, rez, rez), 0)
            j +=1
        grid.append(a)
        j = 0
        i +=1
    return grid

def neighbors(gridx, gridy):
    wallcount = 0

    if buffer[gridx-1][gridy-1] == BLACK:
        wallcount += 1
    if buffer[gridx-1][gridy] == BLACK:
        wallcount += 1
    if buffer[gridx-1][gridy+1] == BLACK:
        wallcount += 1
    if buffer[gridx][gridy-1] == BLACK:
        wallcount += 1
    if buffer[gridx][gridy+1] == BLACK:
        wallcount += 1
    if buffer[gridx+1][gridy-1] == BLACK:
        wallcount += 1
    if buffer[gridx+1][gridy] == BLACK:
        wallcount += 1
    if buffer[gridx+1][gridy+1] == BLACK:
        wallcount += 1

    return wallcount



def smoothmap():
    i = 1
    j = 1
    while i < W-1:
        while j < H-1:
            neighbourwall = neighbors(i,j)

            if neighbourwall > 4:
                buffer[i][j] = BLACK
            elif neighbourwall < 4:
                buffer[i][j] = WHITE
            j += 1
        j = 0
        i+=1


pygame.init()

x=1
y=1

screen = pygame.display.set_mode((screenW, screenH))
screen.fill((45,45,45))
clock = pygame.time.Clock()


buffer = genmap()
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                buffer = genmap()
            if event.key == pygame.K_RETURN:
                smoothmap()
                # print(neighbors(x,y))
                # x +=1
                # y +=1
    i = 0
    j = 0
    while i < W:
        while j < H:
            pygame.draw.rect(screen, buffer[i][j], (i * rez, j * rez, rez, rez), 0)
            j += 1
        j = 0
        i += 1

    smoothmap()
    pygame.display.update();
    clock.tick(5)
