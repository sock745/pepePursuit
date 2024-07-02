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

bg = pygame.image.load("gameover.png")

speed = 5

def draw():
  screen.blit(alex,(alex_rect.x,alex_rect.y))
  screen.blit(pepe,(pepe_rect.x,pepe_rect.y))
  screen.blit(pepe1,(pepe_rect1.x,pepe_rect1.y))
  pygame.display.update()

def quit_game():
  global run
  for event in pygame.event.get():
    if alex_rect.colliderect(pepe_rect):
      run = False
    elif alex_rect.colliderect(pepe_rect1):
      run = False  
run = True

while run:
  clock.tick(30)
  screen.fill((248,236,209))
  
  draw()
  quit_game()
    #print (str(alex_rect.x) + " , " + str(alex_rect.y)
  
  userInput = pygame.key.get_pressed()
  if userInput[pygame.K_a]:
    alex_rect.x-= speed
  if userInput[pygame.K_d]:
    alex_rect.x += speed
  if userInput[pygame.K_w]:
    alex_rect.y -= speed
  if userInput[pygame.K_s]:
    alex_rect.y += speed
  #782 x
#-51 x

# -17 y
# 408 y
  if alex_rect.x >= 782:
    alex_rect.x = -10
  elif alex_rect.x <= -10:
    alex_rect.x = 782

  if alex_rect.y >= 408:
    alex_rect.y = -10
  elif alex_rect.y <= -10:
    alex_rect.y = 408

  pepe_rect.x += random.randint(5,10)
  pepe_rect.y += random.randint(5,10)
  pepe_rect1.x -= random.randint(5,10)
  pepe_rect1.y -= random.randint(5,10)
