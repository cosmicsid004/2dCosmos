import pygame
import math

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

# 100 pixels to 1 meter
PPM = 100 

gravity = 9.8 * PPM #m/s^2
throwSpeedMPS = 1 #m/s
throwStrength = throwSpeedMPS * PPM
angle = 45
onGround = True

while running:
    dt = clock.tick(60) / 1000.0 # delta time in seconds
    for event in pygame.event.get(): # to stop the window
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                running = False

            if event.key == pygame.K_SPACE and onGround:
                vx = throwStrength * math.cos(math.radians(angle))
                vy = -throwStrength * math.sin(math.radians(angle))
                onGround = False

    if not onGround:
        vy += gravity * dt
        x += vx * dt
        y += vy * dt

    if y >= 700:
        y = 700
        vy = 0
        vx = 0
        onGround = True

    game_display.blit(bg_image, (0, 0)) #Draws (blits) the background image onto the game window at position (0, 0)
    game_display.blit(ball, (x, y))
    pygame.display.update() # Updates the entire display to show the latest changes on the screen

pygame.quit()