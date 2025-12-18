import math

class Ball:
    def __init__(self):
        self.x, self.y = 10, 700
        self.vx, self.vy = 0, 0
        self.onGround = True

    def throw(self, speed, angle):
        self.vx = speed * math.cos(math.radians(angle))
        self.vy = -speed * math.sin(math.radians(angle))
        self.onGround = False

    def update(self, dt, gravity, air_drag):
        if not self.onGround:
            self.vy += gravity * dt
            self.vy *= air_drag
            self.vx *= air_drag

            self.x += self.vx * dt
            self.y += self.vy * dt