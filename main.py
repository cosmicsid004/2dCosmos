import pygame
pygame.init()

window_width = 1280
window_height = 850
game_display = pygame.display.set_mode((window_width, window_height))

bg_image = pygame.image.load('background.jpeg').convert()
ball = pygame.image.load('ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (150, 150))

clock = pygame.time.Clock() # to limit the FPS
keys = pygame.key.get_pressed()
running = True

x = 10
y = 700
vx = 0
vy = 0

gravity = 2560
throwStrength = -1200
onGround = True

while running:
    dt = clock.tick(60) / 1000.0 # delta time in seconds
    for event in pygame.event.get(): # to stop the window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                running = False

            if event.key == pygame.K_SPACE:
                vy = throwStrength
                onGround = False

    vy += gravity * dt
    y += vy * dt

    if y >= 700:
        y = 700
        vy = 0
        onGround = True

    game_display.blit(bg_image, (0, 0)) #Draws (blits) the background image onto the game window at position (0, 0)
    game_display.blit(ball, (x, y))
    pygame.display.update() # Updates the entire display to show the latest changes on the screen

pygame.quit()