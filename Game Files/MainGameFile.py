from pygame import *

(widdth, heiight) = (800, 600)
screen = pygame.display.set_mode((widdth, heiight))
pygame.display.set_caption("ScrollLandia")
background = (222, 222, 22, 0)
y = 40
x = 40
width = 40
twoy = 400
height = 40
vel = 5
screen.fill(background)
pygame.display.flip()

count = 20
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 740:
        x += vel
        count = count + 20
    if keys[pygame.K_UP] and y > vel - 10:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - vel:
        y += vel

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255, 255), (x, y, width, height))
    screen2 = pygame.draw.rect(screen, (255, 255, 2, 255), (0, 530, 900, 90))
    pygame.display.update()
