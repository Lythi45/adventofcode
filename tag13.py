import sys
import pygame
import time
from pygame.locals import *

BLOCKSIZE = 32
OFFSET = 20
GAP = 10
FPS = 5
WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
BG = pygame.image.load('background.jpg')

class Block(pygame.sprite.Sprite):

    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.width = BLOCKSIZE
        self.height = BLOCKSIZE
        self.image = pygame.Surface([BLOCKSIZE, BLOCKSIZE])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.severity = 0

    def move(self):
        self.rect.x += BLOCKSIZE + GAP


class Wall(pygame.sprite.Sprite):

    def __init__(self, depth, length):
        pygame.sprite.Sprite.__init__(self)

        self.length = length
        self.depth = depth
        self.image = pygame.Surface([BLOCKSIZE, BLOCKSIZE * length])
        self.image.fill((40, 40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = OFFSET + (depth * BLOCKSIZE) + (depth * GAP)
        self.rect.y = OFFSET

        self.block = Block((244, 66, 66), self.rect.x, OFFSET)
        self.block_direction = 1

        enemy_sprites.add(self.block)

    def move(self):
        if self.block.rect.y - OFFSET >= (self.length - 2) * BLOCKSIZE + OFFSET:
            self.block_direction = -1
        elif self.block.rect.y <= OFFSET:
            self.block_direction = 1

        self.block.rect.y += BLOCKSIZE if self.block_direction == 1 else (-BLOCKSIZE)

time.sleep(10)
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont(None, 30)
fpsClock = pygame.time.Clock()
cameraX = 0

enemy_sprites = pygame.sprite.Group()
player_sprite = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()

player = Block((57, 249, 92), OFFSET, OFFSET)
player_sprite.add(player)
# read wall locations from file
with open('tag13.txt', 'r') as f:
    df = f.readlines()
    for line in df:
        a, b = line.split(': ')
        wall_sprites.add(Wall(int(a)+1, int(b)))

# Game loop.
while True:
    # draw bg, walls and enemies
    SCREEN.fill((70, 137, 244))
    SCREEN.blit(BG,(0,0))

    for wall in wall_sprites:
        SCREEN.blit(wall.image, (wall.rect.x - cameraX, wall.rect.y))
    for enemy in enemy_sprites:
        SCREEN.blit(enemy.image,(enemy.rect.x - cameraX, enemy.rect.y))
    # handle keyboard input
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # Update
    player.move()
    # check collision
    for wall in wall_sprites:
        collision = pygame.sprite.collide_rect(player, wall.block)
        if collision:
            player.severity += wall.length * (wall.depth - 1)
        wall.move()
    # draw player
    SCREEN.blit(player.image, (player.rect.x - cameraX, player.rect.y))
    textsurface = myfont.render('Severity: {}'.format(player.severity), True, (107, 244, 66))
    SCREEN.blit(textsurface,(WIDTH - 200, HEIGHT - 50))

    cameraX += BLOCKSIZE + GAP

    pygame.display.flip()
    fpsClock.tick(FPS)