import pygame

class Sprite :
    def __init__(self, image):
        self.image = image

    def draw(self, screen, position, direction):
        rotImg = pygame.transform.rotate(self.image, direction)
        rotRect = rotImg.get_rect()
        rotRect.center = position
        screen.blit(rotImg, rotRect)