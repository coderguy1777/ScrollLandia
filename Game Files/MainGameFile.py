import pygame


width = 960
height = 540
fps = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
vec = pygame.Vector2

pygame.init()
pygame.mixer.init()
title = pygame.display.set_caption("ScrollLandia")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = width / 2
        self.rect.bottom = height - 10
        self.speedx = vec(0, 0)
        self.speedy = vec(0, 0)
        self.pos = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        self.pos = self.rect.midbottom
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_d]:
            self.speedx = 10

        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        if keystate[pygame.K_a]:
            self.speedx = -10
        self.rect.x += self.speedx
        if keystate[pygame.K_w]:
            self.speedy = -10
        if keystate[pygame.K_s]:
            self.speedy = 10
        self.rect.y += self.speedy
        if self.rect.right > width:
            self.rect.right = width
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > height:
            self.rect.bottom = height
        if self.rect.top < 0:
            self.rect.top = 0

    def test(self):
        return self.speedx



gamesprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
player = Player()
gamesprites.add(player)
plat = Platform(0, height - 40, width, 40)
platforms.add(plat)



running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gamesprites.update()
    platforms.update()
    screen.fill(BLACK)
    gamesprites.draw(screen)
    platforms.draw(screen)
    if player.rect.bottom > plat.rect.top:
        player.rect.bottom = plat.rect.top
    if player.rect.top < 10:
        player.rect.top = 10

    if player.rect.top > plat.rect.bottom:
        player.rect.top = 10
    pygame.display.flip()
    print(player.test())
    print(player.rect.midbottom)

pygame.quit()