import pygame
class Button:
    def __init__(self, image, x, y,clicked,surf):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = clicked
        self.surf = surf

    def draw(self):

        action = False
        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check mouse over
        if self.rect.collidepoint(pos):
            butts = pygame.mouse.get_pressed()
            if butts[0]:
                self.clicked = True
                

        
        # draw on screen
        
        self.surf.blit(self.image, (self.rect.x, self.rect.y))

        return action