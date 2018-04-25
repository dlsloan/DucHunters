import pygame
import Sprite


class GameScreen:
    def __init__():
        pygame.init()
        self._step_sound = pygame.mixer.Sound('assets/sfx/step2.wav')
        pygame.display.set_caption('minimal program')



# define a main function
def main():
    # initialize the pygame module
    pygame.init()
    sound = pygame.mixer.Sound("assets/sfx/step2.wav")
    sound.play()
    # load and set the logo
    #logo = pygame.image.load("logo32x32.png")
    #pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")

    testS = Sprite.Sprite(pygame.image.load('assets/sprites/baton.png'))

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800, 600))

    # define a variable to control the main loop
    running = True
    spin = 0
    dist = 0
    # main loop
    while running:
        screen.fill((128, 0, 128))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        dist += 1
        testS.draw(screen, (50, 50), spin)
        pos = pygame.math.Vector2(0, -dist)
        pos = pos.rotate(-spin)
        pos += pygame.math.Vector2(50, 50)
        testS.draw(screen, pos, spin)
        spin += 1
        if (spin >= 360) :
            spin -= 360
        pygame.time.delay(20)
        pygame.display.flip()

#def runSound() :



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()