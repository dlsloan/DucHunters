import pygame
import AssetLoader

_XMAX = 800
_YMAX = 600

_YSTEP = 50
_XSTEP = 50

class DuckHunter:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('minimal program')
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((128, 0, 128))
        logo = pygame.image.load("assets/ducklogo.png")
        pygame.display.set_icon(logo)

    def update_display(self):
        pygame.display.flip()
        self.screen.fill((128, 0, 128))


def move_down(game, assets, x, y):
    y = y + _YSTEP
    if y >= _YMAX:
        y = _YMAX - 1

    assets.step1_sound.play()

    return x,y


def move_up(game, assets, x, y):
    y = y - _YSTEP
    if y <= 0:
        y = 0

    assets.step1_sound.play()
    return x,y


def move_right(game, assets, x, y):
    x = x + _XSTEP
    if x >= _XMAX:
        x = _XMAX - 1

    assets.step1_sound.play()
    return x,y


def move_left(game, assets, x, y):
    x = x - _XSTEP
    if x <= 0:
        x = 0
    assets.step1_sound.play()
    return x,y


# define a main function
def main():
    game = DuckHunter()
    assets = AssetLoader.AssetLoader()
    running = True
    duck_x = 0
    duck_y = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                duck_x, duck_y = move_down(game, assets, duck_x, duck_y)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                duck_x, duck_y = move_up(game, assets, duck_x, duck_y)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                duck_x, duck_y = move_left(game, assets, duck_x, duck_y)
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                duck_x, duck_y = move_right(game, assets, duck_x, duck_y)

        game.screen.blit(assets.duck2_sprite, (duck_x, duck_y))
        game.update_display()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()