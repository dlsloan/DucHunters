# import the pygame module, so you can use it
import pygame


class AssetLoader:
    def __init__(self):
        self.step1_sound = pygame.mixer.Sound('assets/sfx/step1.wav')
        self.step2_sound = pygame.mixer.Sound('assets/sfx/step2.wav')
        self.flight1_sound = pygame.mixer.Sound('assets/sfx/flight.aiff')
        #self.flight2_sound = pygame.mixer.Sound('assets/sfx/flight2.mp3')
        self.hit_sound = pygame.mixer.Sound('assets/sfx/hit.wav')
        #self.win_sound = pygame.mixer.Sound('assets/sfx/win.wav')
        self.baton_sprite = pygame.image.load('assets/sprites/baton.png')
        self.duck_sprite = pygame.image.load('assets/sprites/duck.jpg')
        self.duck2_sprite = pygame.image.load('assets/sprites/duck2.png')