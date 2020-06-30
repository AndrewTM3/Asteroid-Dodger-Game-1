#main file
import sys, pygame
from pygame.locals import*

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

#main function
def main():
  #maximum refreshery
  clock.tick(60)
  #set screen color
  screen.fill(color)
  pygame.display.flip()

if __name__ == "__main__":
  main()

