import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("My Mario Game")

player = pygame.Rect(100, 400, 40, 40)

speed = 5
jump = False
velocity = 0

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Move left/right
    if keys[pygame.K_LEFT]:
        player.x -= speed

    if keys[pygame.K_RIGHT]:
        player.x += speed

    # Jump
    if keys[pygame.K_SPACE] and not jump:
        jump = True
        velocity = -15

    # Gravity
    if jump:
        player.y += velocity
        velocity += 1

        if player.y >= 400:
            player.y = 400
            jump = False

    # Draw
    screen.fill((100, 180, 255))

    # Ground
    pygame.draw.rect(screen, (50, 180, 50), (0, 440, 800, 60))

    # Player
    pygame.draw.rect(screen, (255, 0, 0), player)

    pygame.display.update()

pygame.quit()