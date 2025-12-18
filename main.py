import pygame
import math
import tkinter as tk

#______________TKINTER___________________________________
root = tk.Tk()
root.title("Control PLanel")
tkHeight = 150
tkWidth = 1280
root.geometry(f"{tkWidth}x{tkHeight}+{320}+{0}")

v = tk.Scale(root, from_= 0, to=100, width=40, length=400, label="Speed(m/s)", orient="horizontal")
g = tk.Scale(root, from_= 0, to=100, width=40, length=400, label="Gravity(m/s2)", orient="horizontal")
a = tk.Scale(root, from_= 0, to=90, width=40, length=400, label="Angle(dgree)", orient="horizontal")

v.pack(side="left", padx=10)
g.pack(side="left", padx=10)
a.pack(side="left", padx=10)

#------PYGAME-------------------------
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

restitution = 0.6 #bounce 
friction = 0.85 #ground
stop_threshold = 30
air_drag = 0.999

x, y = 10, 700
vx = vy = 0
PPM = 50 # 50 pixels to 1 meter
onGround = True
ground_y = 700 # the floor

while running:
    dt = clock.tick(60) / 1000.0 # delta time in seconds

    throwSpeed = v.get()
    gravity = g.get() * PPM
    angle = a.get()

    throwStrength = throwSpeed * PPM

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
        vx *= air_drag # resistence due to air drag
        vy *= air_drag

        x += vx * dt
        y += vy * dt

    if y >= ground_y:
        y = ground_y
        
        if abs(vy) > stop_threshold:
            vy = -vy * restitution
            vs = vx * friction
        else:
            vx = 0
            vy = 0
            onGround = True

    game_display.blit(bg_image, (0, 0)) #Draws (blits) the background image onto the game window at position (0, 0)
    game_display.blit(ball, (x, y))
    pygame.display.update() # Updates the entire display to show the latest changes on the screen
    root.update()

pygame.quit()