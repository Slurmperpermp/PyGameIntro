import pygame
pygame.init()

class char(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
 
        # self.rect = pygame.Rect(0,0,160,160)
        # self.image = pygame.image.load("Picka.png")

        self.image = pygame.Surface([200, 201])
        self.image.fill((255,255,255))
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()


mainChar = pygame.image.load("Picka.png")

mainCharRect = mainChar.get_rect()

screen = pygame.display.set_mode([700,800])

mainChar = char()

done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               mainChar.rect.x -= 5
            if event.key == pygame.K_RIGHT:
                mainChar.rect.x += 5
                
            if event.key == pygame.K_UP:
                mainChar.rect.y -= 5
              
            if event.key == pygame.K_DOWN:
                mainChar.rect.y += 5

    screen.fill((0,0,0))
    screen.blit(mainChar.image, mainChar.rect)
    pygame.display.flip()

