import pygame
#create ship class 
class Ship(pygame.sprite.Sprite):

#create init function that takes in position
  def __init__(self,pos):
    super().__init_()
    #create image
    self.image=pygame.image.load("ship.png")
    #scale image
    self.image=pygame.transform.smoothscale(self.image,(40,400))
    #rotate image
    self.image=pygame.transform.rotate(self.image,-90)
    #create image rectangle
    self.rect=self.image.get_rect()
    #move center of rectangle to function
    self.rect.center=pos
    #speed
    self.speed=pygame.math.Vector2(0,0)

  #update image
  def update(self):
    self.rect.move_ip(self.seed)


