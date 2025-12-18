import pygame
import math
import tkinter as tk
from classBall import Ball

#______________TKINTER___________________________________
root = tk.Tk()
root.title("Control PLanel")
tkHeight = 120
tkWidth = 1280
root.geometry(f"{tkWidth}x{tkHeight}+{320}+{0}")

v = tk.Scale(root, from_= 0, to=100, width=40, length=400, label="Speed(m/s)", orient="horizontal")
g = tk.Scale(root, from_= 0, to=100, width=40, length=400, label="Gravity(m/s2)", orient="horizontal")
a = tk.Scale(root, from_= 0, to=90, width=40, length=400, label="Angle(dgree)", orient="horizontal")
airRes = tk.DoubleVar(value=1.0)
airResButton = tk.Checkbutton(root, text="Air Resistence", variable=airRes, onvalue=0.999, offvalue=1.0)

airResButton.pack()
v.pack(side="left", padx=10)
g.pack(side="left", padx=10)
a.pack(side="left", padx=10)

#------PYGAME-------------------------
pygame.init()

window_width = 1280
window_height = 850
game_display = pygame.display.set_mode((window_width, window_height))

bg_image = pygame.image.load('background.jpeg').convert()
ball_image = pygame.image.load('ball.png').convert_alpha()
ball_image = pygame.transform.scale(ball_image, (150, 150))

clock = pygame.time.Clock() # to limit the FPS
running = True

ball_radius = 50  # got from hit and trial

restitution = 0.6 #bounce 
friction = 0.85 #ground
stop_threshold = 30
air_drag = 0.999

PPM = 50 # 50 pixels to 1 meter
ground_y = 700 # the floor
right_wall = 1200

ball = Ball()

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

            if event.key == pygame.K_SPACE and ball.onGround:
                ball.throw(throwStrength, angle)

    if not ball.onGround:
        ball.update(dt, gravity, airRes.get())

    if ball.y + ball_radius >= ground_y:
        ball.y = ground_y - ball_radius
        
        if abs(ball.vy) > stop_threshold:
            ball.vy = -ball.vy * restitution
            ball.vx = ball.vx * friction
        else:
            ball.vx = 0
            ball.vy = 0
            ball.onGround = True

    if ball.x + ball_radius >= right_wall:
        ball.x = right_wall - ball_radius
        ball.vx = -ball.vx * restitution

    elif ball.x + ball_radius <= 0:
        ball.x = 0 - ball_radius
        ball.vx = -ball.vx * restitution


    game_display.blit(bg_image, (0, 0)) #Draws (blits) the background image onto the game window at position (0, 0)
    game_display.blit(ball_image, (ball.x, ball.y)) #drawing from sentre
    pygame.display.update() # Updates the entire display to show the latest changes on the screen
    root.update()

pygame.quit()