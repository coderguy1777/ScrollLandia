import pygame

(width, height) = (1920, 1080) # Sets up the dimensions of the window
screen = pygame.display.set_mode((width, height)) # Creates the Screen window, with a 1920 * 1080 dimension.

#Is the loop where a boolean running is present that is set as true, and until you close it out, it becomes false, ending the program when it is close out.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
