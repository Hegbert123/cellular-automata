import pygame
import random

pygame.init()

tileWidth =  240#30
tileHeight = 200# 17
tileSize = 4
width = tileWidth * tileSize
height = tileHeight * tileSize
screen = pygame.display.set_mode((width, height))



class Square():

    def __init__(self, x, y):
        self.x = x
        self.y = y
        ran= random.randint(1,100)
        if ran < 60:
            #land
            self.type =1
        else:
            self.type =0

    def drawSquare(self):
        if self.type == 0:
            #sea
           pygame.draw.rect(screen,(0,0,255),(self.x * tileSize, self.y * tileSize, tileSize, tileSize))
        elif self.type == 1:
            #land
            pygame.draw.rect(screen,(160,82,45),(self.x * tileSize, self.y * tileSize, tileSize, tileSize))

        elif self.type ==2:
             pygame.draw.rect(screen,(0,0,0),(self.x * tileSize, self.y * tileSize, tileSize, tileSize))
    def getType(self):
        return self.type

    def changeType(self, tiles):
        self.sea, self.land = self.getNeighbors( tiles)
        if self.sea >= 5:
            self.type = 0
        elif self.land > 5:
            self.type = 1

    def getNeighbors(self, tiles):
        self.sea = 0
        self.land = 0
        for c in range(self.y - 1, self.y + 2):
            for r in range(self.x - 1, self.x + 2):
                if not c < 0 and not c >= tileHeight and not r < 0 and not r >= tileWidth:
                    #print(c, r)
                    if c == self.y and r == self.x:
                        pass
                    else:
                        if tiles[c][r].getType() == 0:
                            self.sea +=1
                        else:
                            self.land +=1
                else:
                   self.sea +=1

        return self.sea, self.land
       #if self.sea >= 4:
        #   self.type = 0
        #lif self.land => 4:
         #  self.type = 1



def smooth():
    for c in range(tileHeight):
    
        for r in range(tileWidth):
            tiles[c][r].changeType(tiles)


tiles = []
def generateMap():
    global tiles

    tiles = []


    #type =1 is land


    for c in range(tileHeight):
    
        tiles.append([])
        for r in range(tileWidth):
            tiles[c].append(Square(r,c))



def countLand():
    numtiles = 0
    numland = 0
    for c in range(tileHeight):
    
        for r in range(tileWidth):
            if tiles[c][r].getType(tiles) == 1:
                land +=1
            tiles +=1
    print("tiles: ", numtiles, " numlands: ", numland)



generateMap()

running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print(tiles)

            if event.key == pygame.K_e:
                smooth()
            if event.key == pygame.K_x:
                o, l = tiles[5][5].getNeighbors(tiles)
                print("ocean: ", o, "\n land: ", l)

            if event.key == pygame.K_c:
                tiles[29][59].type = 2

            if event.key == pygame.K_b:
                countLand()
            if event.key == pygame.K_SPACE:
                generateMap()
    for c in range(tileHeight):
    
        for r in range(tileWidth):
            tiles[c][r].drawSquare()
    pygame.display.update()