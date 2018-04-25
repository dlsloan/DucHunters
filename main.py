


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

    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((800, 600))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

#def runSound() :



# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()