import pygame

class Sprite :
    def __init__(self, image):
        self.image = image

    def draw(self, screen, position, rotation):
        rotImg = pygame.transform.rotate(self.image, rotation)
        rotRect = rotImg.get_rect()
        rotRect.center = position
        screen.blit(rotImg, rotRect)

    def draw_mirror(self, screen, position, rotation):
        rotImg = pygame.transform.flip(self.image, True, False)
        rotImg = pygame.transform.rotate(rotImg, rotation)
        rotRect = rotImg.get_rect()
        rotRect.center = position
        screen.blit(rotImg, rotRect)

    def get_rect(self):
        return self.image.get_rect()