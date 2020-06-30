#main file
import sys, pygame
from pygame.locals import*
from ship import*
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



#main function
def main():
  global Level

  while Level<=NumLevels:
    #refresh rate
    clock.tick(60)
    for event in pygame.event.get():
      if event.type==QUIT:
        sys.exit()

  #maximum refreshery
  clock.tick(60)
  #set screen color
  screen.fill(color)
  #add in ship image
  screen.blit(Player.image,Player.rect)
  pygame.display.flip()
  

if __name__ == "__main__":
  main()

