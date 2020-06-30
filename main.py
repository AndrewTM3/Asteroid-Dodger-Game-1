#main file
import sys, pygame
from pygame.locals import*
from ship import*
from asteroid import*
pygame.init()
screen_info=pygame.display.Info()

#width and height
size=(width,height)=(int(screen_info.current_w*0.5)), int(screen_info.current_h*0.5)
screen=pygame.display.set_mode(size)

#Clock
clock=pygame.time.Clock()
#Color
color=(30,0,30)
#fill screen with color
screen.fill(color)

#setup variables
NumLevels=4
Level=1
AsteroidCount=3
Player=Ship((20,200))
Asteroids=pygame.sprite.Group()

#init function
def init():
  global AsteroidCount,Asteroids
  Player.reset((20,200))
  Asteroids.empty()
  AsteroidCount +=3
  for i in range(AsteroidCount):
    Asteroids.add(Asteroid((random.randint(50,width-50),random.randint(50,height-50)),random.randint(15,60)))

#main function
def main():
  global Level
  init()
  while Level<=NumLevels:
    #refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type==QUIT:
        sys.exit()
        if event.type==pygame.KEYDOWN:
          #Right arrow
          if event.key==pygame.K_RIGHT:
            #Speed of arrow
            Player.speed[0]=10
            #left arrow
          if event.key==pygame.K_LEFT:
            #Left arrow speed
            Player.speed[0]=-10
            #Up arrow
          if event.key==pygame.K_UP:
            #Up arrow Speed
            Player.speed[1]=10
            #Down Arrow
          if event.key==pygame.K_Down:
            #Down Arrow speed
            Player.speed[1]=-10
        if event.type==pygame.KEYUP:
          if event.key==pygame.K_RIGHT:
            #Speed of arrow
            Player.speed[0]=0
            #left arrow
          if event.key==pygame.K_LEFT:
            #Left arrow speed
            Player.speed[0]=0
            #Up arrow
          if event.key==pygame.K_UP:
           #up arrow speed
            Player.speed[1]=0
            #Down arrow
          if event.key==pygame.K_Down:
           #Down Arrow Speed
            Player.speed[1]=0 
    Player.update()
    Asteroids.update()
  
    #maximum refreshery
    clock.tick(60)
    #set screen color
    screen.fill(color)

    Asteroids.draw(screen)
   #add in ship image
    screen.blit(Player.image,Player.rect)
    pygame.display.flip()
  

if __name__ == "__main__":
  main()

