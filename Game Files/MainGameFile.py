import pygame
import sys
import os

(width, height) = (800, 600)
background_color = (255, 0, 255)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("ScrollLandia")
screen.fill(background_color)
pygame.display.flip()

y = 425
x = 50
width = 40
height = 60
vel = 5

running = True
while running:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and x > vel:
        x -= vel
    if keys[pygame.K_d] and x < 500 - 40:
        x += vel
    if keys[pygame.K_w] and y > vel:
        y -= vel
    if keys[pygame.K_s] and y < 500 - 40:
        y += vel

    screen.fill((0, 0, 0)) 
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pygame.display.update()
