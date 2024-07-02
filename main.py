import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

pepespwnx=300
pepespwny=300
print (pepespwnx)
print (pepespwny)
alex = pygame.image.load("player.png")
alex_rect = alex.get_rect()
alex_rect.x=253
alex_rect.y=242

pepe = pygame.image.load("angrypepe.png")
pepe_rect = pepe.get_rect()
pepe_rect.x=pepespwnx
pepe_rect.y=pepespwny

pepespwnx1=1
pepespwny1=1
pepe1 = pygame.image.load("angrypepe.png")
pepe_rect1 = pepe1.get_rect()
pepe_rect1.x=pepespwnx1
pepe_rect1.y=pepespwny1
