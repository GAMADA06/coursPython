import pygame
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

GRAVITY = 1

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mon Jumpy")

jumpy_image = pygame.image.load('assets/doddle.png').convert_alpha()
bg_image = pygame.image.load("assets/bg_doddle.png").convert_alpha()


class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(jumpy_image, (50, 50))
        self.width = 30
        self.height = 40
        self.velocity = 0
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.flip = False

    def move(self):
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            dx = -10
            self.flip = True
        if keys[pygame.K_d]:
            dx = 10
            self.flip = False

        #gravity
        self.velocity += GRAVITY
        dy += self.velocity

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right


        if self.rect.bottom + dy > SCREEN_HEIGHT:
            dy = 0
            self.velocity = -20


        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.rect.x - 15, self.rect.y - 5))
        # pygame.draw.rect(screen, WHITE, self.rect, 2)



jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

run = True
while run:
    clock.tick(FPS)
    jumpy.move()

    screen.blit(bg_image, (0,0))
    jumpy.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()