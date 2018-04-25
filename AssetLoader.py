# import the pygame module, so you can use it
import pygame


class AssetLoader:
    def __init__(self):
        self._step1_sound = pygame.mixer.Sound('assets/sfx/step1.wav')
        self._step2_sound = pygame.mixer.Sound('assets/sfx/step2.wav')
        self._flight1_sound = pygame.mixer.Sound('assets/sfx/flight.aiff')
        self._flight2_sound = pygame.mixer.Sound('assets/sfx/flight2.mp3')
        self._hit_sound = pygame.mixer.Sound('assets/sfx/hit.wav')
        self._win_sound = pygame.mixer.Sound('assets/sfx/win.wav')

        self._baton_sprite = pygame.image.load('assets/sprites/baton.png')
        self._duck_

    def get_step_sound1(self):
        return self._step1_sound

    def get_step_sound2(self):
        return self._step2_sound

    def get_flight_sound1(self):
        return self._flight1_sound

    def get_flight_sound2(self):
        return self._flight2_sound

    def get_hit_sound(self):
        return self._hit_sound

    def get_win_sound(self):
        return self._win_sound

